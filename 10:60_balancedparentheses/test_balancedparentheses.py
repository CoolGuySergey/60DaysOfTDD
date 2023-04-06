from balancedparenthesis import parentheses_checker


def test_parentheses_checker():

    """test function parentheses_checker()"""

    assert not parentheses_checker("{})")
    assert not parentheses_checker("){}")
    assert not parentheses_checker("{})")

    assert not parentheses_checker("{{)(}}")
    assert not parentheses_checker("({)}")

    assert parentheses_checker("[({})]")
    assert parentheses_checker("{}([])")
    assert parentheses_checker("{()}[[{}]]")
