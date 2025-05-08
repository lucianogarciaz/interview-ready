package main

import "fmt"

type MapSumNode struct {
	child map[rune]*MapSumNode
	sum   int
}

type MapSum struct {
	root       *MapSumNode
	keyToValue map[string]int
}

func Constructor() MapSum {
	return MapSum{
		root: &MapSumNode{
			child: make(map[rune]*MapSumNode),
			sum:   0,
		},
		keyToValue: make(map[string]int),
	}
}

func (m *MapSum) Insert(key string, val int) {
	pointer := m.root
	pSum, ok := m.keyToValue[key]
	if ok {
		m.keyToValue[key] = val
		val = val - pSum
	}

	if !ok {
		m.keyToValue[key] = val
	}

	for _, v := range key {
		_, ok = pointer.child[v]
		if !ok {
			pointer.child[v] = &MapSumNode{
				child: make(map[rune]*MapSumNode),
				sum:   0,
			}
		}
		pointer.sum += val
		pointer = pointer.child[v]
	}

	pointer.sum += val
	fmt.Printf("\n\n")
}

func (m *MapSum) Sum(prefix string) int {
	pointer := m.root

	for _, v := range prefix {
		_, ok := pointer.child[v]
		if !ok {
			return 0
		}

		pointer = pointer.child[v]
	}

	return pointer.sum
}
