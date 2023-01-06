def solve(matrix):
    # CODE HERE
    m = len(matrix)
    n = len(matrix[0])
    row = [False] * m
    col = [False] * n
    
    # mark the rows and cols that need to be set as 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True
    
    # set the rows and cols as 0
    for i in range(m):
        for j in range(n):
            if row[i] or col[j]:
                matrix[i][j] = 0
    
    return matrix
