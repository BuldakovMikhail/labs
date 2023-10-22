def parse_data(fname="list.lst"):
    matrix = []

    with open(fname, "r") as src:
        while a := src.readline():
            b = a.split()
            t1, t2, r1, r2, r3 = b
            try:
                r1 = int(r1, 2)
            except Exception:
                r1 = None

            try:
                r2 = int(r2, 2)
            except Exception:
                r2 = None

            try:
                r3 = int(r3, 2)
            except Exception:
                r3 = None

            t1 = int(t1)
            t2 = int(t2)

            matrix.append([t1, t2, r1, r2, r3])

    new_matrix = []

    for i in range(len(matrix) - 1):
        if matrix[i][2] and matrix[i][2] == matrix[i + 1][2]:
            new_matrix.append(matrix[i])

    return new_matrix
