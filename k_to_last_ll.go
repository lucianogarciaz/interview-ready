package main

// 2.  *Return Kth to Last*:

// Implement an algorithm to find the kth to last element of a singly linked list.
func kthToLastNode(root *ListNode, k int) *ListNode {
	output := root
	length := 0
	for root != nil {
		length++
		root = root.Next
	}

	if k > length {
		return nil
	}

	index := length - k
	for i := 0; i < index; i++ {
		output = output.Next
	}

	return output
}
