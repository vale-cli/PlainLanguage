#!/usr/bin/env python3
"""Regenerate the swap lists of SimpleWords, HiddenVerbs, and Strict.Words.

    $ script/words.py

The lists are the guidelines' "Use simple words and phrases" and "Avoid
hidden verbs", with each verb written out in its forms so a fix keeps the
tense: "commenced" suggests "started". Only the block under `swap:` is
rewritten; each rule's header and tests are left as they are.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent / "PlainLanguage" / "styles"

# (forms, replacements): forms is "base 3s past ing" (use - to skip a form);
# replacements is the matching list, alternatives joined by '|'.
def V(forms, repl):
    return (forms.split(), repl.split())

# Entries with no verb forms: key, value.
CORE_PLAIN = [
    ("accorded", "given"),
    ("accordingly", "so"),
    ("additional", "added|more|other"),
    ("addressees are requested to", "please"),
    ("addressees", "you"),
    ("adjacent to", "next to"),
    ("adversely impact on", "hurt|set back"),
    ("afford an opportunity", "allow|let"),
    ("a number of", "some|several|many"),
    ("apparent", "clear|plain"),
    ("appreciable", "many"),
    ("approximately", "about"),
    ("arrive onboard", "arrive"),
    ("as a means of", "to"),
    ("as prescribed by", "in|under"),
    ("assistance", "help|aid"),
    ("at the present time", "now|at present"),
    ("by means of", "by|with"),
    ("capability", "ability"),
    ("capabilities", "abilities"),
    ("caveat", "warning"),
    ("caveats", "warnings"),
    ("in close proximity to", "near"),
    ("close proximity", "nearness"),
    ("concerning", "about|on"),
    ("consequently", "so"),
    ("currently", "now"),
    ("due to the fact that", "because|since"),
    ("during the period of", "during"),
    ("effect modifications", "make changes"),
    ("equipments", "equipment"),
    ("equitable", "fair"),
    ("evidenced", "showed"),
    ("evident", "clear"),
    ("expeditious", "fast|quick"),
    ("expeditiously", "quickly"),
    ("expertise", "skill|ability"),
    ("failed to", "didn't"),
    ("feasible", "workable|possible"),
    ("for a period of", "for"),
    ("frequently", "often"),
    ("has a requirement for", "needs"),
    ("have a requirement for", "need"),
    ("identical", "same"),
    ("impacted", "affected|changed"),
    ("in addition", "also|besides|too"),
    ("in an effort to", "to"),
    ("inasmuch as", "since"),
    ("in a timely manner", "on time|promptly"),
    ("inception", "start"),
    ("indication", "sign"),
    ("in lieu of", "instead of"),
    ("in order that", "so|so that"),
    ("in order to", "to"),
    ("in regard to", "about|on"),
    ("with regard to", "about|on"),
    ("in relation to", "about|with|to"),
    ("interpose no objection", "don't object"),
    ("in the amount of", "for"),
    ("in the event of", "if"),
    ("in the event that", "if"),
    ("in the near future", "soon"),
    ("in view of the above", "so"),
    ("in view of", "since|because"),
    ("is applicable to", "applies to"),
    ("are applicable to", "apply to"),
    ("is authorized to", "may"),
    ("are authorized to", "may"),
    ("is in consonance with", "agrees with|follows"),
    ("is responsible for", "handles"),
    ("it appears", "it seems"),
    ("magnitude", "size"),
    ("methodology", "method"),
    ("methodologies", "methods"),
    ("no later than", "by"),
    ("not later than", "by"),
    ("numerous", "many"),
    ("optimum", "best|most"),
    ("pertaining to", "about|on|of"),
    ("portion", "part"),
    ("portions", "parts"),
    ("practicable", "practical"),
    ("previous", "earlier"),
    ("previously", "before|earlier"),
    ("prior to", "before"),
    ("proficiency", "skill"),
    ("provided that", "if"),
    ("provides guidance for", "guides"),
    ("regarding", "about|on"),
    ("remainder", "rest"),
    ("remuneration", "pay|payment"),
    ("similar to", "like"),
    ("state-of-the-art", "latest|newest"),
    ("subsequent", "later|next"),
    ("subsequently", "later|then"),
    ("substantial", "large|much"),
    ("successfully complete", "complete|pass"),
    ("successfully completed", "completed|passed"),
    ("sufficient", "enough"),
    ("therefore", "so"),
    ("time period", "time|period"),
    ("until such time as", "until"),
    ("utilization", "use"),
    ("viable", "workable|practical"),
    ("whereas", "because|since"),
    ("with reference to", "about"),
    ("with the exception of", "except|except for"),
    ("witnessed", "saw"),
]

CORE_VERBS = [
    V("accomplish accomplishes - accomplishing", "do|carry_out does|carries_out - doing|carrying_out"),
    V("accrue accrues accrued accruing", "add|gain adds|gains added|gained adding|gaining"),
    V("anticipate anticipates anticipated anticipating", "expect expects expected expecting"),
    V("ascertain ascertains ascertained ascertaining", "find_out|learn finds_out|learns found_out|learned finding_out|learning"),
    V("assist assists assisted assisting", "help helps helped helping"),
    V("attain attains attained attaining", "meet|reach meets|reaches met|reached meeting|reaching"),
    V("attempt attempts attempted attempting", "try tries tried trying"),
    V("commence commences commenced commencing", "start|begin starts|begins started starting|beginning"),
    V("comply_with complies_with complied_with complying_with", "follow follows followed following"),
    V("comprise comprises - comprising", "make_up|include makes_up|includes - making_up|including"),
    V("consolidate consolidates consolidated consolidating", "combine|merge combines|merges combined|merged combining|merging"),
    V("constitute constitutes - constituting", "make_up|form makes_up|forms - making_up|forming"),
    V("convene convenes convened convening", "meet meets met meeting"),
    V("deem deems deemed deeming", "consider|think considers|thinks considered|thought considering|thinking"),
    V("demonstrate demonstrates demonstrated demonstrating", "show|prove shows|proves showed|proved showing|proving"),
    V("depart departs departed departing", "leave leaves left leaving"),
    V("designate designates - designating", "name|choose names|chooses - naming|choosing"),
    V("desire desires desired desiring", "want|wish wants|wishes wanted wanting"),
    V("determine determines - determining", "decide|find decides|finds - deciding|finding"),
    V("disclose discloses - disclosing", "show|tell shows|tells - showing|telling"),
    V("discontinue discontinues discontinued discontinuing", "stop|drop stops|drops stopped|dropped stopping|dropping"),
    V("disseminate disseminates disseminated disseminating", "send|issue sends|issues sent|issued sending|issuing"),
    V("eliminate eliminates eliminated eliminating", "cut|drop|end cuts|drops|ends cut|dropped|ended cutting|dropping|ending"),
    V("endeavor endeavors endeavored endeavoring", "try tries tried trying"),
    V("ensure ensures ensured ensuring", "make_sure makes_sure made_sure making_sure"),
    V("enumerate enumerates enumerated enumerating", "count|list counts|lists counted|listed counting|listing"),
    V("exhibit exhibits exhibited exhibiting", "show shows showed showing"),
    V("expedite expedites expedited expediting", "speed_up|hurry speeds_up|hurries sped_up|hurried speeding_up|hurrying"),
    V("expend expends expended expending", "spend spends spent spending"),
    V("facilitate facilitates facilitated facilitating", "help|ease helps|eases helped|eased helping|easing"),
    V("finalize finalizes finalized finalizing", "finish|complete finishes|completes finished|completed finishing|completing"),
    V("forfeit forfeits forfeited forfeiting", "lose|give_up loses|gives_up lost|gave_up losing|giving_up"),
    V("furnish furnishes - -", "give|send gives|sends - -"),
    V("indicate indicates indicated indicating", "show shows showed showing"),
    V("initiate initiates initiated initiating", "start starts started starting"),
    V("modify modifies modified modifying", "change changes changed changing"),
    V("necessitate necessitates necessitated necessitating", "need|require needs|requires needed|required needing|requiring"),
    V("notify notifies notified notifying", "tell tells told telling"),
    V("obligate obligates obligated obligating", "bind|require binds|requires bound|required binding|requiring"),
    V("participate participates participated participating", "take_part takes_part took_part taking_part"),
    V("possess possesses possessed possessing", "have|own has|owns had|owned having|owning"),
    V("preclude precludes precluded precluding", "prevent prevents prevented preventing"),
    V("prioritize prioritizes prioritized prioritizing", "rank ranks ranked ranking"),
    V("proceed - proceeded -", "go_ahead|continue - went_ahead|continued -"),
    V("procure procures procured procuring", "get|buy gets|buys got|bought getting|buying"),
    V("promulgate promulgates promulgated promulgating", "issue|publish issues|publishes issued|published issuing|publishing"),
    V("purchase purchases purchased purchasing", "buy buys bought buying"),
    V("relocate relocates relocated relocating", "move moves moved moving"),
    V("reside resides resided residing", "live lives lived living"),
    V("retain retains retained retaining", "keep keeps kept keeping"),
    V("solicit solicits solicited soliciting", "ask_for asks_for asked_for asking_for"),
    V("terminate terminates terminated terminating", "end|stop ends|stops ended|stopped ending|stopping"),
    V("transmit transmits transmitted transmitting", "send sends sent sending"),
    V("utilize utilizes utilized utilizing", "use uses used using"),
]

STRICT_PLAIN = [
    ("aircraft", "plane"),
    ("appropriate", "proper|right"),
    ("approximate", "about"),
    ("combat environment", "combat"),
    ("combined", "joint"),
    ("component", "part"),
    ("components", "parts"),
    ("contains", "has"),
    ("expiration", "end"),
    ("females", "women"),
    ("however", "but"),
    ("immediately", "at once|now"),
    ("initial", "first"),
    ("liaison", "discussion"),
    ("limited number", "limits"),
    ("maximum", "most|largest|greatest"),
    ("minimum", "least|smallest"),
    ("objective", "aim|goal"),
    ("option", "choice|way"),
    ("options", "choices|ways"),
    ("parameters", "limits"),
    ("relative to", "about|on"),
    ("represents", "is"),
    ("requirement", "need"),
    ("requirements", "needs"),
    ("selection", "choice"),
    ("timely", "prompt"),
    ("your office", "you"),
]

STRICT_VERBS = [
    V("address addresses addressed addressing", "discuss discusses discussed discussing"),
    V("advise advises advised advising", "tell|recommend tells|recommends told|recommended telling|recommending"),
    V("allocate allocates allocated allocating", "divide|give divides|gives divided|gave dividing|giving"),
    V("benefit benefits benefited benefiting", "help helps helped helping"),
    V("delete deletes deleted deleting", "cut|drop cuts|drops cut|dropped cutting|dropping"),
    V("elect elects - electing", "choose|pick chooses|picks - choosing|picking"),
    V("employ employs employed employing", "use uses used using"),
    V("encounter encounters encountered encountering", "meet|find meets|finds met|found meeting|finding"),
    V("establish establishes established establishing", "set_up|show sets_up|shows set_up|showed setting_up|showing"),
    V("forward forwards forwarded forwarding", "send sends sent sending"),
    V("function functions functioned functioning", "work|act works|acts worked|acted working|acting"),
    V("identify identifies identified identifying", "find|name|show finds|names|shows found|named|showed finding|naming|showing"),
    V("implement implements implemented implementing", "carry_out|start carries_out|starts carried_out|started carrying_out|starting"),
    V("interface interfaces interfaced interfacing", "meet|work_with meets|works_with met|worked_with meeting|working_with"),
    V("maintain maintains maintained maintaining", "keep|support keeps|supports kept|supported keeping|supporting"),
    V("minimize minimizes minimized minimizing", "decrease|reduce decreases|reduces decreased|reduced decreasing|reducing"),
    V("monitor monitors monitored monitoring", "check|watch checks|watches checked|watched checking|watching"),
    V("observe observes observed observing", "see sees saw seeing"),
    V("operate operates operated operating", "run|use|work runs|uses|works ran|used|worked running|using|working"),
    V("perform performs performed performing", "do does did doing"),
    V("- - permitted permitting", "- - let letting"),
    V("provide provides provided providing", "give|offer gives|offers gave|offered giving|offering"),
    V("reflect reflects reflected reflecting", "say|show says|shows said|showed saying|showing"),
    V("remain remains remained remaining", "stay stays stayed staying"),
    V("render renders rendered rendering", "give|make gives|makes gave|made giving|making"),
    V("request requests requested requesting", "ask asks asked asking"),
    V("require requires required requiring", "need needs needed needing"),
    V("submit submits submitted submitting", "give|send gives|sends gave|sent giving|sending"),
    V("validate validates validated validating", "confirm confirms confirmed confirming"),
    V("warrant warrants warranted warranting", "call_for|permit calls_for|permits called_for|permitted calling_for|permitting"),
]

# Hidden verbs: (light verbs by tense, noun phrase, verb by tense).
LIGHT = {
    "make": "make makes made made making",
    "reach": "reach reaches reached reached reaching",
    "conduct": "conduct conducts conducted conducted conducting",
    "perform": "perform performs performed performed performing",
    "carry out": "carry_out carries_out carried_out carried_out carrying_out",
    "undertake": "undertake undertakes undertook undertaken undertaking",
    "give": "give gives gave given giving",
    "take": "take takes took taken taking",
    "have": "have has had had having",
    "gain": "gain gains gained gained gaining",
    "provide": "provide provides provided provided providing",
}
ANALYZE = ["conduct", "perform", "carry out", "undertake"]
HIDDEN = [
    (["make", "reach"], "a decision", "decide decides decided deciding"),
    (["make"], "an application", "apply applies applied applying"),
    (["make"], "(?:a |the )?payment of", "pay pays paid paying"),
    (["make"], "a payment", "pay pays paid paying"),
    (["make"], "a recommendation", "recommend recommends recommended recommending"),
    (["make"], "a suggestion", "suggest suggests suggested suggesting"),
    (["make"], "a determination(?: of)?", "determine determines determined determining"),
    (["make"], "an assumption", "assume assumes assumed assuming"),
    (["make"], "an adjustment(?: to)?", "adjust adjusts adjusted adjusting"),
    (["make"], "a choice", "choose chooses chose choosing"),
    (["make"], "an attempt", "try tries tried trying"),
    (["make"], "an inquiry", "ask asks asked asking"),
    (["make"], "a reduction (?:in|of)", "reduce reduces reduced reducing"),
    (["make"], "a contribution", "contribute contributes contributed contributing"),
    (["make"], "a revision (?:to|of)", "revise revises revised revising"),
    (ANALYZE, "an analysis of", "analyze analyzes analyzed analyzing"),
    (ANALYZE, "a review of", "review reviews reviewed reviewing"),
    (ANALYZE, "an investigation (?:of|into)", "investigate investigates investigated investigating"),
    (ANALYZE, "an assessment of", "assess assesses assessed assessing"),
    (ANALYZE, "an evaluation of", "evaluate evaluates evaluated evaluating"),
    (ANALYZE, "an inspection of", "inspect inspects inspected inspecting"),
    (ANALYZE, "an examination of", "examine examines examined examining"),
    (ANALYZE, "the calculation of", "calculate calculates calculated calculating"),
    (["give"], "consideration to", "consider considers considered considering"),
    (["take"], "into consideration", "consider considers considered considering"),
    (["give", "provide"], "an explanation of", "explain explains explained explaining"),
    (["give", "provide"], "a description of", "describe describes described describing"),
    (["give", "provide"], "assistance(?: to)?", "help helps helped helping"),
    (["give"], "approval for", "approve approves approved approving"),
    (["give"], "authorization for", "authorize authorizes authorized authorizing"),
    (["have"], "a need for", "need needs needed needing"),
    (["have"], "a discussion (?:of|about)", "discuss discusses discussed discussing"),
    (["have"], "an impact on", "affect affects affected affecting"),
    (["have"], "a tendency to", "tend to|tends to|tended to|tending to"),
    (["gain", "have"], "an understanding of", "understand understands understood understanding"),
    (["reach"], "an agreement", "agree agrees agreed agreeing"),
    (["reach"], "a conclusion", "conclude concludes concluded concluding"),
]


def words(s):
    return s.replace("_", " ")


def emit_plain(pairs):
    out = []
    for k, v in pairs:
        out.append(f"  '{k}': {v}")
    return out


def emit_verbs(verbs):
    out = []
    for forms, repl in verbs:
        for f, r in zip(forms, repl):
            if f == "-":
                continue
            out.append(f"  '{words(f)}': {words(r)}")
    return out


def emit_hidden():
    out = []
    for lights, noun, verb in HIDDEN:
        vforms = verb.split() if "|" not in verb else verb.split("|")
        # vforms: base 3s past ing; participle reuses past
        base, s3, past, ing = vforms
        tense_verbs = [base, s3, past, past, ing]
        for i in range(5):
            if i == 3:
                continue  # participle merged with past below
            forms = []
            for l in lights:
                lf = LIGHT[l].split()
                forms.append(words(lf[i]))
                if i == 2 and lf[3] != lf[2]:
                    forms.append(words(lf[3]))
            alt = forms[0] if len(forms) == 1 else "(?:" + "|".join(forms) + ")"
            out.append(f"  '{alt} {noun}': {tense_verbs[i]}")
    return out


def write(rule, lines):
    path = ROOT / rule
    text = path.read_text()
    head, rest = text.split("swap:\n", 1)
    tail = rest[rest.index("\n\ntests:"):]
    path.write_text(head + "swap:\n" + "\n".join(lines) + tail)


write("PlainLanguage/SimpleWords.yml", emit_plain(CORE_PLAIN) + emit_verbs(CORE_VERBS))
write("Strict/Words.yml", emit_plain(STRICT_PLAIN) + emit_verbs(STRICT_VERBS))
write("PlainLanguage/HiddenVerbs.yml", emit_hidden())
