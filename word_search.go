package main

func exist(board [][]byte, word string) bool {
	if len(board) == 0 {
		return false
	}

	n := len(board)
	m := len(board[0])
	if n*m < len(word) {
		return false
	}

	current := []string{}
	visited := make([][]bool, n)
	for i := range visited {
		visited[i] = make([]bool, m)
	}

	var backtrack func(x, y int, pos int) bool

	backtrack = func(x, y int, pos int) bool {
		if pos == len(word) {
			return true
		}
		if x < 0 || y < 0 || x == n || y == m {
			return false
		}

		if visited[x][y] {
			return false
		}

		if string(board[x][y]) != string(word[pos]) {
			return false
		}

		visited[x][y] = true
		current = append(current, string(word[pos]))

		if backtrack(x+1, y, pos+1) {
			return true
		}
		if backtrack(x-1, y, pos+1) {
			return true
		}
		if backtrack(x, y+1, pos+1) {
			return true
		}

		if backtrack(x, y-1, pos+1) {
			return true
		}

		visited[x][y] = false
		current = current[:len(current)-1]

		return false
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if backtrack(i, j, 0) {
				return true
			}
		}
	}
	return false
}
