#!/usr/bin/env python 3
# -*-coding: utf-8 -*-

if __name__ == '__main__':
    n = 10
    m = 10

    A = []
    for _ in range(n):
        rows = list(map(int, input().split()))
        assert len(rows) == m
        A.append(rows)

    B = []
    for i in range(n):
        B.append([0]*m)

    for i in range(n):
        for j in range(m):
            B[0][0] = A[0][0]
            B[0][j] = B[0][j - 1] + A[0][j]
            B[i][0] = B[i-1][0] + A[i][0]