#!python3
# -*- coding: utf-8 -*-


"""
7. 整数反转
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
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        elif x < 0:
            sign = "min"
            x = x * -1
        else:
            sign = "plus"
        
        # 建立一个栈机制的列表
        warehouse = list()
        for sbyte in str(x):
            warehouse.append(sbyte)
        
        # 逆序取出
        index = 1
        new_num = ""
        while index <= len(warehouse):
            new_num = new_num + warehouse[-index]
            index += 1
        
        if sign == 'min':
            new_num = 0 - int(new_num)
        else:
            new_num = int(new_num)
        
        if -2**31 < new_num < 2**31-1:
            return new_num
        else:
            return 0


if __name__ == '__main__':
    x1 = 123
    target1 = 321
    assert(Solution().reverse(x1) == target1)
    x2 = -123
    target2 = -321
    assert(Solution().reverse(x2) == target2)
    x3 = 120
    target3 = 21
    assert(Solution().reverse(x3) == target3)
    x4 = 0
    target4 = 0
    assert(Solution().reverse(x4) == target4)