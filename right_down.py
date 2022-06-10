if __name__ == '__main__':
    n = 10
    m = 10
    A = []
    for _ in range(n):
        row = list(map(int, input().split()))
        assert len(row) == m
        A.append(row)

    B = []

    for row in range(m):
        B.append([0] * n)

    for i in range(n):
        for j in range(m):
            B[0][0] = A[0][0]
            B[0][j] = B[0][j-1] + A[0][j]
            B[i][0] = B[i - 1][0] + A[i][0]

    for i in range(1, n):
        for j in range(1, m):
            B[i][j] = max(B[i-1][j], B[i][j-1]) + A[i][j]

    print(B)
    print(B[9][9])

    for i in range(1, n):
        for j in range(1, m):
            B[i][j] = min(B[i-1][j], B[i][j-1]) + A[i][j]
    print(B[n-1][m-1])