import math


def quadratic_calculator(a, b, c):

    if a == 0:
        raise ValueError("Coefficient 'a' cannot be 0 (not a quadratic equation).")

    discriminant = b ** 2 - 4 * a * c

    print(f"Equation is: ({a}) x² + ({b}) x + ({c}) = 0")

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("There are 2 roots")
        return [x1, x2]
    elif discriminant == 0:
        x = -b / (2 * a)
        print("There are 1 roots")
        return [x]
    else:
        print("There are 0 roots")
        return []


if __name__ == "__main__":
    examples = [
        (2, 1, -3),
        (2, 4, 2),
        (1, 0, 9),
        (0, 1, 0),
    ]

    for a, b, c in examples:
        print("\n" + "="*30)
        try:
            roots = quadratic_calculator(a, b, c)
            for i, root in enumerate(roots):
                print(f"x{i+1} = {root}")
        except ValueError as e:
            print(f"Error: {e}")
