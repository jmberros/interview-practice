# String Compression: Implement a method to perform basic string compression
# using the counts of repeated characters. For example, the string aabcccccaaa
# would become a2blc5a3, If the "compressed" string would not become smaller
# than the original string, your method should return the original string. You
# can assume the string has only uppercase and lowercase letters (a - z).


test_cases = [
    ("aabcccccaaa", "a2b1c5a3"),
    ("aabbcc", "aabbcc"),
    ("aaa", "a3"),
    ("", ""),
]


def compress(s: str) -> str:
    """Compresses the string."""
    new_s_chars = []

    prev_char = None
    count = 0

    for i in range(len(s) + 1):
        char = s[i] if i < len(s) else None

        if char == prev_char or i == 0:
            count += 1
        else:
            new_s_chars.append(f"{prev_char}{count}")
            count = 1  # Resets the count starting here

        prev_char = char

    new_s = "".join(new_s_chars)
    return new_s if len(new_s) < len(s) else s


if __name__ == "__main__":
    from helpers import run_test_cases

    run_test_cases(test_cases, compress)
