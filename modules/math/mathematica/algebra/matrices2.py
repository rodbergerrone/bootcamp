def add_matrices(m1, m2):
    c = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] + m2[i][j])
        c.append(row)
    return c

    # hacking z zipem
    # c = []
    # for row1, row2 in zip(m1, m2):
    #     c.append([x + y for x, y in zip(row1, row2)])
    # return c

def sub_matrices(m1, m2):
    c = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] - m2[i][j])
        c.append(row)
    return c