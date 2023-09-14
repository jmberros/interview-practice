# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

test_cases = [
    ("abc", True),
    ("aca", False),
    ("", True),
]

# 💡
# aprovechar que está sorted:
# atravesas letra por letra y si es igual a la anterior tiene dupes!


# Notes: without other data structure, although sorted(s) iplicitly uses a list
# Time: O(n log n)
# Space: O(n)
def is_unique(s: str) -> bool:
    """Determines if a string has all unique characters."""
    previous_char = None
    for char in sorted(s):
        if char == previous_char:
            return False
        previous_char = char
    return True


# Notes: using a different data structure (set)
# Time: O(n), conversion from list to set
# Space: O(n)
def is_unique_2(s: str) -> bool:
    return len(set(s)) == len(s)


if __name__ == "__main__":
    from helpers import run_test_cases
    run_test_cases(test_cases, is_unique)
    run_test_cases(test_cases, is_unique_2)
