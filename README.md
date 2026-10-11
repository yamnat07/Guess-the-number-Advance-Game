# Guess the Number (Upgraded)

A command-line number guessing game written in Python. The computer picks a secret number, and you try to guess it using "Too High" / "Too Low" hints. This is an upgraded version of my earlier Guess the Number game, with selectable difficulty levels, input validation, and a save-score feature.

## What's New in This Version

- **Difficulty selection:** choose from four levels, each with its own number range.
- **Save your score:** after each round you can save your result to a file, with your name, the date and time, your attempts and the difficulty.
- **Play again with a new difficulty:** every new round lets you pick a difficulty again.
- **Input validation:** letters, empty input, and out-of-range numbers are handled with a message instead of crashing the game.
- **Welcome screen:** a short introduction before the first difficulty menu.

## Comparison With the Previous Version

| | Previous version | Upgraded version |
|---|---|---|
| Number range | Fixed, 1 to 100 | Four difficulty levels: 1-50, 1-100, 1-500, 1-1000 |
| Welcome screen | None | Short introduction before the first menu |
| Out-of-range message | Always says "1 to 100" | Shows the range of the chosen difficulty |
| Saving scores | Not available | Saves name, date, time, attempts and difficulty to `scores.txt` |
| Play again | New secret number, same range | New secret number, and you pick the difficulty again |
| Attempts counter | Local to `guess_it()` | Shared (global) so `save()` can read it, and reset after every round |
| Functions | `guess_it()`, `main()` | `difficulty()`, `guess_it()`, `save()`, `main()` |
| Libraries | `random` | `random`, `datetime` |
| Size | About 48 lines | About 134 lines |

**What stayed the same:** the core guessing loop, the "Too High" / "Too Low" hints, the results screen with total attempts, the play again / exit menu, and the rule that only valid guesses count as attempts.

### Concepts Used in the Upgrade

- Returning a value from a function and storing it (`con_num = difficulty()`)
- Passing the chosen range into `guess_it()` and `save()` as arguments
- Reading the current date and time with `datetime` and formatting it with `strftime()`
- Writing to a text file in append mode, so old scores are never erased
- Safer menus that compare the typed text instead of converting it to a number, so letters can't crash them

## Difficulty Levels

| Choice | Level | Number range |
|---|---|---|
| 1 | Easy | 1 to 50 |
| 2 | Normal | 1 to 100 |
| 3 | Hardcore | 1 to 500 |
| 4 | Professional | 1 to 1000 |

## How to Play

1. Run the game and read the welcome screen.
2. Choose a difficulty (1-4).
3. Type your guesses. The game tells you whether each guess is too high or too low.
4. When you guess the number, the game shows the correct number and how many attempts you took.
5. Choose whether to save your score, then whether to play again or exit.

Only valid guesses count as attempts. Guesses that are not numbers, or are outside the range, are rejected and not counted.

## Requirements

- Python 3.6 or newer
- No extra packages needed. The game uses only the standard library (`random` and `datetime`).

## How to Run

```bash
python guess-the-number-adv.py
```

On some systems you may need to use `python3` instead of `python`.

## Example Session

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
WELCOME TO GUESS THE NUMBER
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Do you have enough guts to guess my secret number?
If YES! Then Good Luck

====================
Choose Difficulty
====================
1.Easy(Numbers From 1 to 50)
2.Normal(Numbers From 1 to 100)
3.Hardcore(Numbers From 1 to 500)
4.Professional(Numbers From 1 to 1000)

Enter your choice in [1,2,3,4] only!
Enter the difficulty:2
You have chosen Normal Difficulty!
====================
GUESS THE NUMBER
====================
I have chosen a number, can you guess it?
Enter your Guess: 50
Too Low! Try a higher number.
Enter your Guess: 75
Too High! Try a smaller number.
Enter your Guess: 62
Congratulations!!! You Guessed the right number.
Correct number:62
===RESULTS===
Total Attempts:3
~~~~~~~~~~~~~~~~~~~~
===SAVING===
~~~~~~~~~~~~~~~~~~~~
1.Save Your Score.
2.Don`t Save.
Enter your choice:1
Enter Player name: Alex
Saving Complete.
1.Play again/Beat your score.
2.Exit.
Enter your choice: 2
Thanks For Playing!Hope you beat your score next time.
```

## Saved Scores

If you choose to save, your result is added to a file called `scores.txt` in the folder where you run the game. The file is created automatically the first time you save, and new scores are added to the end without erasing old ones. Each entry looks like this:

```
Date:11-10-2026
Time:09:21:45 PM
Player Name:Alex
Attempts:3
Difficulty:Normal
```

The date is in `DD-MM-YYYY` format, and the time is in 12-hour format with AM/PM.

## Project Structure

```
guess-the-number-adv.py   # the whole game
scores.txt                # created automatically when you save a score
README.md
```

## Notes

- The game works through three main functions: `difficulty()` (the menu), `guess_it()` (the guessing loop) and `save()` (saving the score).
- Delete `scores.txt` if you want to start with a fresh score list.
