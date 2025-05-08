package main

import "testing"

func TestMapSum(t *testing.T) {
	tests := []struct {
		name       string
		operations []string
		inputs     [][]interface{}
		expected   []interface{}
	}{
		{
			name:       "Example 1",
			operations: []string{"MapSum", "insert", "sum", "insert", "sum"},
			inputs:     [][]interface{}{{}, {"apple", 3}, {"ap"}, {"app", 2}, {"ap"}},
			expected:   []interface{}{nil, nil, 3, nil, 5},
		},
		{
			name:       "Example 2",
			operations: []string{"MapSum", "insert", "insert", "sum", "insert", "sum"},
			inputs:     [][]interface{}{{}, {"apple", 3}, {"app", 2}, {"ap"}, {"apple", 2}, {"ap"}},
			expected:   []interface{}{nil, nil, nil, 5, nil, 4},
		},
		{
			name:       "Empty Prefix",
			operations: []string{"MapSum", "insert", "insert", "sum"},
			inputs:     [][]interface{}{{}, {"apple", 3}, {"app", 2}, {""}},
			expected:   []interface{}{nil, nil, nil, 5},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			var mapSum *MapSum
			for i, op := range tt.operations {
				switch op {
				case "MapSum":
					mapSum = &MapSum{
						root: &MapSumNode{
							child: make(map[rune]*MapSumNode),
							sum:   0,
						},
						keyToValue: make(map[string]int),
					}
				case "insert":
					key := tt.inputs[i][0].(string)
					val := tt.inputs[i][1].(int)
					mapSum.Insert(key, val)
				case "sum":
					prefix := tt.inputs[i][0].(string)
					result := mapSum.Sum(prefix)
					if result != tt.expected[i] {
						t.Errorf("Sum(%q) = %v, want %v", prefix, result, tt.expected[i])
					}
				}
			}
		})
	}
}
