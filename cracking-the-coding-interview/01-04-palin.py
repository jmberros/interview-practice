# Palindrome Permutation: Given a string, write a function to check if it is a
# permutation of a palindrome. A palindrome is a word or phrase that is the
# same forwards and backwards. A permutation is a rearrangement of letters. The
# palindrome does not need to be limited to just dictionary words.
from collections import Counter

test_cases = [
    ("Tact Coa", True),
    ("abcde", False),
]


# Time: O(n)
# Space: O(n)
def is_palindrome_permutation(s: str) -> bool:
    """Checks if s is a permutation of a palindrome."""
    # Observation: to be a palindrome, the string needs to have an even number
    # of letters for all letters except maybe for one (the one in the middle).
    seen_odd_count = False
    s = s.replace(" ", "").casefold()
    # ^ NOTE: Spaces can be ignored to consider something a palindrome
    for letter, count in Counter(s).items():
        print(letter, count)
        if count % 2 != 0:
            if seen_odd_count:
                return False
            seen_odd_count = True

    return True


if __name__ == "__main__":
    from helpers import run_test_cases

    run_test_cases(test_cases, is_palindrome_permutation)
