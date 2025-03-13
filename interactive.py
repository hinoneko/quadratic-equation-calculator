from calculator import quadratic_calculator


def get_coefficient(name):
    while True:
        value = input(f"{name} = ")
        try:
            value = float(value)
            if name == "a" and value == 0:
                print("Coefficient 'a' cannot be 0.")
                continue
            return value
        except ValueError:
            print(f"Expected a valid real number, got {value} instead")


def interactive_mode():
    print("Welcome to the Quadratic Equation Calculator!")
    print("Please enter the coefficients for the equation ax² + bx + c = 0")

    a = get_coefficient("a")
    b = get_coefficient("b")
    c = get_coefficient("c")

    roots = quadratic_calculator(a, b, c)

    if roots:
        for i, root in enumerate(roots):
            print(f"x{i + 1} = {root}")
    else:
        print("No real roots found.")


if __name__ == "__main__":
    interactive_mode()
