package main

import "testing"

func TestIsOneAway(t *testing.T) {
	testCases := []struct {
		name     string
		s1       string
		s2       string
		expected bool
	}{
		// {
		// 	name:     "Same strings",
		// 	s1:       "pale",
		// 	s2:       "pale3",
		// 	expected: true,
		// },
		// {
		// 	name:     "Same strings",
		// 	s1:       "pale",
		// 	s2:       "pale",
		// 	expected: true,
		// },
		// {
		// 	name:     "One character replaced",
		// 	s1:       "pale",
		// 	s2:       "bale",
		// 	expected: true,
		// },
		// {
		// 	name:     "One character inserted",
		// 	s1:       "pale",
		// 	s2:       "pales",
		// 	expected: true,
		// },
		{
			name:     "One character removed",
			s1:       "pales",
			s2:       "pale",
			expected: true,
		},
		{
			name:     "Two characters replaced",
			s1:       "pale",
			s2:       "bake",
			expected: false,
		},
		{
			name:     "Two characters inserted",
			s1:       "pale",
			s2:       "palest",
			expected: false,
		},
		{
			name:     "Empty strings",
			s1:       "",
			s2:       "",
			expected: true,
		},
		{
			name:     "One empty string, one single character",
			s1:       "",
			s2:       "a",
			expected: true,
		},
		{
			name:     "One empty string, multiple characters",
			s1:       "",
			s2:       "abc",
			expected: false,
		},
		{
			name:     "Case sensitive replacement",
			s1:       "Pale",
			s2:       "pale",
			expected: true,
		},
		{
			name:     "Different length strings - too many differences",
			s1:       "apple",
			s2:       "aple",
			expected: true,
		},
		{
			name:     "Different length strings - too many differences",
			s1:       "apple",
			s2:       "aptitude",
			expected: false,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := isOneAway(tc.s1, tc.s2)
			if result != tc.expected {
				t.Errorf("isOneAway(%q, %q) = %v; want %v", tc.s1, tc.s2, result, tc.expected)
			}
		})
	}
}
