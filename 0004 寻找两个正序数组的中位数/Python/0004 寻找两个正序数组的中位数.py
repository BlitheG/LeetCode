#!python3
#-*- coding: utf-8 -*-
"""
4. 寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

示例 3：
输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000

示例 4：
输入：nums1 = [], nums2 = [1]
输出：1.00000

示例 5：
输入：nums1 = [2], nums2 = []
输出：2.00000

提示：
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # 时间复杂度位m+n的暴力解法
        if len(nums1) + len(nums2) == 0:
            res = '%.5f' % 0
        elif  len(nums1) + len(nums2) == 1:
            res = '%.5f' % (nums1+nums2)[0]
        else:
            tmp_list = nums1+nums2
            tmp_list.sort()
            if len(tmp_list) % 2 == 0:
                res = '%.5f' % ((tmp_list[int(len(tmp_list)/2-1)] + tmp_list[int(len(tmp_list)/2)]) /2)
            else:
                res = '%.5f' % (tmp_list[int(len(tmp_list)/2)])
        return float(res)


    def findMedianSortedArrays2(self, nums1: list[int], nums2: list[int]) -> float:
        # 时间复杂度位log(m+n)
        if len(nums1) + len(nums2) == 0:
            return '%.5f' % 0
        elif  len(nums1) + len(nums2) == 1:
            return '%.5f' % (nums1+nums2)[0]

        # 二分查找
        pass


if __name__ == '__main__':
    nums1 = []
    nums2 = []
    target = 0.00000
    assert(Solution().findMedianSortedArrays(nums1, nums2) == target)
    nums1 = []
    nums2 = [1]
    target = 1.00000
    assert(Solution().findMedianSortedArrays(nums1, nums2) == target)
    nums1 = [2]
    nums2 = []
    target = 2.00000
    assert(Solution().findMedianSortedArrays(nums1, nums2) == target)
    nums1 = [1, 2]
    nums2 = [3, 4]
    target = 2.50000
    assert(Solution().findMedianSortedArrays(nums1, nums2) == target)
    nums1 = [1,3]
    nums2 = [2]
    target = 2.00000
    assert(Solution().findMedianSortedArrays(nums1, nums2) == target)
    nums1 = [0,0,0,0,0]
    nums2 = [-1,0,0,0,0,0,1]
    target = 0.00000
    assert(Solution().findMedianSortedArrays(nums1, nums2) == target)

    
