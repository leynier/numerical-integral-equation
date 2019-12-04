def gauss(matrix):
    n = len(matrix)

    for i in range(n):
        # Search for maximum in this column
        maxEl = abs(matrix[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > maxEl:
                maxEl = abs(matrix[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n + 1):
            matrix[maxRow][k], matrix[i][k] = matrix[i][k], matrix[maxRow][k]

        # Make all rows below this one 0 in current column
        for k in range(i + 1, n):
            c = -matrix[k][i]/matrix[i][i]
            for j in range(i, n+1):
                if i == j:
                    matrix[k][j] = 0
                else:
                    matrix[k][j] += c * matrix[i][j]

    # Solve equation Ax=b for an upper triangular matrix
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = matrix[i][n]/matrix[i][i]
        for k in range(i-1, -1, -1):
            matrix[k][n] -= matrix[k][i] * x[i]
    return x
