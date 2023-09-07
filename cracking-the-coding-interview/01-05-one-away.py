# One Away: There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character. Given two
# strings, write a function to check if they are one edit (or zero edits) away.

test_cases = [
    (dict(s1="pale", s2="ple"), True),
    (dict(s1="pales", s2="pale"), True),
    (dict(s1="pale", s2="bale"), True),
    (dict(s1="pale", s2="bake"), False),
]


# Time: O(n)
# Space: O(n) -- Can be improved to O(1) easily
def one_away(s1: str, s2: str) -> bool:
    """Determines if s1 and s2 are one or zero edits away."""

    len_diff = abs(len(s1) - len(s2))

    if len_diff > 1:
        return False

    if len_diff == 0:
        differences = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                differences += 1
            if differences > 1:
                return False
        return True

    # The longer string might have had an insertion.
    # We check if all characters are the same except for one.
    short, long = sorted([s1, s2], key=len)
    offset = 0
    for i in range(len(short)):
        if short[i + offset] != s2[i]:
            offset += 1
        if abs(offset) > 1:  # Means more than one character doesn't match
            return False
    return True


if __name__ == "__main__":
    from helpers import run_test_cases

    run_test_cases(test_cases, one_away)
