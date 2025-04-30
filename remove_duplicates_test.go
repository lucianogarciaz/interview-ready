package main

import (
	"reflect"
	"sort"
	"testing"
)

func TestRemoveDuplicates(t *testing.T) {
	testCases := []struct {
		name           string
		nums           []int
		expectedK      int
		expectedNums   []int
		expectedLength int
	}{
		{
			name:           "Example 1: Basic case with few duplicates",
			nums:           []int{1, 1, 2},
			expectedK:      2,
			expectedNums:   []int{1, 2},
			expectedLength: 3,
		},
		{
			name:           "Example 2: Multiple duplicates",
			nums:           []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4},
			expectedK:      5,
			expectedNums:   []int{0, 1, 2, 3, 4},
			expectedLength: 10,
		},
		{
			name:           "Empty array",
			nums:           []int{},
			expectedK:      0,
			expectedNums:   []int{},
			expectedLength: 0,
		},
		{
			name:           "Array with no duplicates",
			nums:           []int{1, 2, 3, 4, 5},
			expectedK:      5,
			expectedNums:   []int{1, 2, 3, 4, 5},
			expectedLength: 5,
		},
		{
			name:           "Array with all duplicates",
			nums:           []int{1, 1, 1, 1, 1},
			expectedK:      1,
			expectedNums:   []int{1},
			expectedLength: 5,
		},
		{
			name:           "Array with duplicates at the end",
			nums:           []int{1, 2, 3, 4, 4, 4},
			expectedK:      4,
			expectedNums:   []int{1, 2, 3, 4},
			expectedLength: 6,
		},
		{
			name:           "Array with duplicates at the beginning",
			nums:           []int{1, 1, 1, 2, 3, 4},
			expectedK:      4,
			expectedNums:   []int{1, 2, 3, 4},
			expectedLength: 6,
		},
		{
			name:           "Single element array",
			nums:           []int{5},
			expectedK:      1,
			expectedNums:   []int{5},
			expectedLength: 1,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			// Create a copy of the input array to avoid modifying the test case
			nums := make([]int, len(tc.nums))
			copy(nums, tc.nums)

			// Call the function to test
			k := removeDuplicates(nums)

			// Check if the returned k is correct
			if k != tc.expectedK {
				t.Errorf("removeDuplicates() returned k = %v, want %v", k, tc.expectedK)
			}

			// Check if the first k elements are correct
			if !reflect.DeepEqual(nums[:k], tc.expectedNums) {
				t.Errorf("First %d elements = %v, want %v", k, nums[:k], tc.expectedNums)
			}

			// Check if the length of the array is preserved
			if len(nums) != tc.expectedLength {
				t.Errorf("Array length changed: got %d, want %d", len(nums), tc.expectedLength)
			}
		})
	}
}

func TestRemoveElement(t *testing.T) {
	testCases := []struct {
		name           string
		nums           []int
		val            int
		expectedK      int
		expectedNums   []int
		expectedLength int
	}{
		{
			name:           "Example 1: Remove value 3",
			nums:           []int{3, 2, 2, 3},
			val:            3,
			expectedK:      2,
			expectedNums:   []int{2, 2},
			expectedLength: 4,
		},
		{
			name:           "Example 2: Remove value 2",
			nums:           []int{0, 1, 2, 2, 3, 0, 4, 2},
			val:            2,
			expectedK:      5,
			expectedNums:   []int{0, 1, 3, 0, 4},
			expectedLength: 8,
		},
		{
			name:           "Empty array",
			nums:           []int{},
			val:            1,
			expectedK:      0,
			expectedNums:   []int{},
			expectedLength: 0,
		},
		{
			name:           "Array with all elements equal to val",
			nums:           []int{5, 5, 5, 5},
			val:            5,
			expectedK:      0,
			expectedNums:   []int{},
			expectedLength: 4,
		},
		{
			name:           "Array with no elements equal to val",
			nums:           []int{1, 2, 3, 4},
			val:            5,
			expectedK:      4,
			expectedNums:   []int{1, 2, 3, 4},
			expectedLength: 4,
		},
		{
			name:           "Single element array equal to val",
			nums:           []int{7},
			val:            7,
			expectedK:      0,
			expectedNums:   []int{},
			expectedLength: 1,
		},
		{
			name:           "Single element array not equal to val",
			nums:           []int{7},
			val:            8,
			expectedK:      1,
			expectedNums:   []int{7},
			expectedLength: 1,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			// Create a copy of the input array to avoid modifying the test case
			nums := make([]int, len(tc.nums))
			copy(nums, tc.nums)

			// Call the function to test
			k := removeElement(nums, tc.val)

			// Check if the returned k is correct
			if k != tc.expectedK {
				t.Errorf("removeElement() returned k = %v, want %v", k, tc.expectedK)
			}

			// Check if the first k elements contain the expected values (in any order)
			if k > 0 {
				// Sort both slices to compare regardless of order
				actualElements := make([]int, k)
				copy(actualElements, nums[:k])
				sort.Ints(actualElements)

				expectedElements := make([]int, len(tc.expectedNums))
				copy(expectedElements, tc.expectedNums)
				sort.Ints(expectedElements)

				if !reflect.DeepEqual(actualElements, expectedElements) {
					t.Errorf("First %d elements = %v, want %v", k, nums[:k], tc.expectedNums)
				}
			}

			// Check if the length of the array is preserved
			if len(nums) != tc.expectedLength {
				t.Errorf("Array length changed: got %d, want %d", len(nums), tc.expectedLength)
			}
		})
	}
}
