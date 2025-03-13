from file_utils import read_coefficients_from_file
from calculator import quadratic_calculator


def file_mode(file_path):
    a, b, c = read_coefficients_from_file(file_path)

    roots = quadratic_calculator(a, b, c)

    print(f"Equation: ({a})x² + ({b})x + ({c}) = 0")
    if roots:
        print(f"There are {len(roots)} root(s).")
        for i, root in enumerate(roots, start=1):
            print(f"x{i} = {root}")
    else:
        print("No real roots found.")
