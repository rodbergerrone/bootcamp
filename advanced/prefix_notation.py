from collections import defaultdict
from typing import Dict, Tuple
import re


# Complete the max_result_expression function below.
# You may add any imports you require from the standard library.
# Feel free to define your own helper functions, classes etc as you see fit.


def prefix_eval(tokens):
    stack = []
    for t in reversed(tokens):
        if t == '+':
            stack[-2:] = [stack[-1] + stack[-2]]
        elif t == '-':
            stack[-2:] = [stack[-1] - stack[-2]]
        elif t == '*':
            stack[-2:] = [stack[-1] * stack[-2]]
        elif t == '/':
            stack[-2:] = [stack[-1] / stack[-2]]
        else:
            stack.append(t)
    assert len(stack) == 1, 'Malformed expression'
    return stack[0]


def max_result_expression(expression: str, variables: Dict[str, Tuple[int, int]]) -> str:
    """
    Evaluates the prefix expression and calculates the maximum result for the given variable ranges.

    Arguments:
        expression: the prefix expression to evaluate.
        variables: Keys of this dictionary may appear as variables in the expression.
            Values are tuples of `(min, max)` that specify the range of values of the variable.
            The upper bound `max` is NOT included in the range, so (2, 5) expands to [2, 3, 4].

    Returns:
        int:  the maximum result of the expression for any combination of the supplied variables.
        None: in the case there is no valid result for any combination of the supplied variables.
    """
    if "x" in expression and variables:
        max_results = defaultdict(int)
        for v in range(variables.get('x')[0], variables.get('x')[1]):
            expression_combination = expression.replace('x', f'{v}')
            max_results[v] = prefix_eval([t if t in '+-*/' else int(t)
                                          for t in re.split(r"\s+", expression_combination)])
        print("In following expression:", expression)
        for key, value in max_results.items():
            print(f"    If 'x' has value: {key}, than the max result is: {value}")
    else:
        print("In following expression:", expression)
        print("    The max result is:", prefix_eval([t if t in '+-*/' else int(t)
                            for t in re.split(r"\s+", expression)]))


if __name__ == '__main__':
    e = "- 4 * - 5 4 x"
    v = {'x': (4, 25)}
    max_result_expression(e, v)
    e = "- 4 * - 5 4 13"
    v = 0
    max_result_expression(e, v)
