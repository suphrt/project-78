def right_back(rows, cols, A, curr_row, curr_col):
    if curr_row == rows-1:
        if curr_col == cols - 1:
            return A[rows-1][cols-1]
        elif(curr_row < rows-1):
            return A[curr_row][curr_col] + max_coins()
