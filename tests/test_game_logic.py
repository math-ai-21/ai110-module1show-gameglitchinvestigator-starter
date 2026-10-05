import pytest

from logic_utils import check_guess, update_score, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome,message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome,message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome,message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_on_even_attempt_does_not_add_points():
    # Attempt 2 is even; the old code returned 10 + 5 = 15
    assert update_score(10, "Too High", 2) == 5

def test_negative_guess_is_rejected():
    # A negative number is below the lowest valid guess, so it must not be accepted
    ok, value, err = parse_guess("-5", 1, 100)
    assert ok is False
    assert value is None
    assert "Out of range" in err

#New test cases generated to cover edge-cases, following Claude's suggestions.
def test_decimal_guess_is_rejected():
    # A decimal must be rejected, not truncated to an int
    ok, value, err = parse_guess("3.7", 1, 100)
    assert ok is False
    assert value is None
    assert "not a number" in err

def test_extremely_large_guess_is_rejected():
    # A huge integer is far above the highest valid guess
    ok, value, err = parse_guess("99999999999999999999", 1, 100)
    assert ok is False
    assert value is None
    assert "Out of range" in err

def test_non_numeric_guess_is_rejected():
    # Letters are not a number at all
    ok, value, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert value is None
    assert "not a number" in err


