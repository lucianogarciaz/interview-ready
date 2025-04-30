package main

import "testing"

func TestStringRotation(t *testing.T) {
	testCases := []struct {
		name     string
		s1       string
		s2       string
		expected bool
	}{
		{
			name:     "Rotation example",
			s1:       "waterbottle",
			s2:       "erbottlewat",
			expected: true,
		},
		{
			name:     "Same string",
			s1:       "hello",
			s2:       "hello",
			expected: true,
		},
		{
			name:     "Empty strings",
			s1:       "",
			s2:       "",
			expected: true,
		},
		{
			name:     "Different lengths",
			s1:       "hello",
			s2:       "helloworld",
			expected: false,
		},
		{
			name:     "Not a rotation",
			s1:       "hello",
			s2:       "ollhe",
			expected: false,
		},
		{
			name:     "Rotation with repeated characters",
			s1:       "aabbaabb",
			s2:       "abbaabba",
			expected: true,
		},
		{
			name:     "Different strings with same length",
			s1:       "abcde",
			s2:       "edcba",
			expected: false,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := stringRotation(tc.s1, tc.s2)
			if result != tc.expected {
				t.Errorf("stringRotation(%q, %q) = %v, want %v", tc.s1, tc.s2, result, tc.expected)
			}
		})
	}
}
