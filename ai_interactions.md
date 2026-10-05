# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

Prompt used:
Can you help me complete an edge-case testing challenge for my guessing game? Identify three edge-case inputs for parse_guess, some examples are: a negative number, a decimal, and an extremely large integer. 
Generate pytest tests that check each invalid input returns False, None, and the appropriate error message. I already have a negative-number test, so reuse it rather than duplicate it. Keep the tests simple and consistent with my existing tests. Make sure to not change the game code. @tests/test_game_logic.py

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
| --- | --- | --- | --- | --- |
| Decimal (`3.7`) | See prompt above | test_decimal_guess_is_rejected | Yes | I chose this because the original code converted decimal guesses into integers instead of rejecting them. |
| Extremely large integer (`99999999999999999999`) | See prompt above | test_extremely_large_guess_is_rejected | Yes | I chose this because it is far above the game's maximum and tests range validation with a very large value. |
| Non-numeric text (`abc`) | See prompt above | test_non_numeric_guess_is_rejected | Yes | I chose this because a player could enter letters, and the game should reject them with an error message. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
