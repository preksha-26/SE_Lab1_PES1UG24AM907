# Lab 4: Memory Color Pattern Repair Lab

**Name:** K Preksha
**SRN:** PES1UG24AM907

A Simon-style pattern recall game built with **Pygame**. The game uses a finite state machine (`WATCH`, `PLAYER_TURN`, `GAME_OVER`), time-based sequence playback and index-matching input validation. This submission fixes the deliberate bug in the starter code and implements all three optional features.

---

## Submission Links

| Item | Link |
|------|------|
| Chat / LLM history | *(paste shared chat link here)* |

---

## Tasks Completed

### Task 1: Sequence duplication bug (fixed)
**Problem:** Advancing to the next round made the pattern grow far more than one step.

**Fix:** `_start_round()` in `game_engine.py` now appends exactly **one** random color to the sequence each round. It never copies or extends the existing list.

### Task 2: Dynamic playback acceleration
Flash and pause durations shrink as the round number increases, down to a minimum so the game stays playable.

| | Round 1 | Reduction per round | Minimum |
|---|---------|--------------------|---------|
| Flash duration | 600 ms | 40 ms | 150 ms |
| Pause between flashes | 300 ms | 20 ms | 80 ms |

### Task 3: Sound effects
Each pad has its own pitch, generated as a sine wave in code (no audio files or numpy needed). The tone plays when a pad flashes during playback and when the player clicks it.

| Pad | Note | Frequency |
|-----|------|-----------|
| Red | C4 | 261.63 Hz |
| Blue | E4 | 329.63 Hz |
| Green | G4 | 392.00 Hz |
| Yellow | C5 | 523.25 Hz |

A low buzz plays on Game Over. If no audio device is found, the game runs silently without crashing.

### Task 4: Player turn timer
A countdown bar below the grid starts when playback ends. The time allowed grows with the pattern length:

`time limit = 3000 ms + 1000 ms × (number of steps)`

The bar shrinks as time passes and changes color (green, then yellow, then red). If time runs out before the pattern is completed, the Game Over screen appears.

---

## How to Run

```bash
pip install pygame
python main.py
```

Requires Python 3.10+. Run the command from inside this folder.

**Controls:** Left-click the colored pads to repeat the sequence. Press **R** to restart after Game Over.

---

## Folder Structure

```
Lab4_Memory_Color_Pattern/
├── game/
│   ├── __init__.py
│   ├── color_button.py    # pad drawing, lit/dim state, pitch
│   └── game_engine.py     # state machine, playback, input, timer, audio
├── main.py                # window setup and main loop
└── README.md
```

---

## Expected Behavior (verified)

- Each round replays the full sequence step by step with lit pads.
- Each round adds exactly one new step.
- Clicking a pad lights it briefly, plays its tone and registers the guess.
- A wrong pad immediately triggers Game Over.
- Running out of time triggers Game Over.
- Pressing R on the Game Over screen resets to round 1 with score 0.

---

## Tunable Constants

At the top of `game/game_engine.py`:

`FLASH_START`, `FLASH_MIN`, `FLASH_STEP`, `PAUSE_START`, `PAUSE_MIN`, `PAUSE_STEP`, `TURN_BASE_MS`, `TURN_PER_STEP_MS`

---

## LLM Usage and Review

I used Claude as a pair-programming partner to analyze the bug, implement the features and test them. I reviewed the generated code and checked each task against the expected behavior above. The full conversation is linked in the Submission Links table.
