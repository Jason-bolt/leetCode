def uniquePaths(m: int, n: int) -> int:
    def recur(m=m, n=n, i=0, j=0):
        if i >= m or j >= n:
            return 0
        if i == m-1 and j == n-1:
            return 1
        return recur(m, n, i+1, j) + recur(m, n, i, j+1)
    return recur()
    
print(uniquePaths(3, 7))