package main

import (
	"testing"
)

func TestHasRoute(t *testing.T) {
	// Test case 1: Direct connection
	t.Run("direct connection", func(t *testing.T) {
		node1 := &GraphNodes{Val: 1}
		node2 := &GraphNodes{Val: 2}
		node1.Neighbors = []*GraphNodes{node2}

		if !hasRoute(node1, node2) {
			t.Error("Expected route between directly connected nodes")
		}
	})

	// Test case 2: Indirect connection
	t.Run("indirect connection", func(t *testing.T) {
		node1 := &GraphNodes{Val: 1}
		node2 := &GraphNodes{Val: 2}
		node3 := &GraphNodes{Val: 3}
		node1.Neighbors = []*GraphNodes{node2}
		node2.Neighbors = []*GraphNodes{node3}

		if !hasRoute(node1, node3) {
			t.Error("Expected route between indirectly connected nodes")
		}
	})

	// Test case 3: No connection
	t.Run("no connection", func(t *testing.T) {
		node1 := &GraphNodes{Val: 1}
		node2 := &GraphNodes{Val: 2}
		node3 := &GraphNodes{Val: 3}
		node1.Neighbors = []*GraphNodes{node2}

		if hasRoute(node1, node3) {
			t.Error("Expected no route between unconnected nodes")
		}
	})

	// Test case 4: Circular connection
	t.Run("circular connection", func(t *testing.T) {
		node1 := &GraphNodes{Val: 1}
		node2 := &GraphNodes{Val: 2}
		node3 := &GraphNodes{Val: 3}
		node1.Neighbors = []*GraphNodes{node2}
		node2.Neighbors = []*GraphNodes{node3}
		node3.Neighbors = []*GraphNodes{node1}

		if !hasRoute(node1, node3) {
			t.Error("Expected route between nodes in circular connection")
		}
	})

	// Test case 5: Self-loop
	t.Run("self loop", func(t *testing.T) {
		node1 := &GraphNodes{Val: 1}
		node1.Neighbors = []*GraphNodes{node1}

		if !hasRoute(node1, node1) {
			t.Error("Expected route in self-loop case")
		}
	})

	// Test case 6: Complex graph
	t.Run("complex graph", func(t *testing.T) {
		// Create a more complex graph
		// 1 -> 2 -> 3 -> 4
		//  \-> 5 -> 6
		node1 := &GraphNodes{Val: 1}
		node2 := &GraphNodes{Val: 2}
		node3 := &GraphNodes{Val: 3}
		node4 := &GraphNodes{Val: 4}
		node5 := &GraphNodes{Val: 5}
		node6 := &GraphNodes{Val: 6}

		node1.Neighbors = []*GraphNodes{node2, node5}
		node2.Neighbors = []*GraphNodes{node3}
		node3.Neighbors = []*GraphNodes{node4}
		node5.Neighbors = []*GraphNodes{node6}

		// Test path from 1 to 4
		if !hasRoute(node1, node4) {
			t.Error("Expected route from 1 to 4")
		}

		// Test path from 1 to 6
		if !hasRoute(node1, node6) {
			t.Error("Expected route from 1 to 6")
		}

		// Test no path from 6 to 4
		if hasRoute(node6, node4) {
			t.Error("Expected no route from 6 to 4")
		}
	})
}
