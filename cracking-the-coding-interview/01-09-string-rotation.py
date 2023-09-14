# String Rotation; Assume you have a method isSubstring which checks if one word
# is a substring of another. Given two strings, s1 and s2, write code to check
# if s2 is a rotation of s1 using only one call to isSubstring [e.g.,
# "waterbottle" is a rotation of 'erbottlewat")

# 💡
# Truquito bellísimo: hacés s1 + s1 y ahí adentro están todas las "rotaciones".
# Ojo que acá rotation significa una palabra de igual longitud pero que comienza
# en el medio, pegando la vuelta.


test_cases = [
    (dict(s1="waterbottle", s2="erbottlewat"), True),
    (dict(s1="foobarbaz", s2="foo"), False)
]


def is_substring(s1: str, s2: str):
    """Checks if s1 is a substring of s2."""
    return s1 in s2


def is_rotation(s1: str, s2: str) -> bool:
    """Checks if s2 is a rotation of s1."""
    return len(s1) == len(s2) and is_substring(s2, s1 + s1)


if __name__ == "__main__":
    from helpers import run_test_cases

    run_test_cases(test_cases, is_rotation)
