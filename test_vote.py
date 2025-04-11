from vote import is_eligible_to_vote


def test_eligible_voter():
    assert is_eligible_to_vote(20, True) is True
    assert is_eligible_to_vote(18, True) is True


def test_underage_voter():
    assert is_eligible_to_vote(17, True) is False


def test_non_citizen():
    assert is_eligible_to_vote(25, False) is False


def test_underage_and_non_citizen():
    assert is_eligible_to_vote(16, False) is False

      
