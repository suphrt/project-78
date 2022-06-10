if __name__ == '__main__':
    n = 10
    m = 10
    A = []
    for _ in range(n):
        row = list(map(int, input().split()))
        assert len(row) == m
        A.append(row)

    C = []
    for row in range(n):
        C.append([0] * m)
    for i in range(n):
        for j in range(m):
            C[i][j] = A[9-i][j]

    B = []
    for row in range(n):
        B.append([0] * m)

    for i in range(n):
        for j in range(m):
            B[0][0] = C[0][0]
            B[0][j] = B[0][j - 1] + C[0][j]
            B[i][0] = B[i - 1][0] + C[i][0]


    for i in range(1, n):
        for j in range(1, m):
            B[i][j] = max(B[i-1][j], B[i][j-1]) + C[i][j]

    print(B)
    print(B[9][9])

    for i in range(1, n):
        for j in range(1, m):
            B[i][j] = min(B[i-1][j], B[i][j-1]) + C[i][j]

    print(B[n-1][m-1])
