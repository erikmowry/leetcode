"""Top Down Solution"""
def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return knapsack_recursive(dp, profits, weights, capacity, 0)

def knapsack_recursive(dp, profits, weights, capacity, current_index):
    if capacity <= 0 or current_index >= len(profits):
        return 0
    #if you have not seen this before store the capacity in the corresponding memo
    if dp[current_index][capacity] != -1:
        return dp[current_index][capacity]

    #Calculate profit starting at this current index and add items until the capacity is maxed out
    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + \
                  knapsack_recursive(dp, profits, weights, capacity - weights[current_index], current_index+1)
    #calculate profit 2 if we skip the current index
    profit2 = knapsack_recursive(dp, profits, weights, capacity, current_index + 1)
    #compare the max_profit of including the current index and excluding the current index and keep the winner
    dp[current_index][capacity] = max(profit1, profit2)
    return dp[current_index][capacity]

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()