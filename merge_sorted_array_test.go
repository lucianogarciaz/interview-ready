package main

import (
	"reflect"
	"testing"
)

func TestMerge(t *testing.T) {
	testCases := []struct {
		name   string
		nums1  []int
		m      int
		nums2  []int
		n      int
		expect []int
	}{
		{
			name:   "Example 1: Merge [1,2,3] and [2,5,6]",
			nums1:  []int{1, 2, 3, 0, 0, 0},
			m:      3,
			nums2:  []int{2, 5, 6},
			n:      3,
			expect: []int{1, 2, 2, 3, 5, 6},
		},
		{
			name:   "Example 2: Merge [1] and []",
			nums1:  []int{1},
			m:      1,
			nums2:  []int{},
			n:      0,
			expect: []int{1},
		},
		{
			name:   "Example 3: Merge [] and [1]",
			nums1:  []int{0},
			m:      0,
			nums2:  []int{1},
			n:      1,
			expect: []int{1},
		},
		{
			name:   "Merge [4,5,6,0,0,0] and [1,2,3]",
			nums1:  []int{4, 5, 6, 0, 0, 0},
			m:      3,
			nums2:  []int{1, 2, 3},
			n:      3,
			expect: []int{1, 2, 3, 4, 5, 6},
		},
		{
			name:   "Merge [1,2,3,0,0,0] and [4,5,6]",
			nums1:  []int{1, 2, 3, 0, 0, 0},
			m:      3,
			nums2:  []int{4, 5, 6},
			n:      3,
			expect: []int{1, 2, 3, 4, 5, 6},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			// Create a copy of nums1 to avoid modifying the original test case
			nums1Copy := make([]int, len(tc.nums1))
			copy(nums1Copy, tc.nums1)

			merge(nums1Copy, tc.m, tc.nums2, tc.n)

			if !reflect.DeepEqual(nums1Copy, tc.expect) {
				t.Errorf("merge(%v, %d, %v, %d) = %v; want %v",
					tc.nums1, tc.m, tc.nums2, tc.n, nums1Copy, tc.expect)
			}
		})
	}
}
