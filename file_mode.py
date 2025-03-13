import sys
from calculator import quadratic_calculator


def read_coefficients_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read().strip()

            coefficients = content.split()

            if len(coefficients) != 3:
                print("Invalid file format")
                sys.exit(1)

            a, b, c = map(float, coefficients)

            if a == 0:
                print("Coefficient 'a' cannot be 0.")
                sys.exit(1)

            return a, b, c

    except FileNotFoundError:
        print(f"File {file_path} does not exist")
        sys.exit(1)
    except ValueError:
        print("Invalid file format")
        sys.exit(1)


def file_mode(file_path):
    a, b, c = read_coefficients_from_file(file_path)

    roots = quadratic_calculator(a, b, c)

    if roots:
        for i, root in enumerate(roots):
            print(f"x{i + 1} = {root}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        file_mode(file_path)
    else:
        print("Usage: python equation.py <file_path>")
