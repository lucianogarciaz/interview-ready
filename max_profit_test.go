package main

import "testing"

func TestMaxProfitWithoutSlidingWindow(t *testing.T) {
	testCases := []struct {
		name     string
		prices   []int
		expected int
	}{
		{
			name:     "Basic increasing prices",
			prices:   []int{1, 2, 3, 4, 5},
			expected: 4,
		},
		{
			name:     "Basic decreasing prices",
			prices:   []int{5, 4, 3, 2, 1},
			expected: 0,
		},
		{
			name:     "Empty array",
			prices:   []int{},
			expected: 0,
		},
		{
			name:     "Single price",
			prices:   []int{1},
			expected: 0,
		},
		{
			name:     "Two prices - profit",
			prices:   []int{1, 2},
			expected: 1,
		},
		{
			name:     "Two prices - no profit",
			prices:   []int{2, 1},
			expected: 0,
		},
		{
			name:     "Complex scenario",
			prices:   []int{7, 1, 5, 3, 6, 4},
			expected: 5,
		},
		{
			name:     "Multiple peaks and valleys",
			prices:   []int{3, 2, 6, 5, 0, 3},
			expected: 4,
		},
		{
			name:     "Multiple peaks and valleys",
			prices:   []int{4, 4, 6, 5, 0, 3},
			expected: 3,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := maxProfitWithoutSlidingWindow(tc.prices)
			if result != tc.expected {
				t.Errorf("maxProfitWithoutSlidingWindow(%v) = %d; want %d", tc.prices, result, tc.expected)
			}
			result = maxProfit(tc.prices)
			if result != tc.expected {
				t.Errorf("maxProfitWithoutSlidingWindow(%v) = %d; want %d", tc.prices, result, tc.expected)
			}
		})
	}
}
