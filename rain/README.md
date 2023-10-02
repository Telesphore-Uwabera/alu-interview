
# Rainwater Trapping Project

This project is designed to solve the problem of calculating the amount of rainwater retained between walls represented by a list of non-negative integers. It follows specific guidelines and requirements.

## Project Requirements

1. The code is written in Python 3.4.3.
2. Allowed editors: vi, vim, emacs.
3. All files end with a new line.
4. The first line of all files is `#!/usr/bin/python3`.
5. A `README.md` file is included at the root of the project folder.
6. The code follows the PEP 8 style (version 1.7.x).
7. No external modules are imported.
8. All modules and functions are documented.
9. All files are executable.

## Usage

To calculate the amount of rainwater retained, use the provided `rain` function in the `0-rain.py` file. You can call the function with a list of non-negative integers representing wall heights.

Example usage in `0_main.py`:

```python
walls = [0, 1, 0, 2, 0, 3, 0, 4]
print(rain(walls))  # Output: 6

walls = [2, 0, 0, 4, 0, 0, 1, 0]
print(rain(walls))  # Output: 6
```

## File Structure

- `0-rain.py`: Contains the implementation of the `rain` function.
- `0_main.py`: Example usage of the `rain` function.
- `README.md`: This documentation file.

## Author

This project is authored by Telesphore Uwabera
