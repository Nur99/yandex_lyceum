def valid(x):
    return 0 <= x < 10


class SeaMap:
    def __init__(self):
        self.map_ = [['.'] * 10 for i in range(10)]

    def shoot(self, row, col, info):
        if info == 'miss':
            self.map_[row][col] = '*'
        elif info == 'hit':
            self.map_[row][col] = 'x'
        elif info == 'sink':
            self.map_[row][col] = 'x'
            coords = [(row, col)]
            for r in range(row + 1, 10):
                if self.map_[r][col] != 'x':
                    break
                coords.append((r, col))
            for r in range(row - 1, -1, -1):
                if self.map_[r][col] != 'x':
                    break
                coords.append((r, col))
            for c in range(col + 1, 10):
                if self.map_[row][c] != 'x':
                    break
                coords.append((row, c))
            for c in range(col - 1, -1, -1):
                if self.map_[row][c] != 'x':
                    break
                coords.append((row, c))
            for r, c in coords:
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if (valid(r + dr) and valid(c + dc)
                                and self.map_[r + dr][c + dc] == '.'):
                            self.map_[r + dr][c + dc] = '*'

    def cell(self, row, col):
        return self.map_[row][col]
