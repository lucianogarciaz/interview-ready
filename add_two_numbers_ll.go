package main

import (
	"fmt"
	"math/big"
	"strconv"
)

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	num1 := ""
	for l1 != nil {
		num1 = fmt.Sprintf("%d%s", l1.Val, string(num1))
		l1 = l1.Next
	}
	num2 := ""
	for l2 != nil {
		num2 = fmt.Sprintf("%d%s", l2.Val, num2)
		l2 = l2.Next
	}

	a := new(big.Int)
	b := new(big.Int)
	a.SetString(num1, 10)
	b.SetString(num2, 10)
	result := new(big.Int).Add(a, b)

	rLn := &ListNode{}
	head := rLn
	str := fmt.Sprintf("%d", result)
	for i := len(str) - 1; i >= 0; i-- {
		val, _ := strconv.Atoi(string(str[i]))
		rLn.Next = &ListNode{
			Val: val,
		}
		rLn = rLn.Next
	}

	return head.Next
}
