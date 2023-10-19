def pascal_triangle(n):
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

