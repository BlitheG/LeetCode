#!python3
#-*- coding: utf-8 -*-
"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：
输入：[3,2,3]
输出：3

示例 2：
输入：[2,2,1,1,1,2,2]
输出：2

进阶：
尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
"""
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums_dict = dict()
        for item in nums:
            if item not in nums_dict:
                nums_dict[item] = 1
            else:
                nums_dict[item] += 1
        tmp_key = ""
        count = 0
        for key, value in nums_dict.items():
            if count < value:
                count = value
                tmp_key = key
        return tmp_key

    def majorityElement2(self, nums: list[int]) -> int:
        """
        网上找的有意思的思路：
        列表排序过后，中间的数属于众数，不进行计算直接去中间的数
        """
        nums.sort()
        return nums[int(len(nums)/2)]

if __name__ == '__main__':
    nums = [3, 2, 3]
    target = 3
    assert(Solution().majorityElement(nums) == target)