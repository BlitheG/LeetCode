# 题干
## 3. 无重复字符的最长子串
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

# 思路1
1. s进入，判断s长度
2. 新列表l1, 存储字符
3. 新字符串str， 存储不重复字符串
3. 遍历字符串s
4. 判断字符是否在列表l1中，不在列表则+到str中
5. 在列表中，判断res 和len(str)， 将更大的赋值到res，并且重新截取列表和字符串

# 误区
要小心，如"dvdf"，得到结果df 而不是vdf

