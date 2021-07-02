#!python3
#-*- coding: utf-8 -*-
"""
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

示例 3：
输入：s = "a"
输出："a"

示例 4：
输入：s = "ac"
输出："a"

提示：
1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成
"""
class Solution:
    def longestPalindrome(self, test_str: str) -> str:
        """
        leetcode 给出结果超过限制
        """
        if len(test_str) == 1:
            return test_str
        str_dict = dict()
        hw_str = ""
        for index, item in enumerate(test_str):
            if item in str_dict.values():
                str_dict[index] = item
                print(str_dict)
                tmp_hw_str = ""
                # 遍历字典检查回文数据
                for key, value in str_dict.items():
                    if not tmp_hw_str:
                        if item == value:
                            count = 0
                            is_hw = True
                            while (key + count) < (index - count):
                                print(count, key, index)
                                if str_dict[key + count] != str_dict[index - count]:
                                    is_hw = False
                                    break 
                                else:
                                    count += 1
                            if is_hw:
                                tmp_hw_str = test_str[key:index+1]
                                print(tmp_hw_str)
                    else:
                        if len(hw_str) <= len(tmp_hw_str):
                            hw_str = tmp_hw_str
            else:      
                str_dict[index] = item
        if not hw_str:
            return test_str[0]
        print(hw_str)
        return hw_str
                
    def longestPalindrome1(self, test_str: str) -> str:
        print(test_str)
        if len(test_str) == 1:
            return test_str
        elif len(test_str) == 2:
            if test_str[0] == test_str[1]:
                return test_str
            else:
                return test_str[0]
        else:
            copy_str = test_str
            huiwen_str =""
            longest_str = ""
            count = 0
            for index, item in enumerate(test_str):
                # 查找回文的中点, 进行回文验证：
                #     1. 偶数长回文 "abccba"
                #     2. 奇数长回文 "abcdcba"
                #     3. "abcccba"
                #     4. "saaaaaaaas"
                if (index-1) >=0 and (index+1) < len(copy_str) and item == copy_str[index-1] == copy_str[index+1]:
                    huiwen_str = copy_str[index-1: index+2]
                    count = 1
                    while item == copy_str[index-count]:
                        start = index - count
                        count += 1
                        if index-count < 0:
                            break
                    count = 1
                    while item == copy_str[index+count]:
                        end = index + count
                        count += 1
                        if index+count >= len(copy_str):
                            break
                    # 取到所有相同的字符串
                    huiwen_str = copy_str[start:end+1]
                    count = 1
                    while (start - count) >= 0 and (end + count) < len(copy_str):
                        if copy_str[start-count] == copy_str[end+count]:
                            huiwen_str = copy_str[(start-count):(end+count+1)]
                            count += 1
                        else:
                            break

                elif (index-1) >= 0 and item == copy_str[index-1]:
                    huiwen_str = copy_str[index-1:index+1]
                    count = 2
                    while (index - count) >= 0 and (index + count -1) < len(copy_str):
                        if copy_str[index - count] == copy_str[index + count - 1]:
                            huiwen_str = copy_str[(index - count): (index + count)]
                            count += 1
                        else:
                            break
                elif (index-2) >= 0 and item == copy_str[index-2]:
                    huiwen_str = copy_str[index-2:index+1]
                    count = 3
                    while (index - count) >= 0 and (index + count - 2) < len(copy_str):
                        if copy_str[index - count] == copy_str[index + count - 2]:
                            huiwen_str = copy_str[(index - count): (index + count -1)]
                            count += 1
                        else:
                            break
                else:
                    huiwen_str = copy_str[0]
                if len(longest_str) <= len(huiwen_str):
                    longest_str = huiwen_str

            return longest_str


if __name__ == '__main__':
    s = "abccba"
    target = "abccba"
    assert(Solution().longestPalindrome1(s) == target)
    s = "abcdcba"
    target = "abcdcba"
    assert(Solution().longestPalindrome1(s) == target)
    s = "babababd"
    target = "bababab"
    assert(Solution().longestPalindrome1(s) == target)
    s = "sooos"
    target = "sooos"
    assert(Solution().longestPalindrome1(s) == target)
