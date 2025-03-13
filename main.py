from interactive_mode import interactive_mode
from file_mode import file_mode


def main():
    print("Welcome to the Quadratic Equation Calculator!")
    print("Please enter the coefficients for the equation ax² + bx + c = 0\n")

    print("Select mode:")
    print("1. Interactive mode (enter coefficients manually)")
    print("2. File mode (read coefficients from a file)")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        interactive_mode()
    elif choice == "2":
        file_mode()
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
