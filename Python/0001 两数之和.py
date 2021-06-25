#!python3
#-*- coding: utf-8 -*-
"""
1. 两数之和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1]。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
 
提示：
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
只会存在一个有效答案
进阶：你可以想出一个时间复杂度小于 O(n^2) 的算法吗？
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # # 超过输出限制
        # count = 0
        # res = 1
        # while count < len(nums):
        #     if nums[count] + nums[res] == target:
        #         return [count, res]
        #     else:
        #         res += 1
        #         if res == len(nums):
        #             count += 1
        #             res = count + 1
        
        num_dict = {}
        for index, num in enumerate(nums):
            num_dict[index] = num
        
        for key1, num1 in num_dict.items():
            for key2, num2 in num_dict.items():
                if key1 != key2:
                    if num1 + num2 == target:
                        return [key1, key2]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    assert (Solution().twoSum(nums, target) == [0, 1])
    nums = [3, 2, 4]
    target = 6
    assert (Solution().twoSum(nums, target) == [1, 2])