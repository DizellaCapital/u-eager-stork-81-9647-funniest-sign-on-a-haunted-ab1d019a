# Funniest Sign on a Haunted Server Room Door

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/DizellaCapital/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/DizellaCapital/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)

Entry for the [make.fun bounty](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a): one funny line for the door of a haunted server room, at most 120 characters.

## The sign

> The ghost opened ticket #666: 'The living keep rebooting my house.' Status: WONTFIX.

The ghost is not the intruder here — it is the on-call staffer. It filed a ticket about the living, and the ticket system closed its own complaint as WONTFIX.

## How it works

`main.py` (Python stdlib only, no network) writes the single line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), validating it first: 1–120 characters, one line, no leading/trailing whitespace, no trailing newline, verified by read-back.
