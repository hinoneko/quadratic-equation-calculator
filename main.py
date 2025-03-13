import sys
from interactive_mode import interactive_mode
from file_mode import file_mode


def main():
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 2:
        file_path = sys.argv[1]
        file_mode(file_path)
    else:
        print("Usage: python main.py [file_path]")


if __name__ == "__main__":
    main()
