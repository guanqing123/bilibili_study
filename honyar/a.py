def closest_sum_to_11(nums, target=11):
    # 动态规划数组
    dp = [-float('inf')] * (target + 1)
    dp[0] = 0  # 初始值

    # 遍历每个数字
    for num in nums:
        for x in range(num, target + 1):
            dp[x] = max(dp[x], dp[x - num] + num)

    # 返回 <= target 的最大值
    return max(dp)

# 给定的数字列表
nums = [4.69, 5.93, 6.79, 4.13, 5.98, 3.98, 5.21, 6.43, 3.86, 1.08, 7.97, 8.84, 7.5, 10.57, 7.89]
result = closest_sum_to_11(nums)
print(f"接近但不超过 11 的最大总和是：{result}")
