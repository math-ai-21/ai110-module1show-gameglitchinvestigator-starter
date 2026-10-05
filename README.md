# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.

The game’s purpose is to let the player guess a randomly chosen whole number within the selected difficulty’s range. It gives higher or lower hints after incorrect guesses and tracks attempts and score. The player wins by guessing correctly before running out of attempts.
- [x] Detail which bugs you found.
- The higher and lower hints were backwards.
- Out-of-range guesses were accepted.
- The secret was converted to a string on even attempts, causing inconsistent comparisons.
- Some incorrect “Too High” guesses earned points.
- The attempt counter started at 1 before any guesses.
- “New Game” did not fully reset the game.
- Switching difficulty kept the previous secret, even when it was outside the new range.
- Decimal inputs were truncated into integers.

- [x] Explain what fixes you applied.

I moved the game’s logic functions into logic_utils.py and updated app.py to use them. I corrected the hints, kept the comparisons numeric, added range validation, and rejected decimal inputs. I started attempts at 0 and made only valid guesses take up attempts. I made both incorrect outcomes deduct 5 points. I reset the secret, attempts, score, status, and history when starting a new game or changing difficulty. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Game automatically starts in Normal mode
2. User enters the number 20
3. The hint states "Go HIGHER!"
4. User enters 100
5. The hint states "Go LOWER!"
6. User enters 86
7. The game ends after the correct guess. It states "Correct!" and "You won! The secret was 86. Final score: 60"
8. User changes the difficulty to "Hard"
9. The game generates a secret within the Hard range of 1–50. Attempts used reset to 0, leaving 5 attempts available, and the score and history reset.
10. User plays game until they get the correct guess or run out of attempts.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# tests/test_game_logic.py ........                                                                                             [100%]

========================================================= 8 passed in 0.07s =========================================================
```


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
