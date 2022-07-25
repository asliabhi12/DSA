def matrixReshape(mat, r: int, c: int):
    rows = len(mat)
    cols = len(mat[0])
    o = r * c
    if rows*cols < o or rows*cols > o:
        return mat

    new_matrix = [[0 for j in range(c)] for i in range(r)]
    for i in range(o):
        new_matrix[i//c][i%c] = mat[i//cols][i%cols]

    return new_matrix


