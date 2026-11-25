# news-image-20261124 — World on Edge

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/viansofyan/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/viansofyan/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A one-page newspaper front page summing up the world news of
**Tuesday, 24 November 2026**, headlined **WORLD ON EDGE**. Naval
silhouettes cross a globe beneath an orbital arc, in ink navy
`#142235` on newsprint ivory `#F4EBDD`, with signal red `#B72C32`
for the war rows. Six stories, in order of consequence:

1. **Iran — blockade confrontation.** Iran vowed to use every tool
   against the US naval blockade, which it calls military aggression,
   as Vice President JD Vance and Secretary of State Marco Rubio met
   Qatar's prime minister at the White House and UK logs recorded
   Iranian attacks in the Strait of Hormuz.
2. **NATO — space defence.** Alliance chief Mark Rutte said NATO will
   defend every inch of its territory, including in space, after
   reports that Russia is preparing to launch a nuclear-armed
   satellite, "Sputnik-S", within 60 days.
3. **Ukraine — Zaporizhzhia and 700,000 dead.** An overnight Russian
   strike on Zaporizhzhia killed two and wounded 40, including four
   children. A new Meduza/Mediazona analysis puts Russian soldiers
   killed in the nearly five-year war past 700,000.
4. **Gaza — Hamas security chief killed.** Israeli airstrikes killed
   Naeem Abu Nahel, director of Hamas' internal security apparatus,
   and six others in Gaza City.
5. **Libya — Benghazi probe.** The UN mission in Libya called for an
   independent investigation into attacks at Benghazi port, where a
   Russian warship was hit in suspected sea-drone strikes and sank.
6. **Nvidia — the CEO is back.** Jensen Huang was reinstated as chief
   executive less than two weeks after resigning, after President
   Trump said he "made the deal" with the board. The same day, the US
   Commerce Department blacklisted Singaporean cloud firm Megaspeed
   over alleged chip smuggling to China.

Sources: Just Security, The Global Eye, Meduza/Mediazona, UKMTO, AP.

## How it runs

`main.py` (Python 3.13, standard library only) copies
`assets/entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default
`/output/entry.png`). No network, no randomness — every run writes
identical bytes. Verify determinism with:

```sh
rm -rf /tmp/out1 /tmp/out2
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png
```

## License

MIT — see `LICENSE`.
