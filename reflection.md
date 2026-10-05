# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  When I first ran the game, I noticed that it was not working as intended. First, the hints were backwards: after it told me to go lower, I guessed the lowest possible number, 1, but it still told me to go lower. This suggested that the “Go LOWER!” and “Go HIGHER!” messages were switched. Also, after finishing one round, I noticed that clicking “New Game” displayed “Game over. Start a new game to try again.” but did not let me start a new game.
  
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  - the hints were switched
  - the "New Game" button wasn't working
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.
 
| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
| --- | --- | --- | --- | --- |
| 10 (secret > 10) | "Go HIGHER!" | "Go LOWER!" | none | app.py, check_guess() |
| -10 | It should inform the user that it is out of range. | Accepts -10 and says "Go LOWER!" | none | app.py, parse_guess() |
| 110 | It should inform the user that it is out of range. | Accepts 110 and alternates between "Go LOWER!" and "Go HIGHER!" on successive guesses. | none | app.py, check_guess(), parse_guess() |
| "twenty" | It should reject the input and not count it. | It uses an attempt. | "That is not a number." | app.py, if submit: |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  I used Claude for this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  One correct suggestion it gave was to remove the code that converted the secret number from an integer to a string on even-numbered attempts, so guesses would be compared numerically. I accepted this suggestion and verified it by rerunning the Streamlit app and checking that the guessing hints worked correctly. 

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

  One suggestion I did not accept was to hide the “Developer Debug Info” panel behind another control because it revealed the answer. I kept the existing expander because seeing the secret was useful while testing. I verified my version by comparing my guesses with the displayed secret and checking that the hints and win message matched.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  I decided a bug was fixed only after understanding the changes in the code and testing the Streamlit app. I tested the app before making changes and then after making changes to check whether the original issue was resolved. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  One test I ran using pytest checked the update_score function. Originally, an incorrect “Too High” guess earned points on even-numbered attempts, while a “Too Low” guess lost points. This seemed inconsistent, so after changing the code, I tested whether a “Too High” guess deducted 5 points as expected. The test passed, showing that the function behaved correctly for the case I tested.

- Did AI help you design or understand any tests? How?

  Yes, AI helped me design good tests. I gave it specific areas that we can check and it generated test cases based on those ideas.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  I would explain that Streamlit reruns the code from top to bottom when you interact with the app, like clicking “Submit Guess.” Session state remembers values like the secret number and score so they are not lost during each rerun. Those values stay until the code resets them, like when you start a new game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  One habit I want to reuse is reading all the instructions before starting and making sure I commit as I go through the project. 

- What is one thing you would do differently next time you work with AI on a coding task?

  Next time I work with AI, I would first think of my own possible solutions for the bugs I identified, then ask AI for suggestions and compare them with mine. This would help me understand what is going on without AI automatically making several changes at once.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

  This project showed me that AI-generated code can look correct but still behave incorrectly. I learned to understand suggested changes and test them using pytest and the Streamlit app before deciding that a problem is fixed.