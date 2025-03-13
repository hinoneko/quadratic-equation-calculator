from input_utils import get_coefficient
from calculator import quadratic_calculator


def interactive_mode():
    print("Welcome to the Quadratic Equation Calculator!")
    print("Please enter the coefficients for the equation ax² + bx + c = 0")

    a = get_coefficient("a")
    b = get_coefficient("b")
    c = get_coefficient("c")

    roots = quadratic_calculator(a, b, c)

    if roots:
        print(f"Equation: ({a})x² + ({b})x + ({c}) = 0")
        print(f"There are {len(roots)} root(s).")
        for i, root in enumerate(roots, start=1):
            print(f"x{i} = {root}")
    else:
        print("No real roots found.")
