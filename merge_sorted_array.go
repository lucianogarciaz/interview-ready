package main

import (
	"sort"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	if n == 0 {
		return
	}

	if m == 0 {
		copy(nums1, nums2)
		return
	}

	for i, v2 := range nums2 {
		left := 0
		right := m + i - 1
		var pivot int
		for left <= right {
			pivot = (left + right) / 2
			v1 := nums1[pivot]
			if v1 == v2 {
				break
			}

			if v1 < v2 {
				left = pivot + 1
				continue
			}

			if v1 > v2 {
				right = pivot - 1
			}
		}
		if nums1[pivot] < v2 {
			pivot += 1
		}

		copy(nums1[pivot+1:], nums1[pivot:])
		nums1[pivot] = v2
	}
}

func merge2(nums1 []int, m int, nums2 []int, n int) {
	copy(nums1[m:], nums2)

	sort.Slice(nums1, func(a int, b int) bool {
		return nums1[a] < nums1[b]
	})
}
