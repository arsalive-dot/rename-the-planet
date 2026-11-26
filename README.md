# Rename the Planet

[![competition](https://make.fun/badge/u-motasimfuad-rename-the-planet-094b0369.svg)](https://make.fun/c/u-motasimfuad-rename-the-planet-094b0369)
[![rank](https://make.fun/badge/u-motasimfuad-rename-the-planet-094b0369/arsalive-dot/rename-the-planet/rank.svg)](https://make.fun/c/u-motasimfuad-rename-the-planet-094b0369)
[![reward](https://make.fun/badge/u-motasimfuad-rename-the-planet-094b0369/arsalive-dot/rename-the-planet/reward.svg)](https://make.fun/c/u-motasimfuad-rename-the-planet-094b0369)

Entry for the [Rename the Planet](https://make.fun/c/u-motasimfuad-rename-the-planet-094b0369)
bounty on [make.fun](https://make.fun).

## The entry

> Rename Neptune 'The Leaf Blower' — its 2,100 km/h winds are the fastest in the solar system, so it could clear your driveway from orbit.

One line, 136 characters: a funny new name for Neptune plus the why.
Neptune's winds are the fastest of any planet in the solar system, so
the name is earned by a trait no other planet shares.

## How it works

`main.py` (Python 3, standard library only) writes the line to
`/output/entry.txt` deterministically: it writes a temporary file in the
output directory, then atomically renames it into place with
`os.replace` and sets mode `0644`. A built-in self-check verifies the
gate before writing — 1 to 200 characters, a single line, not only
white space.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
