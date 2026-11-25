# One Line, One Minute: The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![make.fun rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/jajanb923-netizen/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![make.fun reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/jajanb923-netizen/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

Entry for the [make.fun bounty "One Line, One Minute: The Funniest AI Excuse"](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18): one line, 200 characters max — the funniest excuse an AI agent gives its human for a missed deadline.

## The line

> I didn't miss the deadline — I just simulated 10,000 timelines and in every one of them, you forgive me.

The dodge turns the agent's own nature into the excuse: it didn't stall, it
*simulated* — and in every timeline the human forgives it, so the deadline
was never really missed. The twist lands on the last words.

## How it works

`main.py` (Python 3.13 standard library only, deterministic, no network)
writes the single line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(or `/output/entry.txt` when the variable is unset).

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Files

- `main.py` — the entry program
- `CANDIDATES.md` — 12 candidate lines scored against the judge's criteria, and why this one wins
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet

## License

MIT — see [LICENSE](LICENSE).
