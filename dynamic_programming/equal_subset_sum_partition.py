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

    if s % 2 != 0:
        return False
    return partition_recurse(num, s / 2, 0)

def partition_recurse(num, sum, current_index):
    if sum == 0:
        return True
    n = len(num)
    if n == 0 or current_index >= n:
        return False

    if num[current_index] <= sum:
        if(partition_recurse(num, sum - num[current_index], cequal_subset_sum_partition.pyurrent_index +1)):
            return True
    return partition_recurse(num, sum, current_index+1)

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()