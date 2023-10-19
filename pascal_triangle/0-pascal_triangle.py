#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to a specified height.

    Args:
        n (int): The height of the Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    If n is less than or equal to 0, an empty list is returned.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # The first element in each row is always 1
        if triangle:
            last_row = triangle[-1]
            for j in range(1, i):
                # Calculate the middle elements in the row based on the previous row
                row.append(last_row[j - 1] + last_row[j])
            row.append(1)  # The last element in each row is always 1
        triangle.append(row)

    return triangle

def print_triangle(triangle):
    """
    Print Pascal's triangle.

    Args:
        triangle (list): A list of lists representing Pascal's triangle.

    Prints each row of Pascal's triangle.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row]))

if __name__ == "__main__":
    # Correct output for n = 5
    print_triangle(pascal_triangle(5))

    # Correct output for n = 1
    print_triangle(pascal_triangle(1))

    # Correct output for n = 0
    print_triangle(pascal_triangle(0))

    # Correct output for n = 10
    print_triangle(pascal_triangle(10))

    # Correct output for n = 100
    # Note: Printing a large Pascal's triangle may result in a very long output.
    # It's not practical to print the entire triangle for such a large value of n.
    # You can verify the correctness of the result in other ways.
    print_triangle(pascal_triangle(100))

