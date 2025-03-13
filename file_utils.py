import sys


def read_coefficients_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read().strip()

            coefficients = content.split()

            if len(coefficients) != 3:
                raise ValueError("Invalid file format")

            a, b, c = map(float, coefficients)

            if a == 0:
                raise ValueError("Coefficient 'a' cannot be 0.")

            return a, b, c

    except FileNotFoundError:
        print(f"File '{file_path}' does not exist.")
        sys.exit(1)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
