def is_eligible_to_vote(age, is_citezen):
    if age >= 18 and is_citezen:
        return True
    return False
