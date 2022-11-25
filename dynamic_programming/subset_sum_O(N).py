"""Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.
numbers = [1,2,3,7]
S=6
Output True
1+2+3 = 6

Numbers = [1, 2, 7, 1, 5]
S = 10
Output = True
1+2+7

Number = [1,3,4,8]
S=6
Output False No numbers can equal 6
"""

#My answer
def can_partition(num, sum):
    n = len(num)
    for i in range(n):
        running_sum = num[i]
        for j in range(1, n - i):
            if running_sum + num[i+j] <= sum:
                running_sum += num[i+j]
        if running_sum == sum:
            return True
    return False


#the dp answer
def can_partition(num, sum):
    n = len(num)
    dp = [False for x in range(sum+1)]

    # handle sum=0, as we can always have '0' sum with an empty set
    dp[0] = True

    # with only one number, we can have a subset only when the required sum is equal to its value
    for s in range(1, sum+1):
        dp[s] = num[0] == s

    # process all subsets for all sums
    for i in range(1, n):
        for s in range(sum, -1, -1):
            # if dp[s]==true, this means we can get the sum 's' without num[i], hence we can move on to
            # the next number else we can include num[i] and see if we can find a subset to get the
            # remaining sum
            if not dp[s] and s >= num[i]:
                dp[s] = dp[s - num[i]]
    print(dp)
    return dp[sum]



def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8, 50, 50], 100)))


main()