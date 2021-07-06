package main

import (
    "fmt"
)

func twoSum(nums []int, target int) []int {
    var nums_map = make(map[int]int)
    var res []int

    // 将数组数据存到集合中
    for i, x := range nums {
        nums_map[i] = x
    }

    // 遍历集合，去重坐标相同的数据，计算和值
    re:
        for k1, v1 := range nums_map {
            for k2, v2 := range nums_map {
                if (k1 != k2){
                    if (v1 + v2) == target {
                        res = append(res, k1)
                        res = append(res, k2)
                        break re
                    }
                }
            }
        }
    return res

}

func main() {
    nums := []int{2, 7, 11, 15}
    target := 9
    res := twoSum(nums, target)
    fmt.Println(res)
}