package main

import (
    "fmt";
    "strings"
)

func convert(s string, numRows int) string {
    var new_str = ""
    switch {
        case len(s) == 1 || numRows == 1:
            return s
        case numRows == 2:
            var str_tmp1, str_tmp2 string
            for index, sbyte := range s {
                if (index % 2) == 0 {
                    str_tmp1 += string(sbyte)
                } else {
                    str_tmp2 += string(sbyte)
                }
            }
            fmt.Println(str_tmp1+str_tmp2)
            return (str_tmp1+str_tmp2)
        default:
            var all_list map[int][]string
            all_list = make(map[int][]string)

            for i:=0; i < numRows; i ++ {
                all_list[i] = nil
            }

            // 根据需求在列表中添加字符
            var count = 0
            // True | False = add | min
            var add_or_min = true
            for i:=0; i < len(s); i++ {
                fmt.Println(string(s[i]))
                if count >= numRows {
                    add_or_min = false
                    count = count - 2
                }
                
                if add_or_min {
                    all_list[count] = append(all_list[count], string(s[i]))
                    count ++
                } else {
                    all_list[count] = append(all_list[count], string(s[i]))
                    count --
                }
                if count == -1{
                    add_or_min = true
                    count = 1
                }
            }
            fmt.Println(all_list)

            // golang 中, map 是一种无序的序列
            // for key := range all_list {
            for i:=0; i < numRows; i ++ {
                new_str = new_str + strings.Join(all_list[i], "")
            }
            fmt.Println(new_str)
            return new_str
    }
}

func main() {
    s := "ABC"
    numRows := 3
    convert(s, numRows)
}