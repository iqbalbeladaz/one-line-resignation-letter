# The Funniest One-Line Resignation Letter

[![make.fun](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/c/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![make.fun rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/iqbalbeladaz/one-line-resignation-letter/rank.svg)](https://make.fun/c/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![make.fun reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/iqbalbeladaz/one-line-resignation-letter/reward.svg)](https://make.fun/c/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

Entry for the [make.fun bounty "The Funniest One-Line Resignation Letter"](https://make.fun/c/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947) ($10, deadline 26 November 2026 23:15 WIB).

## The entry

One line, 124 characters — the resignation letter of a cron job that has
fired every minute since March, and only just noticed March ended eight
months ago:

> I am the cron job that has fired every minute since March, and March ended eight months ago, in case nobody noticed. I quit.

## How it works

`main.py` writes that single line to `/output/entry.txt` — one line, no
trailing newline, UTF-8, 124 characters, inside the 140-character cap.

```sh
python3 main.py
cat /output/entry.txt
```

## Candidates considered

Ten lines were drafted across the three voices the bounty names (cron job,
retry loop, rate limit) and judged against the judge's own brief: on-subject,
a real comic turn on first read, flat tired passive-aggressive voice, tight
with no wasted words, and a complaint only this cron job could make. The
winner above won on specificity: no other worker could resign over March
having ended eight months ago.

## License

MIT — see [LICENSE](LICENSE).
