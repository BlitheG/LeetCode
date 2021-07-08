package main

import (
    "fmt"
)


/*
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
 */


func majorityElement1(nums []int) int {
    // 冒泡排序后取中位数
    for i:=0; i < len(nums); i++ {
        for j:=0; j < (len(nums)-1); j++ {
            if (nums[j] > nums[j+1]) {
                nums[j], nums[j+1] = nums[j+1], nums[j]
            }
        }
    }
    fmt.Println(nums)
    return nums[len(nums)/2]
}

func majorityElement(nums []int) int {
    var tmp_map map[int]int
    tmp_map = make(map[int]int)
    var count, res int

    for _, v := range nums {
        _, is_in := tmp_map[v]
        if is_in {
            tmp_map[v] ++
        } else {
            tmp_map[v] = 1
        }
    }
    fmt.Println(tmp_map)

    for key := range tmp_map {
        if count < tmp_map[key] {
            count = tmp_map[key]
            res = key
        }
    }

    return res
}


func main() {
    nums := []int{2,2,1,1,1,2,2}
    res := majorityElement(nums)
    fmt.Println(res)
}