package main

import (
    "fmt"
)

/*
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
*/



// Definition for singly-linked list.
type ListNode struct {
     Val int
     Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    // 需要注意结构体中指针的操作容易导致指针值和地址的混乱
    var list_node =  &ListNode{0, nil}
    var list_node_r = list_node
    var x, y, s, carry int

    for (l1 != nil || l2 != nil) {
        if (l1 != nil) {
            x = l1.Val
        } else {
            x = 0
        }

        if (l2 != nil) {
            y = l2.Val
        } else {
            y = 0
        }

        s = carry + x + y
        carry = s / 10
        list_node_r.Next = &ListNode{s % 10, nil}
        list_node_r = list_node_r.Next

        if (l1 != nil) {
            l1 = l1.Next
        }
        if (l2 != nil) {
            l2 = l2.Next
        }
    }
    if (carry > 0) {
        list_node_r.Next = &ListNode{1, nil}
    }
    return list_node.Next
}


func main() {
    l1 := ListNode{
        Val: 2,
        Next: &ListNode{
            Val: 4,
            Next: &ListNode{
                Val: 3,
                Next: nil,
            },
        },
    }
    l2 := ListNode{
        Val: 5,
        Next: &ListNode{
            Val: 6,
            Next: &ListNode{
                Val: 4,
                Next: nil,
            },
        },
    }
    res := addTwoNumbers(&l1, &l2)
    fmt.Println(res)

}