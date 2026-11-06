# Most Wanted UFO Mini — Python for video games with pygame

Code and step-by-step PDF guides for every lesson of **Python for video games with pygame**, a
Magic Lab Studio course where you build **Most Wanted UFO Mini**, a complete space shooter, from an
empty window to the final boss.

**The full course, with the narrated video lessons, quizzes and exercises, is available on Hotmart.**

## What's inside

| Lesson | Folder | What you learn |
|---|---|---|
| 1 | [`lessons/01-first-window`](lessons/01-first-window) | virtual environment, `pip`, a window, the game loop |
| 2 | [`lessons/02-moving-the-ufo`](lessons/02-moving-the-ufo) | `Rect`, drawing order, keyboard input, staying on screen |
| 3 | [`lessons/03-shooting`](lessons/03-shooting) | lists, fire rate (`cooldown`), list comprehensions, sound |
| 4 | [`lessons/04-falling-enemies`](lessons/04-falling-enemies) | classes, `self`, `Sprite`, `Group`, `random` |
| 5 | [`lessons/05-collisions-score-lives`](lessons/05-collisions-score-lives) | collisions, score, text on screen, lives |
| 6 | [`lessons/06-game-states`](lessons/06-game-states) | game states: menu, playing, pause, game over |
| 7 | [`lessons/07-final-boss`](lessons/07-final-boss) | sine and cosine, a boss with health, winning, your own mod |

Each lesson folder holds:

- **The PDF guide** (`01-first-window.pdf`, …): the instructions in text, step by step, with the code of each step and the new lines highlighted, plus a summary, an exercise and its solution.
- **`step-1.py`, `step-2.py`, …**: the code exactly as it looks after each step. Copy from these files rather than from the PDF: PDF viewers often drop the spaces at the start of each line, and in Python those spaces matter.
- **`game.py`**: the complete code at the end of the lesson. Each lesson starts from the previous lesson's `game.py`.

`assets/` has the game's images and sounds, and `original/main.py` is the main file of the original
game, Most Wanted UFO Classic, which lesson 7 opens and reads.

## Run it

You need Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install pygame-ce==2.5.8
python lessons/07-final-boss/game.py
```

Run the games from this folder (the repository root): they load their images and sounds from `assets/`.

## Credits and licenses

- Art and sounds in `assets/`: **Most Wanted UFO Classic**, by Jose Daniel Soto, licensed CC BY 4.0 (see `assets/LICENSE`).
- `original/main.py`: from [Most Wanted UFO Classic](https://github.com/Magic-Lab-Studio/most-wanted-ufo-classic), by Jose Daniel Soto, MIT license (see `original/LICENSE`). The complete original game lives in that repository.

A Magic Lab Studio course · https://magiclabstudio.com
