package main

import (
	"fmt"
	"strconv"
)

func sumLists(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil && list2 == nil {
		return nil
	}

	num1Str := ""
	num2Str := ""
	for list1 != nil {
		num1Str = fmt.Sprintf("%d%s", list1.Val, num1Str)
		list1 = list1.Next
	}

	for list2 != nil {
		num2Str = fmt.Sprintf("%d%s", list2.Val, num2Str)
		list2 = list2.Next
	}

	num1, _ := strconv.Atoi(num1Str)
	num2, _ := strconv.Atoi(num2Str)

	sum := num1 + num2
	sumToStr := strconv.Itoa(sum)
	sumList := &ListNode{}
	head := sumList
	for i := len(sumToStr) - 1; i >= 0; i-- {
		intNum, _ := strconv.Atoi(string(sumToStr[i]))

		sumList.Next = &ListNode{
			Val: intNum,
		}

		sumList = sumList.Next
	}

	return head.Next
}
