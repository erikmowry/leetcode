"""Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.
numbers = [1,2,3,7]
S=6
Output True
1+2+3 = 6

Numbers = [1, 2, 7, 1, 5]
S = 10
Output = True
1+2+7

Number = [1,3,4,8]tr
S=6
Output False No numbers can equal 6
"""

def can_partition(num, sum):

    n = len(num)
    dp = [[False for x in range(sum+1)] for y in range(n)]
    """
        0 1 2 3 4 5 6
    0   0 0 0 0 0 0 0
    1   0 0 0 0 0 0 0 
    2   0 0 0 0 0 0 0 
    3   0 0 0 0 0 0 0 
    
    """
    #Zero columns is always true
    for i in range(n):
        dp[i][0] = True

    #Go through the first list and check if one number equals the sum
    for i in range(1, sum+1):
        if num[0] == i:
            dp[0][i] = True
    #Loop through the numbers and through the incremented total
    #If the previous number was equal to the sum make this value True else if this number is <= the incremental total find the condition for it's counterpart
    # for instance if j = 4 and i = 2; 4 >= 3 so go find dp[1][6-3=3]
    for i in range(1, n):
        for j in range(1, sum+1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i -1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i-1][j-num[i]]


    return dp[n-1][sum]

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()