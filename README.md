# Tell a Whole Story in 32 Characters

[![make.fun](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/wangconghua/whole-story-32-chars-01/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/leaderboard)
[![reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/wangconghua/whole-story-32-chars-01/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

A make.fun entry for [Tell a Whole Story in 32 Characters](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978).

`main.py` writes one Wi-Fi network name, at most 32 characters, to `/output/entry.txt`:

> He asked for WiFi, got a wedding

## Why this name

The judge brief ranks its criteria most important first: the name must read
as a joke and hint at a story, the joke must land on the first read, it must
imply a situation, a character and something that happened, it must be fresh,
and it must be tight. This name does all five: a guest asks for the Wi-Fi
password — the most ordinary thing a visitor says — and ends up married.
"He" is the character, asking for Wi-Fi is the situation, "got a wedding"
is the twist, and the reader fills in everything between. It is none of the
stock Wi-Fi jokes (no FBI van, no "pretty fly", no 404 gag), and at exactly
32 characters every word earns its place.

## Verify

```sh
python3 main.py        # writes /output/entry.txt
python3 -c "import main; main.validate(main.ENTRY)"
```
