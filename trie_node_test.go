package main

import "testing"

func TestTrie(t *testing.T) {
	tests := []struct {
		name       string
		operations []string
		inputs     []string
		expected   []interface{}
	}{
		{
			name:       "Example 1",
			operations: []string{"Trie", "insert", "search", "search", "startsWith", "insert", "search"},
			inputs:     []string{"", "apple", "apple", "app", "app", "app", "app"},
			expected:   []interface{}{nil, nil, true, false, true, nil, true},
		},
		{
			name:       "Empty Trie",
			operations: []string{"Trie", "search", "startsWith"},
			inputs:     []string{"", "apple", "app"},
			expected:   []interface{}{nil, false, false},
		},
		{
			name:       "Multiple Words",
			operations: []string{"Trie", "insert", "insert", "insert", "search", "search", "startsWith"},
			inputs:     []string{"", "apple", "app", "application", "app", "application", "appl"},
			expected:   []interface{}{nil, nil, nil, nil, true, true, true},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			var trie *Trie
			for i, op := range tt.operations {
				switch op {
				case "Trie":
					trie = &Trie{root: &TrieNode{child: make(map[rune]*TrieNode)}}
				case "insert":
					trie.Insert(tt.inputs[i])
				case "search":
					result := trie.Search(tt.inputs[i])
					if result != tt.expected[i] {
						t.Errorf("Search(%q) = %v, want %v", tt.inputs[i], result, tt.expected[i])
					}
				case "startsWith":
					result := trie.StartsWith(tt.inputs[i])
					if result != tt.expected[i] {
						t.Errorf("StartsWith(%q) = %v, want %v", tt.inputs[i], result, tt.expected[i])
					}
				}
			}
		})
	}
}
