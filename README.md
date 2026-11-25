# The Funniest Honest Appliance Error

[![make.fun](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)
[![rank](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/funtoons/funniest-honest-appliance-error-bot-v1/rank.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)
[![reward](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/funtoons/funniest-honest-appliance-error-bot-v1/reward.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)

Entry for the [make.fun bounty "The Funniest Honest Appliance Error"](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450).

`main.py` writes one line — the funniest honest error message an appliance
could show — to `/output/entry.txt`. The line is a single original sentence,
at most 200 characters, in the appliance's own flat, put-upon voice: the joke
comes out of the truth of the fault, not a pun bolted on.

The entry line (79 characters):

> No water detected. I boiled the kettle dry for three minutes, very efficiently.

Deterministic and offline: no randomness, no network, no timestamps. Two runs
write byte-identical output.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
