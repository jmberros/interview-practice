from linked_list_jm import LinkedList, LinkedListNode
from termcolor import colored, cprint


class TestsFailedException(Exception):
    pass


def run_test_cases(cases, f):
    cprint(f"{f.__name__}", "cyan")
    for inputs, expected_outputs in cases:
        print(f"Inputs: {colored(repr(inputs), 'magenta')}")
        print(f"Exp: {repr(expected_outputs)}")
        if isinstance(inputs, dict):
            outputs = f(**inputs)
        else:
            outputs = f(inputs)
        test_passed = outputs == expected_outputs
        print("Got:", end=" ")
        cprint(repr(outputs), "green" if test_passed else "red")
        print("---")


def run_test_cases_ll(cases, f):
    cprint(f"{f.__name__}", "cyan")

    for inputs, expected_output in cases:
        expected_output_ll = LinkedList(expected_output)
        expected_output_node = expected_output_ll.head
        input_ll = LinkedList(inputs)
        input_node = input_ll.head

        print(f"Inputs: {colored(repr(input_ll), 'magenta')}")
        print(f"Exp: {repr(expected_output_ll)}")

        output = f(input_node)
        if isinstance(output, LinkedListNode):
            output = LinkedList.init_from_head(output)
            test_passed = output == expected_output_ll
        else:
            test_passed = output == expected_output_node.value

        print("Got:", end=" ")
        cprint(repr(output), "green" if test_passed else "red")
        print("---")
