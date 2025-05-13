package main

import (
	"testing"
)

func TestExist(t *testing.T) {
	tests := []struct {
		name     string
		board    [][]byte
		word     string
		expected bool
	}{
		{
			name: "large board with long word",
			board: [][]byte{
				{'A', 'A', 'A', 'A', 'A', 'A'},
				{'A', 'A', 'A', 'A', 'A', 'A'},
				{'A', 'A', 'A', 'A', 'A', 'A'},
				{'A', 'A', 'A', 'A', 'A', 'A'},
				{'A', 'A', 'A', 'A', 'A', 'A'},
				{'A', 'A', 'A', 'A', 'A', 'A'},
			},
			word:     "AAAAAAAAAAAAAAa",
			expected: false,
		},
		{
			name: "vertical word",
			board: [][]byte{
				{'b'},
				{'a'},
				{'b'},
				{'b'},
				{'a'},
			},
			word:     "baa",
			expected: false,
		},
		{
			name: "standard board with valid word",
			board: [][]byte{
				{'A', 'B', 'C', 'E'},
				{'S', 'F', 'C', 'S'},
				{'A', 'D', 'E', 'E'},
			},
			word:     "ABCCED",
			expected: true,
		},
		{
			name: "standard board with another valid word",
			board: [][]byte{
				{'A', 'B', 'C', 'E'},
				{'S', 'F', 'C', 'S'},
				{'A', 'D', 'E', 'E'},
			},
			word:     "SEE",
			expected: true,
		},
		{
			name: "standard board with invalid word",
			board: [][]byte{
				{'A', 'B', 'C', 'E'},
				{'S', 'F', 'C', 'S'},
				{'A', 'D', 'E', 'E'},
			},
			word:     "ABCB",
			expected: false,
		},
		{
			name: "single cell board with invalid word",
			board: [][]byte{
				{'a'},
			},
			word:     "ab",
			expected: false,
		},
		{
			name: "single cell board with valid word",
			board: [][]byte{
				{'a'},
			},
			word:     "a",
			expected: true,
		},
		{
			name: "horizontal word",
			board: [][]byte{
				{'a', 'b'},
			},
			word:     "ba",
			expected: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := exist(tt.board, tt.word)
			if result != tt.expected {
				t.Errorf("exist() = %v; want %v for board %v and word %q",
					result, tt.expected, tt.board, tt.word)
			}
		})
	}
}
