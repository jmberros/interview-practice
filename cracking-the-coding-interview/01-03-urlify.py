# URLify: Write a method to replace all spaces in a string with '%20'. You may
# assume that the string has sufficient space at the end to hold the additional
# characters, and that you are given the "true" length of the string.

# 💡
# Medio pavote, vas juntando los nuevos caracteres en un array y ponés %20
# si es un espacio. Preguntá si quieren que los espacios "colapsen" entre sí.

test_cases = [
    ("ab c d", "ab%20c%20d"),
    (" ", "%20"),
    ("abc", "abc"),
]


# Time: O(1)
# Space: O(n)
def urlify(s: str) -> str:
    """Replace all spaces with %20."""
    new_chars = []
    for char in s:
        if char == " ":
            new_chars.append("%20")
        else:
            new_chars.append(char)
    return "".join(new_chars)


if __name__ == "__main__":
    from helpers import run_test_cases

    run_test_cases(test_cases, urlify)
