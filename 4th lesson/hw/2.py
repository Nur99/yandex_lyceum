def transpose(matrix):
    if (matrix == []):
        return
    new_matrix = [[] for j in range(len(matrix[0]))]
    i = 0
    for row in matrix:
        i = 0
        for j in row:
            new_matrix[i].append(j)
            i += 1
    matrix.clear()
    matrix.extend(new_matrix)
