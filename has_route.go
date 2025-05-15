package main

// Type: Graph Traversal / BFS / DFS
// Difficulty: Medium
// Companies: This is Exercise 4.1 from "Cracking the Coding Interview" book.
// Similar to LeetCode problem #1971 "Find if Path Exists in Graph".
// Commonly asked at companies like Google, Facebook, Amazon, and Microsoft.
// Tests understanding of graph traversal algorithms and connectivity.

// remember always defining a SET to avoid loops
func hasRoute(start *GraphNodes, end *GraphNodes) bool {
	return graphBfs(start, end)
	// return graphDfs(start, end, map[*GraphNodes]bool{})
}

func graphBfs(start *GraphNodes, goal *GraphNodes) bool {
	set := map[*GraphNodes]bool{}
	queue := []*GraphNodes{start}

	for len(queue) > 0 {
		c := queue[0]
		if _, ok := set[start]; ok {
			return false // it means already looped over this node
		}

		if c == goal {
			return true
		}

		queue = queue[1:]
		queue = append(queue, c.Neighbors...)

	}

	return false
}

func graphDfs(start *GraphNodes, goal *GraphNodes, set map[*GraphNodes]bool) bool {
	if start == goal {
		return true
	}

	if _, ok := set[start]; ok {
		return false // it means already looped over this node
	}

	set[start] = true

	for _, n := range start.Neighbors {
		if graphDfs(n, goal, set) {
			return true
		}
	}
	return false
}
