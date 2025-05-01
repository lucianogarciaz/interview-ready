package main

// 1-2-3-4-2-3-4
func detectCycle(l *ListNode) *ListNode {
	hashMap := map[*ListNode]bool{}
	for l != nil {
		if _, ok := hashMap[l]; ok {
			return l
		}
		hashMap[l] = true
		l = l.Next
	}

	return l
}

// When you need to find some elements:
// first always try to think a way with a hasmMap
// secondly with nested for loops
