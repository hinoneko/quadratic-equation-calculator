from file_utils import read_coefficients_from_file
from calculator import quadratic_calculator


def file_mode():
    file_path = input("Enter the path to the file with coefficients: ")
    coefficients = read_coefficients_from_file(file_path)

    if coefficients:
        a, b, c = coefficients
        roots = quadratic_calculator(a, b, c)

        for i, root in enumerate(roots, start=1):
                print(f"x{i} = {root}")
