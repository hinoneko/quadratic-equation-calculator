# Quadratic Equation Calculator

This console application quadratic equation calculator of the form:

```
ax² + bx + c = 0
```

Where a, b, and c are real numbers, with the condition that a ≠ 0.

The program calculates the real roots of the equation, if they exist, and supports two modes of operation: **interactive** and **non-interactive (file)**.


### Features

- **Interactive Mode**: Enter coefficients manually through the console. 
- **File Mode**: Read coefficients from a file. 
- **Handles input validation and guides the user in case of errors**.

## Interactive Mode

If no arguments are passed, the application will run in interactive mode. It will prompt you to input the coefficients step by step:

Example:

```
Welcome to the Quadratic Equation Calculator!
Please enter the coefficients for the equation ax² + bx + c = 0

Select mode:
1. Interactive mode (enter coefficients manually)
2. File mode (read coefficients from a file)
Enter your choice (1 or 2): 1
Enter coefficient a: 2
Enter coefficient b: 7
Enter coefficient c: 4
Equation is: (2.0) x² + (7.0) x + (4.0) = 0
There are 2 roots
x1 = -0.7192235935955849
x2 = -2.7807764064044154
```

## File Mode

To use the file mode, provide the file path as an argument. The file should contain exactly 3 space-separated numbers representing coefficients a, b, and c.

Example file content:

```
1 -1 0

```

Running the program:

```
Welcome to the Quadratic Equation Calculator!
Please enter the coefficients for the equation ax² + bx + c = 0

Select mode:
1. Interactive mode (enter coefficients manually)
2. File mode (read coefficients from a file)
Enter your choice (1 or 2): 2
Enter the path to the file with coefficients: valid.txt
Equation is: (1.0) x² + (-1.0) x + (0.0) = 0
There are 2 roots
x1 = 1.0
x2 = 0.0
```

If the file format is invalid or the file does not exist, the program will display an error and crash.

## Error Handling

- **Invalid choice**: This occurs when you enter an option other than 1 or 2 when selecting the mode.
- **Coefficient 'a' cannot be 0**: The application enforces this rule both in interactive and file modes, as a quadratic equation requires a ≠ 0.
- **Invalid file format**: The file must contain exactly three space-separated numbers.
- **File '{file_path}' does not exist**: This error appears if the specified file path is incorrect or the file doesn't exist.
- **Error: {e}**: This is a generic error message for unexpected issues (like parsing errors).
- **Invalid input. Expected a real number, got {value}**: This happens if you enter something that isn't a valid number (like text or symbols).

## How to Run

### Clone the repository

First, you need to download the project to your local machine. You can do this using Git:

```bash
git clone https://github.com/yourusername/quadratic_equation_calculator.git
cd quadratic_equation_calculator
```

### Run the project

Once you're inside the project folder, run the main script:

```bash 
python main.py
```

## Revert Commit

To revert to a previous state of the project, use the git revert command. For example:

Let's use a command that displays the commit history in a concise form.

```bash
git log --oneline
```
After that, we will make a revert with the given hash.

```bash
git revert <commit_hash>
```
Where <commit_hash> is the hash of the commit you want to revert to.

### Link to the 
1. [Revert Commit](https://github.com/hinoneko/quadratic-equation-calculator/commit/2614c4046913591d014f4d91faf6b4f7b09521ba)
2. [Revert Commit](https://github.com/hinoneko/quadratic-equation-calculator/commit/2920ca11b2f492f13c802afe686a2c99a5cde2c1)