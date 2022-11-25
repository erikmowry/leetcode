def solve_knapsack(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)

def knapsack_recursive(profits, weights, capacity, current_index):
    if capacity <= 0 or current_index >= len(profits):
        return 0

    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + \
                  knapsack_recursive(profits, weights, capacity-weights[current_index], current_index+1)

    profit2 = knapsack_recursive(profits, weights, capacity, current_index+1)

    return max(profit1, profit2)

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()