def rob(nums):
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    return dp[n-1]
def get_input():
    nums = input("Enter a list of integers separated by spaces: ")
    nums = [int(num) for num in nums.split()]
    return nums
nums = get_input()
print(rob(nums))
