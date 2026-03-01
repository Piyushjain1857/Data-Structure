def fast_transpose(sparse):
    rows, cols, count = sparse[0]
    result = [[cols, rows, count]] + [[0, 0, 0] for _ in range(count)]

    if count == 0:
        return result

    # Step 1: Count elements in each column
    col_count = [0] * cols
    for i in range(1, count + 1):
        col = sparse[i][1]
        col_count[col] += 1

    # Step 2: Find starting position
    start_pos = [0] * cols
    start_pos[0] = 1
    for i in range(1, cols):
        start_pos[i] = start_pos[i-1] + col_count[i-1]

    # Step 3: Place elements
    for i in range(1, count + 1):
        r, c, v = sparse[i]
        pos = start_pos[c]
        result[pos] = [c, r, v]
        start_pos[c] += 1

    return result