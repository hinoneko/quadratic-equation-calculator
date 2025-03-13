from input_utils import get_coefficient
from calculator import quadratic_calculator


def interactive_mode():
    a = get_coefficient("a")
    b = get_coefficient("b")
    c = get_coefficient("c")

    roots = quadratic_calculator(a, b, c)

    for i, root in enumerate(roots, start=1):
        print(f"x{i} = {root}")
