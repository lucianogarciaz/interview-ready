package main

// ListNode represents a node in a linked list
type ListNode struct {
	Val  int
	Next *ListNode
}

// a := [1,2,4]
// b := [1,3,4]
// output: [1,1,2,3,4,4]
func mergeTwoLists2(list1 *ListNode, list2 *ListNode) *ListNode {
	// add the selected value from the list
	// remove the element from the selected list (move to the next node)
	// move the pointer to the next line in the outupt list
	output := &ListNode{}
	head := output
	// [1,2,4] [1,3,4]
	// val1, val2, outuput, list1, list2
	// 1, 1, [1], [1,2,4], [3,4]
	// 1,3, [1,1], [2,4], [3,4]

	for list1 != nil && list2 != nil {
		val1 := list1.Val
		val2 := list2.Val
		if val1 < val2 {
			output.Next = &ListNode{
				Val:  val1,
				Next: nil,
			}
			list1 = list1.Next
		}

		if val1 >= val2 {
			output.Next = &ListNode{
				Val:  val2,
				Next: nil,
			}

			list2 = list2.Next
		}

		output = output.Next
	}

	if list1 != nil {
		output.Next = list1
	}

	if list2 != nil {
		output.Next = list2
	}

	return head.Next
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	n := &ListNode{}
	head := n

	for list1 != nil || list2 != nil {
		if list1 == nil {
			n.Next = list2
			break
		}
		if list2 == nil {
			n.Next = list1
			break
		}

		if list1.Val < list2.Val {
			n.Next = list1
			list1 = list1.Next
		} else {
			n.Next = list2
			list2 = list2.Next
		}

		n = n.Next
	}

	return head.Next
}

func moveToNextElement(list *ListNode) *ListNode {
	return list.Next
}

func appendToTail(list *ListNode, val int) *ListNode {
	head := list
	newNode := &ListNode{
		Val:  val,
		Next: nil,
	}

	for list.Next != nil {
		list = list.Next
	}

	list.Next = newNode

	return head
}
