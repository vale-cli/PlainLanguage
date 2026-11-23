# PlainLanguage

[Vale](https://vale.sh) styles for the
[Federal Plain Language Guidelines](https://github.com/GSA/plainlanguage.gov/tree/main/_pages/guidelines),
the United States government's rules for writing that people can read the
first time: simple words, "must" for a requirement, verbs instead of the
nouns that hide them, no legalese, positive statements, short sentences and
paragraphs, defined abbreviations, and the active voice.

Works on [Markdown](https://docs.vale.sh/formats/markdown),
[HTML](https://docs.vale.sh/formats/html),
[AsciiDoc](https://docs.vale.sh/formats/asciidoc),
[reStructuredText](https://docs.vale.sh/formats/restructuredtext),
[Org](https://docs.vale.sh/formats/org), and
[plain text](https://docs.vale.sh/formats/text). `LinkText`, `PDFLinks`,
`HowToHeadings`, and `FAQ` read links and headings, so they need a markup
format.

## Install

Requires Vale 3.20.0 or later, and builds on
[Std](https://github.com/vale-cli/Std), the standard library the sentence,
passive, and acronym rules extend. Sync pulls Std in; it stays present
without being enabled.

```ini
StylesPath = styles
Packages = https://github.com/vale-cli/PlainLanguage/releases/latest/download/PlainLanguage.zip

[*.{md,html}]
BasedOnStyles = PlainLanguage
```

```console
$ vale sync
```

`PlainLanguage` is the core style. `Strict` is the rest of the
guidelines' word list, for agency writing; add it beside the core.

| Style | What it checks |
| ----- | -------------- |
| `PlainLanguage` | The checkable guidelines. See below. |
| `Strict` | The entries of "Use simple words and phrases" that are often the right word elsewhere: `provide`, `require`, `request`, `submit`, `option`, `however`. Every one is a suggestion with a fix. |

### Core rules

| Rule | Guideline | Examples flagged |
| ---- | --------- | ---------------- |
| `SimpleWords` | Use simple words and phrases | `commence`, `utilize`, `in order to`, `prior to`, `ensure` |
| `Shall` | Use "must" to indicate requirements | `shall`, `shall not` |
| `HiddenVerbs` | Avoid hidden verbs | `made a decision`, `conduct an analysis of`, `give consideration to` |
| `Legalese` | Avoid jargon | `herein`, `pursuant to`, `in accordance with`, `heretofore`, `aforementioned` |
| `Jargon` | Avoid jargon | `touch base`, `best practices`, `value added` |
| `Wordy` | Be concise | `at this point in time`, `is able to`, `on a monthly basis`, `due and payable` |
| `Omit` | Use simple words and phrases | `please be advised that`, `in the process of`, `the month of` |
| `Modifiers` | Be concise | `really`, `very`, `totally`, `quite` |
| `Openers` | Use simple words and phrases | `It is important that`, `The following information must`, `There are many people who` |
| `DoubleNegatives` | Use positive language | `no fewer than`, `does not become void unless`, `not unreasonable`, `except ... unless` |
| `Slashes` | Don't use slashes | `and/or`, `faculty/staff` |
| `Pronouns` | Address the user | `he or she`, `his or her` |
| `PassiveVoice` | Use active voice | `were proposed`, `must be included` |
| `SentenceLength` | Write short sentences | a sentence over 25 words |
| `ParagraphLength` | Write short paragraphs | a paragraph over 150 words |
| `Acronyms` | Minimize abbreviations | `ESAC` before `Engineering Safety Advisory Committee (ESAC)` |
| `LinkText` | Write effective links | `click here`, `read more` |
| `HowToHeadings` | Effective headings | `## How to get a permit` |
| `NounStack` | Avoid noun strings | `mine worker safety rules` |
| `CrossReferences` | Minimize cross-references | `Section 18`, `paragraph (b)`, `§ 12`, `under subsection` |
| `FAQ` | Avoid FAQs | `## FAQ`, `## Frequently asked questions` |
| `PDFLinks` | Avoid PDF overload | `[annual report](report.pdf)`, `<a href="report.pdf">` |
| `ExceptionsFirst` | Place the main idea before exceptions and conditions | `Except as described in ...`, `Notwithstanding ...`, `Subject to ...`, a long opening `Unless` clause |
| `Will` | Use the present tense | `will be required to`, `will need to`, `will be able to` |
| `Definitions` | Minimize definitions | `For the purposes of this part`, `the term "farm" means`, `As used in this section` |
| `Only` | Place words carefully | `You only need to`, `are only required to` |

Every rule file starts with a comment naming the guideline it comes from
and links to it. The word rules carry a fix: each verb is listed in its four
forms, so `commenced` suggests `started` and `is commencing` suggests
`is starting`, and a replacement takes the case of the word it replaces.

## Configuration

Limits are parameters, so you can change them without editing the rule:

```ini
[*.md]
BasedOnStyles = PlainLanguage, Strict
PlainLanguage.SentenceLength[max] = 20
PlainLanguage.ParagraphLength[max] = 250
PlainLanguage.PassiveVoice = NO
```

`Acronyms` accepts the abbreviations the guidelines call common knowledge,
such as `FBI` and `ATM`, and Std's list of common technical ones, such as
`API`, `HTML`, `JSON`, and `URL`. Your own go in a
[vocabulary](https://docs.vale.sh/topics/vocab), which the rule reads:

```
styles/config/vocabularies/Agency/accept.txt
```

```ini
Vocab = Agency
```

Technical writing uses more abbreviations its readers know than Std lists,
such as `CI`, `YAML`, and `INI`. Add those to the vocabulary too, one per
line, and `Acronyms` stops asking for them.

A definition counts from the point it appears: `ESAC` before
`Engineering Safety Advisory Committee (ESAC)` is flagged, and every use
after it is not.

## What it doesn't check

Most of the guidelines are about the reader and the structure: write for
your audience, organize around their questions, put the main point first,
use one term for one thing, keep subjects and verbs together, use lists,
tables, and headings, and test with real readers. A linter can't tell who
the reader is or whether the order serves them.

Some are checkable only roughly, and are left out rather than guessed at:

- Present tense beyond the requirement phrases `Will` knows, and
  contractions. The guidelines ask for them "where they sound natural",
  which a rule can't judge.
- Conditions and exceptions in the middle or at the end of a sentence.
  `ExceptionsFirst` reads only the opening, and leaves a short `Unless`
  clause alone, as the guidelines do.
- The boomerang, a cross-reference to the section it's in. A rule can't
  tell which section it's reading.
- At most three abbreviations in a document. A rule can count uses, not
  distinct abbreviations.
- The simple-words entries with no fixed meaning: `subject`, `type`,
  `said, some, such`, `vice`, and `this activity, command`.

`NounStack` reads parts of speech, so it misses some stacks and flags a few
that aren't; `Only` reads "only" after a pronoun, so `You only need` is
flagged and `You need only` is not. `PassiveVoice` finds a form of "be" and a past
participle. The guidelines
allow the passive when the law is the actor or the actor doesn't matter,
so it's a suggestion; participles used as adjectives, `is located`, `are
required`, are left alone.

## Sources

plainlanguage.gov now redirects to digital.gov, which carries part of the
guidelines. Each rule links to its page in the archive of the original site
that GSA keeps on GitHub:

| Guideline | Rules |
| --------- | ----- |
| [Use simple words and phrases](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/words/use-simple-words-phrases.md) | `SimpleWords`, `Omit`, `Openers`, `Strict.Words` |
| [Use "must" to indicate requirements](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/conversational/use-must-to-indicate-requirements.md) | `Shall` |
| [Avoid hidden verbs](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/words/avoid-hidden-verbs.md) | `HiddenVerbs` |
| [Avoid jargon](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/words/avoid-jargon.md) | `Legalese`, `Jargon` |
| [Be concise](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/concise/index.md) | `Wordy`, `Modifiers` |
| [Use positive language](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/concise/use-positive-language.md) | `DoubleNegatives` |
| [Don't use slashes](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/conversational/dont-use-slashes.md) | `Slashes` |
| [Address the user](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/audience/address-the-user.md) | `Pronouns` |
| [Use active voice](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/conversational/use-active-voice.md) | `PassiveVoice` |
| [Write short sentences](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/concise/write-short-sentences.md) | `SentenceLength` |
| [Write short paragraphs](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/concise/write-short-paragraphs.md) | `ParagraphLength` |
| [Minimize abbreviations](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/words/minimize-abbreviations.md) | `Acronyms` |
| [Write effective links](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/web/write-effective-links.md) | `LinkText` |
| [Effective headings](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/organize/effective-headings.md) | `HowToHeadings` |
| [Avoid noun strings](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/words/avoid-noun-strings.md) | `NounStack` |
| [Minimize cross-references](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/design/minimize-cross-references.md) | `CrossReferences` |
| [Avoid FAQs](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/web/avoid-faqs.md) | `FAQ` |
| [Avoid PDF overload](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/web/avoid-pdf-overload.md) | `PDFLinks` |
| [Place the main idea before exceptions and conditions](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/organize/place-the-main-idea-before-exceptions-and-conditions.md) | `ExceptionsFirst` |
| [Use the present tense](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/conversational/use-the-present-tense.md) | `Will` |
| [Minimize definitions](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/words/minimize-definitions.md) | `Definitions` |
| [Place words carefully](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/words/place-words-carefully.md) | `Only` |

## Development

`./test.sh` runs each rule's own cases with `vale test --coverage`, then
checks `fixtures/page.md` and `fixtures/page.html` against the golden files
in `testdata/` and requires their rewrites in `fixtures/clean/` to pass
clean. `./test.sh -u` rewrites the golden files. The test runner needs Vale
3.24.0 or later, and a [Std](https://github.com/vale-cli/Std) checkout
beside this repository, or `STD` pointing at its `Std` directory.

The swap lists of `SimpleWords`, `HiddenVerbs`, and `Strict.Words` are
generated, with every verb written out in its forms. Edit the lists in
`script/words.py` and run it to rewrite them; it leaves each rule's header
and tests alone.

## License

MIT. The word lists are transcribed from the Federal Plain Language
Guidelines, a public-domain work of the United States government; see
[NOTICE](NOTICE).
