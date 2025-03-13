def read_coefficients_from_file():
    while True:
        file_path = input("Enter the path to the file with coefficients: ")
        try:
            with open(file_path, "r") as file:
                content = file.read().strip()
                coefficients = content.split()

                if len(coefficients) != 3:
                    raise ValueError("Invalid file format.")

                a, b, c = map(float, coefficients)

                if a == 0:
                    raise ValueError("Coefficient 'a' cannot be 0.")

                return a, b, c

        except FileNotFoundError:
            print(f"File '{file_path}' does not exist.")

        except ValueError as e:
            print(f"Error: {e}.")
