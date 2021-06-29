#!python3
#-*- coding: utf-8 -*-
"""
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

示例 4:
输入: s = ""
输出: 0
 

提示：
0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s:str) -> int:
        """
        执行用时：72 ms
        内存消耗：14.9 MB
        """
        char_list = list()
        char_str = ""
        tmp_length = 0
        for item in s:
            if item in char_list:
                tmp_length = max(len(char_list), tmp_length)
                char_list = char_list[char_list.index(item)+1:]
                char_str = char_str[char_str.index(item)+1:]
            char_list.append(item)
            char_str = char_str + item

        res = max(len(char_list), tmp_length)
        return res


    def lengthOfLongestSubstring2(self, s):
        """
        leetcode 上的一个很有意思的思路
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans


if __name__ == '__main__':
    s = "abcabcbb"
    assert(Solution().lengthOfLongestSubstring(s) == 3)
    s = "dvdf"
    assert(Solution().lengthOfLongestSubstring(s) == 3)
