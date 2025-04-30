package main

// BINARY SEARCH
func searchInsert(nums []int, target int) int {
	left := 0
	right := len(nums) - 1

	for left <= right {
		pivot := (right + left) / 2
		el := nums[pivot]
		if el == target {
			return pivot
		}

		if el < target {
			left = pivot + 1
		}

		if el > target {
			right = pivot - 1
		}
	}

	return left
}
