import math


def quadratic_calculator(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be 0.")

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
