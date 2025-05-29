# CrowdStrike Python Demo

This project demonstrates basic Python operations with lists and strings, including utility functions and unit tests.

## Project Structure

- `src/`: Source code for list and string utilities.
- `test/`: Unit tests for the source code.
- `conftest.py`: Pytest fixtures.

## How to Run the Code

You can run the example code in each module directly from the terminal:

```sh
python src/lists.py
python src/strings.py
```

These scripts will print example outputs demonstrating the list and string functions.

## How to Run the Code Using Visual Studio Code

1. Open the project folder in VS Code.
2. Make sure the Python extension is installed.
3. Open the file you want to run, such as `src/lists.py` or `src/strings.py`.
4. Click the green "Run" button in the top right, or right-click inside the file and select "Run Python File in Terminal".
5. The output will appear in the integrated terminal at the bottom of VS Code.

These steps let you quickly run and view the results of your Python scripts directly within VS Code.

## How to Run the Tests

### Using the Terminal

1. Make sure you have `pytest` installed:
    ```sh
    pip install pytest
    ```
2. Run all tests from the project root:
    ```sh
    pytest
    ```

### Using Visual Studio Code

1. Open the project folder in VS Code.
2. Make sure the Python extension is installed.
3. Open the Testing sidebar (beaker icon).
4. Click "Run All Tests" or run individual tests from the test explorer.

## What the Code Does

- **src/lists.py**:  
  - Manages a list of CrowdStrike teams.
  - Functions to add, remove, sort, and copy teams.
  - Prints results and demonstrates usage when run as a script.

- **src/strings.py**:  
  - Provides string utilities: uppercase, lowercase, splitting, palindrome check, etc.
  - Prints results and demonstrates usage when run as a script.

- **test/**:  
  - Contains unit tests for all list and string functions.
  - Tests cover adding/removing teams, sorting, copying, and string operations like palindrome checking and case conversion.

---