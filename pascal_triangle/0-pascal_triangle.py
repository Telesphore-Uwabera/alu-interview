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

