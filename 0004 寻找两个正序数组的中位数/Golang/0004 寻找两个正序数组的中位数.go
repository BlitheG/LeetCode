package main

import (
    "fmt"
)

/*
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
*/

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    var res float64
    switch {
        case (len(nums1) + len(nums2) == 0):
            res  = 0
        case (len(nums1) + len(nums2) == 1): 
            switch {
                case (len(nums1) == 1):
                    res = float64(nums1[0])
                case (len(nums2) == 1):
                    res = float64(nums2[0])
                default:
                    res = 0
            }
        default:
            // 合并数组
            tmp_list := make([]int, len(nums1))
            copy(tmp_list, nums1)
            fmt.Println(tmp_list)
            for _, v := range nums2 {
                tmp_list = append(tmp_list, v)
            }
            fmt.Println(tmp_list)

            // 冒泡排序
            for l:=0; l < len(tmp_list); l++ {
                for k:=0; k < (len(tmp_list)-1); k++ {
                    if (tmp_list[k] > tmp_list[k+1]) {
                        tmp_list[k], tmp_list[k+1] = tmp_list[k+1], tmp_list[k]
                    }
                }
            }
            fmt.Println(tmp_list)

            if (len(tmp_list) % 2) == 0 {
                res = (float64(tmp_list[len(tmp_list)/2-1]) + float64(tmp_list[len(tmp_list)/2])) / 2
            } else {
                res = float64(tmp_list[len(tmp_list) / 2])
            }
    }
    return res
}

func main() {
    nums1 := []int{5, 7, 3}
    nums2 := []int{3, 4}
    findMedianSortedArrays(nums1, nums2)
}