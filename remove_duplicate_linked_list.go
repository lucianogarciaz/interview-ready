package main

func deleteDuplicatesLinkedList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	current := head.Next
	previous := head

	for current != nil {
		if current.Val == previous.Val {
			previous.Next = nil
			current = current.Next
			continue
		}

		previous.Next = current
		previous = previous.Next
		current = current.Next
	}

	return head
}
