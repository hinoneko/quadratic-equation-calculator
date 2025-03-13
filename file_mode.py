from file_utils import read_coefficients_from_file
from calculator import quadratic_calculator


def file_mode():
    coefficients = read_coefficients_from_file()

    if coefficients:
        a, b, c = coefficients
        roots = quadratic_calculator(a, b, c)

        for i, root in enumerate(roots, start=1):
            print(f"x{i} = {root}")
