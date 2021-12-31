

def knapsack(weight, profit, C, n):
    dp = [0] * (C+1)
    
    for c in range(1, C+1):
        for item in range(n):
            if weight[item] <= c:
                dp[c] = max(dp[c], dp[c-weight[item]] + profit[item])

    return dp

if __name__ == '__main__':
    w2 = [4, 6, 8]
    p2 = [7, 6, 9]

    w4 = [5, 6, 8]
    p4 = [7, 6, 9]
    
    C = 14
    n = 3

    ans2 = knapsack(w2, p2, C, n)
    ans4 = knapsack(w4, p4, C, n)

    print('(2)\ninputs:\nC =', C, '\nn =', n, '\nweights =', w2, '\nprofits =', p2, '\n\noutput:', ans2[C])
    print('\nsub-problem graph:', ans2)
    print()
    print('(4)\ninputs:\nC =', C, '\nn =', n, '\nweights =', w4, '\nprofits =', p4, '\n\noutput:', ans4[C])
    print('\nsub-problem graph:', ans4)