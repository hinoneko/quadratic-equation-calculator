def get_coefficient(name):
    while True:
        value = input(f"Enter coefficient {name}: ")
        try:
            value = float(value)
            if name == "a" and value == 0:
                print("Coefficient 'a' cannot be 0.")
                continue
            return value
        except ValueError:
            print(f"Invalid input. Expected a real number, got {value}.")
