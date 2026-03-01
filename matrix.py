def convert_to_sparse(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    sparse = []
    
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                sparse.append([i, j, matrix[i][j]])
                count += 1

    # Insert metadata at beginning
    sparse.insert(0, [rows, cols, count])
    return sparse

matrix = [
    [0, 0, 3, 0],
    [0, 0, 0, 0],
    [5, 0, 0, 0],
    [0, 0, 0, 7]
]

sparse_matrix = convert_to_sparse(matrix)

for row in sparse_matrix:
    print(row)