"""Given a set of positive numbers, find if we can partition it into two subsets
such that the sum of elements in both the subsets is equal"""

"""Input {1, 2, 3, 4}
   output: True 
   Explanation: The given set can be partitioned into two subsets with equal sum: {1,4} & {2, 3}
   
   Input: {1,1,3,4,7}
   output: True 
   Explanation: The given set can be partitioned into two subsets with equal sum: {1,3,4}, {1, 7}
   
   Input {2,3,4,6}
   output: False
   Explanation: The given set cannot be partitioned into two subsets with equal sum"""

"""Find the sum of all numbers
Divide the sum by 2 
recurse through and if all sum - nums == 0 return True"""
def can_partition(num):
    s = sum(num)
    #Check if the sum is divisible by 2
    if s % 2 != 0:
        return False

    int_sum = s // 2
    n = len(num)
    dp = [[False for x in range(int_sum+1)] for y in range(len(num))]

    for i in range(0, n):
        dp[i][0] = True

    for i in range(1, int_sum+1):
        dp[0][i] = num[0] == i
        print(dp)


    for i in range(1, n):
        for j in range(1, int_sum + 1):
            if dp[i -1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i -1][j - num[i]]
    return dp[n-1][int_sum]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()