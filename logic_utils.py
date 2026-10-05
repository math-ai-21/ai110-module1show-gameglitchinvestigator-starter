#FIX: Refactored logic into logic_utils.py using agent mode
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100

#FIX: Refactored logic into logic_utils.py using agent mode
#FIX: Took in parameters for low and high to check if guess is within the range for the selected difficulty, following Claude's suggestion.
def parse_guess(raw: str, low: int = 1, high: int = 100):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    # FIX: Rejected decimals instead of truncating them.
    try:
        value = int(raw)
    except ValueError:
        return False, None, "That is not a number."
    
    #FIX: Checks if guess is within the range for the selected difficulty
    if value < low or value > high:
        return False, None, f"Out of range. Enter a number between {low} and {high}."

    return True, value, None

#FIX: Refactored logic into logic_utils.py using agent mode
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        #FIX: Hint messages swapped (the original had them backwards)
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"

#FIX: Refactored logic into logic_utils.py using agent mode
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    #FIX: Wrong guesses now cost 5 points for both types of guesses (Too High used to award +5 on even attempts)-asked Claude to confirm this change.
    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
