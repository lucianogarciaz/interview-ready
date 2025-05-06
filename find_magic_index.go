package main

// [ -1, 1, 2, 3, 4]

// array 				left 	right   pivot   value
// [-1, 0, 1, 2, 4]	 	0        4       2 		 1
// [-1,0,1,2,4]				0		 1
func findMagicIndex(arr []int) int {
	if len(arr) == 0 {
		return -1
	}

	return findMagicIndexWithIndexes(arr, 0, len(arr)-1)
}

func findMagicIndexWithIndexes(arr []int, left, right int) int {
	if left > right {
		return -1
	}

	pivot := (left + right) / 2
	if arr[pivot] == pivot {
		return pivot
	}

	if arr[pivot] < pivot {
		return findMagicIndexWithIndexes(arr, pivot+1, right)
	}

	return findMagicIndexWithIndexes(arr, left, pivot-1)
}
