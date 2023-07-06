def dot(a, b):
    '''
    Алгоритм в лоб за O(n^3).
    Алгоритм Штрассена работате на O(n^2.81).
    '''
    n = len(a)
    result = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result
