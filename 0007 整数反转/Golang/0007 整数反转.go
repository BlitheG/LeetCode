package main

import (
    "fmt"
    "strconv"
    "math"
)


func reverse(x int) int {
    var sign string
    switch {
    case x == 0:
        return 0
    case x < 0:
        sign = "min"
        x = x * -1
    default:
        sign = "plus"
    }

    // 数字转字符串
    var new_num string
    var warehouse []string
    new_num = strconv.Itoa(x)
    for _, b := range new_num {
        warehouse = append(warehouse, string(b))
    }
    fmt.Println(warehouse)

    var new_num_str string
    for i := 1; i <= len(warehouse); i++ {
        new_num_str = new_num_str + warehouse[len(warehouse)-i]
    }
    fmt.Println(new_num_str)

    var res int
    if sign == "min" {
        new_num_tmp, error := strconv.Atoi(new_num_str)
        res = 0 - new_num_tmp
        if error != nil{
            fmt.Println("字符串转换成整数失败")
        }
    } else {
        new_num_tmp, error := strconv.Atoi(new_num_str)
        res = new_num_tmp
        if error != nil{
            fmt.Println("字符串转换成整数失败")
        }
    }

    // 验证范围 -2^31 <= x <= 2^31 - 1
    left_num := 0 - int(math.Pow(2, 31))
    right_num := int(math.Pow(2, 31)-1)
    fmt.Println(left_num, res, right_num)
    if left_num < res {
        if res < right_num {
            return int(res)
        }
    }
    return 0

}

func main() {
    fmt.Println()
    reverse(123)
}