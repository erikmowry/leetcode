""""for each item at index 'i' (0 <= i < items.length) and capacity 'c' (0 <= c <= capacity)
1) exclude the item at index 'i'. In This case,
we will take whatever profit we get from the sub-array excluding this item=>dp[i-1][c]
2) INclude the item at index 'i' if its weight is not more than the capacity. In this case, we include
its profit plus whatever profit we get from the remaining capacity and from remaining items -=> profits[i] +
dp[i-1][c-weights[i]]

dp[i[[c] = max( dp[i-1][c], profits[i] + dp[i-1][c-wights[i]])"""

def solve_knapsack(profits:list, weights:list, capacity:int):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp = [[0 for x in range(capacity+1)] for y in range(n)]
    for i in range(0, n):
        dp[i][0] = 0

    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c - weights[i]]
            profit2 = dp[i-1][c]
            dp[i][c] = max(profit1, profit2)
    print_selected_elements(dp, weights, profits, capacity)
    return dp[n - 1][capacity]

def print_selected_elements(dp, weights, profits, capacity):
  print("Selected weights are: ", end='')
  n = len(weights)
  totalProfit = dp[n-1][capacity]
  for i in range(n-1, 0, -1):
    if totalProfit != dp[i - 1][capacity]:
      print(str(weights[i]) , end=', ')
      capacity -= weights[i]
      totalProfit -= profits[i]

  if totalProfit != 0:
    print(str(weights[0]) + " ", end='')
  print()

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()