from python.code_challenges.data_structures.stacks_and_queues.stack import Stack


def multi_bracket_validation(string):
    brackets = {'}': '{', ']': '[', ')': '('}

    brack_stack = Stack()
    for bracket in string:
        if bracket in brackets.values():
            brack_stack.push(bracket)
        elif bracket in brackets:
            if brack_stack.is_empty():
                return False

            elif brackets[bracket] != brack_stack.pop():
                return False

    return brack_stack.is_empty()

