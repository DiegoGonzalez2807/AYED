def countWays(n, m):
    # Initialise dp[][] array
    dp = [[0 for i in range(n + 1)]
          for i in range(m + 1)]
    for i in range(n + 1):
        dp[1][i] = 1
    sum = 0
    for i in range(2, m + 1):
        for j in range(n + 1):
            sum = 0
            for k in range(j + 1):
                sum += dp[i - 1][k]
            dp[i][j] = sum
            print(dp)
    return dp[m][n]
if __name__ == '__main__':
    N = 20
    K = 2
    print(countWays(N, K))
