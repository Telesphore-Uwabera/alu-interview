#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's Triangle of depth n as a list of lists.

    :param n: The depth of Pascal's Triangle.
    :type n: int
    :return: A list of lists representing Pascal's Triangle.
    :rtype: list of lists of integers
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev_row = triangle[i - 1]
            new_row = [1]
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])
            new_row.append(1)
            triangle.append(new_row)

    return triangle

def print_triangle(triangle):
    """
    Print the Pascal's Triangle.
    """
    for row in triangle:
        print("[{}]".format(",".join(map(str, row)))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

