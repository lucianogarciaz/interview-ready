package main

import "testing"

func TestCountBrokenTags(t *testing.T) {
	tests := []struct {
		name     string
		tags     string
		expected int
	}{
		{
			name:     "empty string",
			tags:     "",
			expected: 0,
		},
		{
			name:     "valid tags",
			tags:     "Something really okay. <app>with something in here <app> and something else</app> blabla </app>",
			expected: 0,
		},
		{
			name:     "one broken tag",
			tags:     "<app><app></app>",
			expected: 1,
		},
		{
			name:     "multiple broken tags",
			tags:     "<app><app><app></app>",
			expected: 2,
		},
		{
			name:     "complex nested tags",
			tags:     "<app><app></app><app></app></app>",
			expected: 0,
		},
		{
			name:     "complex nested broken tags",
			tags:     "<app><app></app><app><app></app>",
			expected: 2,
		},
		{
			name:     "unclosed tags at end",
			tags:     "<app><app><app>",
			expected: 3,
		},
		{
			name:     "mismatched tags",
			tags:     "<app></app><app>",
			expected: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := countBrokenTags(tt.tags)
			if result != tt.expected {
				t.Errorf("countBrokenTags(%q) = %d; want %d", tt.tags, result, tt.expected)
			}
		})
	}
}
