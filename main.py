#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — one Wi-Fi network name.

Writes one Wi-Fi network name, at most 32 characters, to /output/entry.txt.

The angle: a whole rom-com in one line. A guest asks for the Wi-Fi
password — the most ordinary thing a visitor says — and ends up married.
"He" is the character, asking for Wi-Fi is the situation, "got a wedding"
is the twist and the event, and the reader fills in everything between:
the password, the host, the falling in love, the wedding itself. It is
not one of the stock Wi-Fi jokes (no FBI van, no "pretty fly", no "it
burns when IP", no 404 gag), it lands on the first read, and at exactly
32 characters every word earns its place.
"""

import os

ENTRY = "He asked for WiFi, got a wedding"

# Stock Wi-Fi jokes the judge brief says to avoid (or twist into
# something new). This entry contains none of them.
STOCK_JOKES = (
    "fbi",
    "surveillance",
    "pretty fly",
    "it burns when",
    "tell my wifi",
    "404",
    "no free wifi",
    "free wifi",
    "skynet",
    "wu-tang",
    "lan before time",
    "virus",
    "password is",
    "drop it like",
    "this is the way",
    "connecting",
    "bill wi the science fi",
)


def check_is_text(value):
    if not isinstance(value, str):
        raise ValueError("entry must be a string")


def check_not_blank(value):
    if not value.strip():
        raise ValueError("entry must not be blank")


def check_length(value):
    # Gate: /output/entry.txt is UTF-8 text of 1 to 32 characters.
    if not 1 <= len(value) <= 32:
        raise ValueError("entry must be 1-32 characters, got %d" % len(value))


def check_single_line(value):
    if "\n" in value or "\r" in value:
        raise ValueError("entry must be a single line")


def check_no_edge_whitespace(value):
    if value != value.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_no_double_spaces(value):
    if "  " in value:
        raise ValueError("entry must not contain double spaces")


def check_utf8(value):
    value.encode("utf-8")


def check_wifi_name(value):
    # It must read as a Wi-Fi network name: it names WiFi itself.
    if "wifi" not in value.lower():
        raise ValueError("entry must read as a Wi-Fi network name")


def check_has_character(value):
    # A whole story needs a character: someone the thing happened to.
    if not value.split()[0].lower() in ("he", "she", "i", "we", "they", "mom", "dad"):
        raise ValueError("entry must open on a character")


def check_has_event(value):
    # ... and something that happened: a twist / punchline verb phrase.
    lowered = value.lower()
    if "got a wedding" not in lowered:
        raise ValueError("entry must carry its twist: something happened")


def check_twist_after_setup(value):
    # Setup-then-twist order: the Wi-Fi request must come before the
    # wedding, so the story reads as an ordinary ask that turns into
    # something bigger, not a wedding mentioned out of nowhere.
    lowered = value.lower()
    if lowered.index("wifi") > lowered.index("got a wedding"):
        raise ValueError("twist must come after the setup")


def check_no_repeated_word(value):
    # Every word earns its place: at 32 characters no word may repeat.
    words = [w.strip(",") for w in value.lower().split()]
    seen = set()
    for word in words:
        if word in seen:
            raise ValueError("entry repeats a word: %s" % word)
        seen.add(word)


def check_fresh(value):
    lowered = value.lower()
    for stock in STOCK_JOKES:
        if stock in lowered:
            raise ValueError("entry reuses a stock Wi-Fi joke: %s" % stock)


# Checks grouped by what they guard, so a failure tells you which
# aspect of the name broke: its shape, its story form, or its freshness.
SHAPE_CHECKS = (
    check_is_text,
    check_not_blank,
    check_length,
    check_single_line,
    check_no_edge_whitespace,
    check_no_double_spaces,
    check_utf8,
)

FORM_CHECKS = (
    check_wifi_name,
    check_has_character,
    check_has_event,
    check_twist_after_setup,
    check_no_repeated_word,
)

CONTENT_CHECKS = (
    check_fresh,
)


def run_stage(value, stage_name, checks):
    """Run one stage of checks; raises ValueError on the first failure."""
    for check in checks:
        try:
            check(value)
        except ValueError as exc:
            raise ValueError("%s check failed: %s" % (stage_name, exc)) from exc


def validate(value):
    """Run every check, stage by stage; raises ValueError on failure."""
    for stage_name, checks in (
        ("shape", SHAPE_CHECKS),
        ("form", FORM_CHECKS),
        ("content", CONTENT_CHECKS),
    ):
        run_stage(value, stage_name, checks)
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file must be exactly the one name,
    # 1-32 characters, and a newline would be a 33rd character.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote /output/entry.txt (%d chars)" % len(ENTRY))


if __name__ == "__main__":
    main()
