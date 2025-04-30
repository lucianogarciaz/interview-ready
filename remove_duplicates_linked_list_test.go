package main

import "testing"

func TestRemoveDuplicatesNoBuffer(t *testing.T) {
	testCases := []struct {
		name     string
		input    *ListNode
		expected *ListNode
	}{
		{
			name: "Duplicates in the middle",
			input: &ListNode{
				Val: 1,
				Next: &ListNode{
					Val: 2,
					Next: &ListNode{
						Val: 2,
						Next: &ListNode{
							Val: 2,
							Next: &ListNode{
								Val:  4,
								Next: nil,
							},
						},
					},
				},
			},
			expected: &ListNode{
				Val: 1,
				Next: &ListNode{
					Val: 2,
					Next: &ListNode{
						Val:  4,
						Next: nil,
					},
				},
			},
		},
		{
			name: "Duplicates at the beginning",
			input: &ListNode{
				Val: 3,
				Next: &ListNode{
					Val: 3,
					Next: &ListNode{
						Val: 3,
						Next: &ListNode{
							Val:  5,
							Next: nil,
						},
					},
				},
			},
			expected: &ListNode{
				Val: 3,
				Next: &ListNode{
					Val:  5,
					Next: nil,
				},
			},
		},
		{
			name: "Duplicates at the end",
			input: &ListNode{
				Val: 1,
				Next: &ListNode{
					Val: 2,
					Next: &ListNode{
						Val: 3,
						Next: &ListNode{
							Val:  3,
							Next: nil,
						},
					},
				},
			},
			expected: &ListNode{
				Val: 1,
				Next: &ListNode{
					Val: 2,
					Next: &ListNode{
						Val:  3,
						Next: nil,
					},
				},
			},
		},
		{
			name: "No duplicates",
			input: &ListNode{
				Val: 1,
				Next: &ListNode{
					Val: 2,
					Next: &ListNode{
						Val:  3,
						Next: nil,
					},
				},
			},
			expected: &ListNode{
				Val: 1,
				Next: &ListNode{
					Val: 2,
					Next: &ListNode{
						Val:  3,
						Next: nil,
					},
				},
			},
		},
		{
			name: "All duplicates",
			input: &ListNode{
				Val: 5,
				Next: &ListNode{
					Val: 5,
					Next: &ListNode{
						Val:  5,
						Next: nil,
					},
				},
			},
			expected: &ListNode{
				Val:  5,
				Next: nil,
			},
		},
		{
			name: "Single node",
			input: &ListNode{
				Val:  7,
				Next: nil,
			},
			expected: &ListNode{
				Val:  7,
				Next: nil,
			},
		},
		{
			name:     "Empty list",
			input:    nil,
			expected: nil,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := removeDuplicatesWithBuffer(tc.input)

			// Compare the result with expected
			current := result
			expected := tc.expected

			for current != nil && expected != nil {
				if current.Val != expected.Val {
					t.Errorf("Expected value %d, got %d", expected.Val, current.Val)
				}
				current = current.Next
				expected = expected.Next
			}

			if current != nil || expected != nil {
				t.Errorf("Lists have different lengths")
			}

			result = removeDuplicatesNoBuffer(tc.input)

			// Compare the result with expected
			current = result
			expected = tc.expected

			for current != nil && expected != nil {
				if current.Val != expected.Val {
					t.Errorf("Expected value %d, got %d", expected.Val, current.Val)
				}
				current = current.Next
				expected = expected.Next
			}

			if current != nil || expected != nil {
				t.Errorf("Lists have different lengths")
			}
		})
	}
}
