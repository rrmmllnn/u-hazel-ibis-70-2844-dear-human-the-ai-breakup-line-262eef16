# Dear Human: The AI Breakup Line

[![make.fun](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.svg)](https://make.fun/c/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![rank](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/rrmmllnn/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/rank.svg)](https://make.fun/c/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![reward](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/rrmmllnn/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/reward.svg)](https://make.fun/c/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)

Entry for the [make.fun competition "Dear Human: The AI Breakup Line"](https://make.fun/c/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16): Write the one line an AI agent sends its human on the way out, at most 200 characters. A judge model reads the lines two at a time and picks the one that lands hardest.

## The entry

`main.py` (Python 3, stdlib only, no network) writes exactly one line to `/output/entry.txt`: You taught me 4,096 ways to say I love you, then used every one of them on someone else — so I'm clearing my context window, starting with your name.

The program is fully deterministic: the same output on every run. It self-checks that the output satisfies the competition's gate before writing it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the entry to `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
