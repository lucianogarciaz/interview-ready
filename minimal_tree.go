package main

// [1,2,3,4,5,6,7,8]
// marked = 4
// childs: left: 5 + 0 / 2 = 2   right: 5+ 9 /2:  7
func createMinimalBST(a []int) *TreeNode {
	if len(a) == 0 {
		return nil
	}
	if len(a) == 1 {
		return &TreeNode{
			Val: a[0],
		}
	}

	pivot := (len(a) - 1) / 2
	//BECAREFUL ON HOW TO USE INDEXES WHEN REARRENGING ELEMENTS IN GO
	leftSlice := a[0:pivot]
	rightSlice := a[pivot+1:]

	left := createMinimalBST(leftSlice)
	right := createMinimalBST(rightSlice)

	return &TreeNode{
		Val:   a[pivot],
		Left:  left,
		Right: right,
	}
}
