

def knapsack(weight, profit, C, n):
    dp = [[0] * (n+1) for j in range(C+1)]
    
    for c in range(1, C+1):
        for item in range(1, n+1):
            dp[c][item] = dp[c][item-1]
            if (weight[item-1] <= c):
                dp[c][item] = max(dp[c][item-1], dp[c-weight[item-1]][item-1] + profit[item-1])

    return dp[C][n]

if __name__ == '__main__':
    w2 = [4, 6, 8]
    p2 = [7, 6, 9]

    w4 = [5, 6, 8]
    p4 = [7, 6, 9]
    
    C = 14
    n = 3

    ans2 = knapsack(w2, p2, C, n)
    ans4 = knapsack(w4, p4, C, n)

    print('(2)\ninputs:\nC =', C, '\nn =', n, '\nweights =', w2, '\nprofits =', p2, '\n\noutput:', ans2)
    print()
    print('(4)\ninputs:\nC =', C, '\nn =', n, '\nweights =', w4, '\nprofits =', p4, '\n\noutput:', ans4)