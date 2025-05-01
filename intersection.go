package main

// O(n2)
func findIntersection(l1 *ListNode, l2 *ListNode) *ListNode {
	for l1 != nil && l2 != nil {
		linner := l2
		for linner != nil {
			if l1 == linner {
				return l1
			}
			linner = linner.Next
		}
		l2 = l2.Next
		l1 = l1.Next
	}

	return nil
}

// O(n)
func findIntersection2(l1, l2 *ListNode) *ListNode {
	hashMap := map[*ListNode]bool{}
	for l1 != nil {
		hashMap[l1] = true
		l1 = l1.Next
	}

	for l2 != nil {
		if _, ok := hashMap[l2]; ok {
			return l2
		}

		l2 = l2.Next
	}

	return nil
}
