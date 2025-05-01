package main

// 1->2->3->4
// [1,2,3,4]

// first reverse it, lastly compare if they are equal.
func isPalindromeLinkedList(l *ListNode) bool {
	head := l
	return isEqual(head, reverseLinkedList(l))
}

func isEqual(l *ListNode, l2 *ListNode) bool {
	// what happens if the size of the lists are different?
	for l != nil || l2 != nil {
		if l.Val != l2.Val {
			return false
		}

		l = l.Next
		l2 = l2.Next
	}

	return true
}

func reverseLinkedList(l *ListNode) *ListNode {
	listInSlice := []int{}
	for l != nil {
		listInSlice = append(listInSlice, l.Val)
		l = l.Next
	}

	outputLinkedList := &ListNode{}
	head := outputLinkedList
	for i := len(listInSlice) - 1; i >= 0; i-- {
		outputLinkedList.Next = &ListNode{
			Val:  listInSlice[i],
			Next: outputLinkedList.Next,
		}

		outputLinkedList = outputLinkedList.Next
	}

	return head.Next
}
