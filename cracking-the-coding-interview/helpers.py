from termcolor import colored, cprint


class TestsFailedException(Exception):
    pass


def run_test_cases(cases, f):
    cprint(f"{f.__name__}", "cyan")
    for inputs, expected_outputs in cases:
        print(f"Inputs: {colored(repr(inputs), 'magenta')}")
        print(f"Exp: {expected_outputs}")
        if isinstance(inputs, dict):
            outputs = f(**inputs)
        else:
            outputs = f(inputs)
        test_passed = outputs == expected_outputs
        print("Got:", end=" ")
        cprint(outputs, "green" if test_passed else "red")
        print("---")
