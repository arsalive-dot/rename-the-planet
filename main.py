"""Rename the Planet — make.fun entry.

Writes one funny one-liner to /output/entry.txt: a new name for Neptune
plus the why, in a single line under 200 characters.

The joke: Neptune has the fastest winds in the solar system (about
2,100 km/h), so it earns the name "The Leaf Blower" — the only planet
that could clear your driveway from orbit.
"""

import os
import stat
import tempfile

ENTRY = (
    "Rename Neptune 'The Leaf Blower' \u2014 its 2,100 km/h winds are the "
    "fastest in the solar system, so it could clear your driveway from orbit."
)


def main() -> None:
    # Gate self-check (mirrors the sealed scorer): 1-200 chars, one line,
    # not only white space. Fail loudly instead of writing an invalid entry.
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only white space"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(ENTRY)
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, target)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
