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
    """Create a table the size of half the sum of the list + 1 (Zero indexed) X the length of the list
    n = [1, 2, 3, 4]
    s = 1+2+3+4 = 10
    s // 2 = 5 
        0  1  2  3  4  5 
      0 -1 -1 -1 -1 -1 -1
      1 -1 -1 -1 -1 -1 -1
      2 -1 -1 -1 -1 -1 -1
      3 -1 -1 -1 -1 -1 -1
    """
    dp = [[-1 for x in range(int(s//2)+1)] for y in range(len(num))]
    return True if partition_recurse(dp, num, s // 2, 0) == 1 else False

def partition_recurse(dp, num, sum, current_index):
    """If sum == 0 return 1"""
    if sum == 0:
        return 1

    """Recursive exit condition"""
    n = len(num)
    if n == 0 or current_index >= n:
        return 0

    """current_index = 0 
       sum = 5 
       df[0][5] == -1 TRUE
            num[0]==1  1 <= 5 True:
                0"""
    if dp[current_index][sum] == -1:
        if num[current_index] <= sum:
            if partition_recurse(dp, num, sum - num[current_index], current_index+1) ==1:
                dp[current_index][sum] = 1
                return 1
    dp[current_index][sum] = partition_recurse(dp, num, sum, current_index + 1)
    print(dp, current_index, sum)
    return dp[current_index][sum]
def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()