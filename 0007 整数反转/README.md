# 思路
## 7. 整数反转
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1：
输入：x = 123
输出：321

示例 2：
输入：x = -123
输出：-321

示例 3：
输入：x = 120
输出：21

示例 4：
输入：x = 0
输出：0
 
提示：
-2^31 <= x <= 2^31 - 1

# 思路
考虑可以使用栈的思路，先进的元素最后出来

1. 判断整数符号，并存储sign:"正数": true, "负数": false
2. 将数字转字符串，遍历，正序存到列表中
3. 逆序把数据取出， 转数字，添加符号
4. 判断数据大小，是否在限定范围内，输出数字或者0
