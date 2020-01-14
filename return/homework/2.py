def possible_turns(cell):
    turns = []
    coords = cell_str2tuple(cell)
    for delta_col in [-2, -1, 1, 2]:
        for delta_row in [-2, -1, 1, 2]:
            if abs(delta_row) + abs(delta_col) == 3:
                new_coords = (coords[0] + delta_col, coords[1] + delta_row)
                if on_field(new_coords):
                    turns.append(cell_tuple2str(new_coords))
    return turns


def cell_str2tuple(string):
    col = ord(string[0]) - ord('A') + 1
    row = int(string[1])
    return (col, row)


def cell_tuple2str(coords):
    col = chr(ord('A') + coords[0] - 1)
    row = str(coords[1])
    return col + row


def on_field(coords):
    return (1 <= coords[0] <= 8) and (1 <= coords[1] <= 8)
