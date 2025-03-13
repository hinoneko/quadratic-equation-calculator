from calculator import solve_quadratic


def get_coefficient(name):
    while True:
        value = input(f"{name} = ")
        try:
            value = float(value)
            if name == "a" and value == 0:
                print("Coefficient 'a' cannot be 0 (not a quadratic equation).")
                continue
            return value
        except ValueError:
            print(f"Expected a valid real number, got {value} instead")


def interactive_mode():

    a = get_coefficient("a")
    b = get_coefficient("b")
    c = get_coefficient("c")

    roots = solve_quadratic(a, b, c)

    if roots:
        for i, root in enumerate(roots):
            print(f"x{i + 1} = {root}")
    else:
        print("No real roots found.")


if __name__ == "__main__":
    interactive_mode()
