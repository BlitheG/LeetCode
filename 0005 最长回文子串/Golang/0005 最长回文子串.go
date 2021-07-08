package main

import (
	"fmt"
)

func longestPalindrome(s string) string {
    if (s == "" || len(s) == 0) {
        return ""
    }

    // 保存起始位
    var str_range [2] int
    var str = []byte(s)
    for i:=0; i < len(s); i++ {
        // 把回文看成中间的部分全是同一字符，左右部分相对称
        // 找到下一个与当前字符不同的字符
        i = findLongest(str, i, str_range)
    }
	fmt.Println(str_range[0], str_range[1] + 1)
    return s[str_range[0]: str_range[1] + 1]
}



func findLongest(str []byte, low int, str_range [2]int) int {
	// 查找中间部分
	var high = low
	for (high < len(str) - 1 && str[high + 1] == str[low]) {
		high++
	}

	// 定位中间部分的最后一个字符
	var ans = high

	// 从中间向左右扩散
	for (low > 0 && high < len(str) - 1 && str[low - 1] == str[high + 1]) {
		low--
		high++
	}

	// 记录最大长度
	if (high - low > str_range[1] - str_range[0]) {
		str_range[0] = low
		str_range[1] = high
	}
	return ans
}

func main() {
	var s = "babad"
	longestPalindrome(s)
}