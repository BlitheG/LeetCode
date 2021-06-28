#!python3
#-*- coding: utf-8 -*-
"""
2. 两数之和

给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

提示：
每个链表中的节点数在范围 [1, 100] 内   
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
 """

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print("l1: ", l1.val, l1.next)
        print("l2: ", l2.val, l2.next)
        if isinstance(l1.next, ListNode) and isinstance(l2.next, ListNode):
            pre_val = l1.val + l2.val
            if pre_val >= 10:
                pre_val = pre_val - 10
                if isinstance(l1.next, ListNode):
                    next_val = self.upgrade_ListNode(l1.next, 1)
                    return ListNode(val=pre_val, next=self.addTwoNumbers(next_val, l2.next))
                else:
                    next_val = self.upgrade_ListNode(l2.next, 1)
                    return ListNode(val=pre_val, next=self.addTwoNumbers(next_val, l2.next))
            else:
                return ListNode(val=pre_val, next=self.addTwoNumbers(l1.next, l2.next))

        elif isinstance(l1.next, ListNode):
            pre_val = l1.val + l2.val
            if pre_val >= 10:
                pre_val = pre_val - 10
                next_val = self.upgrade_ListNode(l1.next, 1)
                return ListNode(val=pre_val, next=next_val)
            else:
                tmp_val = l1.next.val + l2.next
                if tmp_val >= 10:
                    tmp_val = tmp_val - 10
                    tmp_list_node = ListNode(val=tmp_val, next=self.upgrade_ListNode(l1.next.next, 1))
                else:
                    tmp_list_node = ListNode(val=tmp_val, next=l1.next.next)
                return ListNode(val=pre_val, next=tmp_list_node)

        elif isinstance(l2.next, ListNode):
            pre_val = l1.val + l2.val
            if pre_val >= 10:
                pre_val = pre_val - 10
                next_val = self.upgrade_ListNode(l2.next, 1)
                return ListNode(val=pre_val, next=next_val)
            else:
                tmp_val = l1.next + l2.next.val
                if tmp_val >= 10:
                    tmp_val = tmp_val - 10
                    tmp_list_node = ListNode(val=tmp_val, next=self.upgrade_ListNode(l2.next.next, 1))
                else:
                    tmp_list_node = ListNode(val=tmp_val, next=l2.next.next)
                return ListNode(val=pre_val, next=tmp_list_node)

        else:
            pre_val = l1.val + l2.val
            if pre_val >= 10:
                pre_val = pre_val - 10
                next_val = l1.next + l2.next + 1
                if next_val >= 10:
                    next_val = ListNode(val=0, next=1)
            else:
                next_val = l1.next + l2.next
                if next_val >= 10:
                    next_val = ListNode(val=0, next=1)
            return ListNode(val=pre_val, next=next_val)


    
    def upgrade_ListNode(self, list_node: ListNode, is_over=0) -> ListNode:
        if list_node.val + is_over >= 10:
            if isinstance(list_node.next, ListNode):
                # ListNode(val = 9, next = ListNode(val = 9, next = 9))
                list_node = ListNode(val=0, next=self.upgrade_ListNode(list_node.next, 1))
            elif list_node.next + is_over >= 10:
                # ListNode(val = 9, next = 9)
                list_node = ListNode(val=0, next=ListNode(val=0, next=1))
            else:
                # ListNode(val = 9, next = 7)
                list_node = ListNode(val=0, next=list_node.next+1)
        else:
            # ListNode(val = 8, next = ListNode(val = 9, next = 9))
            list_node = ListNode(val=list_node.val+is_over, next=list_node.next)
        return list_node
         


def ListToListNode(l: list) -> ListNode:
    """
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    len(l) = 9
    l[9-1] = 9
    l[9-2] = 8
    """
    list_length= len(l)
    if list_length <= 1:
        list_node = ListNode(val=0, next=0)
    else:
        list_node = ListNode(val=l[list_length-2], next=l[list_length-1])
        count = 2
        while list_length - count > 0:
            count += 1
            list_node = ListNode(val=l[list_length-count], next=list_node)
    return list_node

def ListNodeToList(list_node: ListNode) -> list:
    l = list()
    l.append(list_node.val)
    while isinstance(list_node.next, ListNode):
        list_node = list_node.next
        l.append(list_node.val)
    if list_node.next != 0:
        l.append(list_node.next)
    print(l)
    return l

def testSolution(l1:list, l2:list, target:list) -> bool:
    list_node_l1 = ListToListNode(l1)
    list_node_l2 = ListToListNode(l2)
    assert (ListNodeToList(Solution().addTwoNumbers(list_node_l1, list_node_l2)) == target)


if __name__ == "__main__":
    l1 = [0]
    l2 = [0]
    target = [0]
    list_node_l1 = ListToListNode(l1)
    list_node_l2 = ListToListNode(l2)
    assert (ListNodeToList(Solution().addTwoNumbers(list_node_l1, list_node_l2)) == target)
    l1 = [2,4,3]
    l2 = [5,6,4]
    target = [7,0,8]
    list_node_l1 = ListToListNode(l1)
    list_node_l2 = ListToListNode(l2)
    assert (ListNodeToList(Solution().addTwoNumbers(list_node_l1, list_node_l2)) == target)

    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    target = [8,9,9,9,0,0,0,1]
    list_node_l1 = ListToListNode(l1)
    list_node_l2 = ListToListNode(l2)
    assert (ListNodeToList(Solution().addTwoNumbers(list_node_l1, list_node_l2)) == target)
