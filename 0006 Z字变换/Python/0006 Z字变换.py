#!python3
#-*- coding: utf-8 -*-
"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
            P   A   H   N
            A P L S I I G
            Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);
 

示例 1：
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

示例 3：
输入：s = "A", numRows = 1
输出："A"

提示：
1 <= s.length <= 1000
s 由英文字母（小写和大写）、',' 和 '.' 组成
1 <= numRows <= 1000
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 特殊情况
        if len(s) == 1 or numRows == 1:
            return s
        elif numRows == 2:
            str_tmp1 = str_tmp2 = ""
            for index, sbyte in enumerate(s):
                if (index % 2) == 0:
                    str_tmp1 += sbyte
                else:
                    str_tmp2 += sbyte
            return (str_tmp1+str_tmp2)
        else:
            all_list = dict()
            # numRows 为几就生成几个列表
            for i in range(numRows):
                all_list[i] = list()
            

            # 根据需求在列表中添加字符
            count = 0
            # True | False = add | min
            add_or_min = True
            for sbyte in s:
                if count >= numRows:
                    add_or_min = False
                    count -= 2
                
                if add_or_min:
                    all_list[count].append(sbyte)
                    count += 1
                else:
                    all_list[count].append(sbyte)
                    count -= 1
                
                if count == -1:
                    add_or_min = True
                    count = 1
            # print(all_list)

            # 重组字符串
            new_str = ""
            for j in range(numRows):
                new_str += "".join(all_list[j])
        return new_str


if __name__ == '__main__':
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    target1 = "PAHNAPLSIIGYIR"
    assert(Solution().convert(s1, numRows1) == target1)
    s2 = "PAYPALISHIRING"
    numRows2 = 4
    target2 = "PINALSIGYAHRPI"
    assert(Solution().convert(s2, numRows2) == target2)
    