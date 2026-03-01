# Sparse Matrix A
A = [
    [4, 4, 3],
    [0, 1, 5],
    [1, 3, 8],
    [3, 2, 6]
]

# Sparse Matrix B
B = [
    [4, 4, 3],
    [0, 1, 3],
    [1, 2, 7],
    [3, 2, 2]
]

def add_sparse(A, B):
    if A[0][0] != B[0][0] or A[0][1] != B[0][1]:
        print("Addition not possible")
        return None

    result = []
    result.append([A[0][0], A[0][1], 0])

    i = 1
    j = 1

    while i <= A[0][2] and j <= B[0][2]:
        if A[i][0] == B[j][0] and A[i][1] == B[j][1]:
            result.append([A[i][0], A[i][1], A[i][2] + B[j][2]])
            i += 1
            j += 1
        elif (A[i][0], A[i][1]) < (B[j][0], B[j][1]):
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1

    while i <= A[0][2]:
        result.append(A[i])
        i += 1

    while j <= B[0][2]:
        result.append(B[j])
        j += 1

    result[0][2] = len(result) - 1
    return result


# Perform Addition
C = add_sparse(A, B)

print("Resultant Sparse Matrix:")
for row in C:
    print(row)