import sys
from interactive_mode import interactive_mode
from file_mode import file_mode


def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        file_mode(file_path)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
