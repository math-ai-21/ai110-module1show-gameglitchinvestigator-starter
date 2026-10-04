# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
When I first ran the game, I noticed that it was not working as intended. First, the hints were backwards: after it told me to go lower, I guessed the lowest possible number, 1, but it still told me to go lower. This suggested that the “Go LOWER!” and “Go HIGHER!” messages were switched. Also, after finishing one round, I noticed that clicking “New Game” displayed “Game over. Start a new game to try again.” but did not let me start a new game.
So the two main bugs are:
-the hints were switched
-the "New Game" button wasn't working
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input        | Expected Behavior | Actual Behavior    | Console Output / Error | Suspected Code Location |
|--------------|-------------------|--------------------|------------------------|-------------------------|
|   10         | "Go HIGHER!"      |"Go LOWER!"         |    none                | app.py, check_guess()   |
|(secret > 10) |                   |                    |                        |                         |
|   -10        | It should inform  |Accepts -10 and says|    none                | app.py, parse_guess()   |
|              | the user that it  |"Go LOWER!"         |                        |                         |
|              | is out of range.  |                    |                        |                         |
|              |                   |                    |                        |                         |
|   110        |It should inform   |Accepts 110 and     |    none                | app.py, check_guess,    |
|              |the user that it   |alternates between  |                        | parse_guess()           |
|              |is out of range.   |"Go LOWER!" and     |                        |                         |
|              |                   |"Go HIGHER!" on     |                        |                         |
|              |                   |successive guesses. |                        |                         |
|  "twenty"    | It should reject  |It uses an attempt. | "That is not a number."| app.py, if submit:      |     
|              | the input and not |                    |                        |                         |
|              | count it.         |                    |                        |                         |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
