#!/bin/sh
#
# Two checks. Each rule carries its cases in a `tests:` block, run in
# isolation by `vale test`, which with `--coverage` also requires every rule
# to fire in some case. Then one page per format is checked under the config
# the README gives and compared to a golden file, and its rewrite in
# fixtures/clean/ is required to produce nothing at all.
#
# The rewrite is the load-bearing half. A Vale rule that matches nothing
# loads, runs, and reports success, so "no alerts" only means something when
# a paired fixture proves the rules fire.
#
# `./test.sh -u` rewrites the golden files instead of comparing.
set -eu

update=0
[ "${1:-}" = "-u" ] && update=1
status=0

root=$(cd "$(dirname "$0")" && pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

# Some rules extend Std, so Std has to be present on the StylesPath --
# present, not enabled, exactly as sync would leave it. CI checks the repo
# out beside this one; locally the sibling clone serves.
vale=${VALE:-vale}
std=${STD:-$root/../Std/Std}
if [ ! -d "$std" ]; then
	echo "FAIL: Std not found at '$std'; set STD to a checkout's style directory" >&2
	exit 1
fi

cp -R "$root/PlainLanguage/styles" "$work/styles"
cp -R "$std" "$work/styles/Std"
mkdir -p "$root/testdata"

# The repository's config, pointed at the assembled StylesPath.
sed "s|^StylesPath = .*|StylesPath = $work/styles|" "$root/.vale.ini" > "$work/vale.ini"

# The in-source cases. Coverage is asked of this package's styles, not Std's.
(cd "$work" && "$vale" test --coverage styles/PlainLanguage styles/Strict) || status=1

# Alerts that share a line and column come back in whatever order the checks
# ran, and that order is not part of the contract. Sorting compares the set.
run() { # <fixture path, relative to root> -> alerts on stdout, sorted
	(cd "$root" && "$vale" --config "$work/vale.ini" --output=line --no-global "$1" 2>&1 || true) |
		sort -t: -k2,2n -k3,3n -k4,4
}

for f in page.md page.html; do
	golden=$root/testdata/$f.txt
	got=$(run "fixtures/$f")
	if [ "$update" -eq 1 ]; then
		printf '%s\n' "$got" > "$golden"
	elif [ ! -f "$golden" ]; then
		echo "FAIL $f: no golden file; run ./test.sh -u"
		status=1
	elif [ "$got" != "$(cat "$golden")" ]; then
		echo "FAIL $f"
		printf '%s\n' "$got" | diff -u "$golden" - || true
		status=1
	else
		echo "ok   $f ($(printf '%s' "$got" | grep -c . || true) alerts)"
	fi

	clean=$(run "fixtures/clean/$f")
	if [ -n "$clean" ]; then
		echo "FAIL clean/$f: the rewrite still violates the style"
		printf '%s\n' "$clean"
		status=1
	else
		echo "ok   clean/$f (clean)"
	fi
done

[ "$update" -eq 1 ] && echo "golden files rewritten"
exit $status
