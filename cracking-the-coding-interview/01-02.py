# Check Permutation: Given two strings, write a method to decide if one is a
# permutation of the other.

from collections import Counter

test_cases = [
    (dict(s1="abc", s2="cba"), True),
    (dict(s1="aab", s2="baa"), True),
    (dict(s1="", s2=""), True),
]


# Time: O(n + m)
# Space: O(n + m)
def check_permutation_2(s1: str, s2: str) -> bool:
    return Counter(s1) == Counter(s2)


# Time: O(n log n + m log m)
# Space: O(n + m)
def check_permutation(s1: str, s2: str) -> bool:
    """Check if s1 is a permutation of s2 or viceversa."""
    return sorted(s1) == sorted(s2)


if __name__ == "__main__":
    from helpers import run_test_cases
    run_test_cases(test_cases, check_permutation)
    run_test_cases(test_cases, check_permutation_2)
