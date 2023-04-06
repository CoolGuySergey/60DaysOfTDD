"""

Write a program to determine if the parentheses (), the brackets [], and
the braces {}, in a string are balanced.

For example:

{{)(}} is not balanced because ) comes before (

({)} is not balanced because ) is not balanced between {} and similarly
the { is not balanced between ()

[({})] is balanced

{}([]) is balanced

{()}[[{}]] is balanced

"""


def parentheses_checker(string):

    """Check if parentheses are balanced"""

    open_close_dict = {
        2: ["()", "[]", "{}"],
        1: ["(", "[", "{"],
        0: [")", "]", "}"],
    }

    opener_tally = [string.count(opener) for opener in  open_close_dict[1]]
    closer_tally = [string.count(closer) for closer in  open_close_dict[0]]

    if len(string) % 2 == 0 and opener_tally == closer_tally and string[0] in open_close_dict[1]:

        while "()" in string or "[]" in string or "{}" in string:

            for pair in open_close_dict[2]:
                string = string.replace(pair, "")

        if not string:
            return True

    return False
