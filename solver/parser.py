def parse_data(fname="list.lst"):
    matrix = []

    with open(fname, "r") as src:
        while a := src.readline():
            b = a.split()
            t1, t2, *r = b
            for i in range(len(r)):
                try:
                    r[i] = int(r[i], 2)
                except Exception:
                    r[i] = None

            t1 = int(t1)
            t2 = int(t2)

            matrix.append([t1, t2, *r])

    new_matrix = []

    # Крч среди одинаковых номеров тактов, мы должны брать тот, у которого меньше ps,
    # но в случае, когда у нас есть одинаковые ps для раних, мы берем тот, у которого больше delta (кринж)
    i = 0

    while i < len(matrix) - 1:
        if matrix[i][2] is None:
            matrix.pop(i)
            continue

        if matrix[i][0] == matrix[i + 1][0] and matrix[i][2] == matrix[i + 1][2]:
            matrix.pop(i)
            continue

        if matrix[i][0] != matrix[i + 1][0] and matrix[i][2] == matrix[i + 1][2]:
            matrix.pop(i + 1)

        i += 1

    return matrix
