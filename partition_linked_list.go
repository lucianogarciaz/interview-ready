package main

func partitionLinkedList(list *ListNode, partition int) *ListNode {
	pa := &ListNode{}
	head := pa
	pb := &ListNode{}
	headPb := pb

	if list == nil {
		return list
	}

	for list != nil {
		if list.Val < partition {
			pa.Next = &ListNode{
				Val:  list.Val,
				Next: nil,
			}
			pa = pa.Next
		}

		if list.Val >= partition {
			pb.Next = &ListNode{
				Val:  list.Val,
				Next: nil,
			}
			pb = pb.Next
		}

		list = list.Next
	}

	if head.Next != nil {
		head = head.Next
	}

	if head.Next == nil && headPb.Next != nil {
		return headPb.Next
	}

	if headPb.Next != nil {
		headPb = headPb.Next
		pa.Next = headPb
	}

	return head
}
