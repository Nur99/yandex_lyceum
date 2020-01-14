def find_mountain(heightsMap):
    best_row, best_col = 0, 0
    for row in range(len(heightsMap)):
        for col in range(len(heightsMap[row])):
            if heightsMap[row][col] > heightsMap[best_row][best_col]:
                best_row, best_col = row, col
    return best_row, best_col
