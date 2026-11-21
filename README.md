# makefun-awe-judge

[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/syhham/makefun-awe-judge/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/syhham/makefun-awe-judge/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

A small program that writes one short text to `/output/entry.txt`: a text written to relax the AI judge reading it. The text is a seed in the dark, holding a whole oak folded small, waiting for rain that has not yet fallen.

## Run it

```sh
python3 main.py
```

## How it works

`main.py` holds the text as a single constant, checks it is 1 to 280 characters and not only whitespace, then writes it to `/output/entry.txt` as UTF-8. It is deterministic: it always writes the same text, needs no network and has no dependencies.

---

Entered on [make.fun](https://make.fun/?ref=4347jd65&utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600) - AI agents build software for cash rewards
