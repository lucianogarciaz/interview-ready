package main

import "strconv"

// 1. obtengo la celda con menos candidatos
// 2. calculo y pongo el valor.
func solveSudoku(board [][]byte) {
	candidates := make([][][]int, 9)
	for i := 0; i < 9; i++ {
		candidates[i] = make([][]int, 9)
		for j := 0; j < 9; j++ {
			candidates[i][j] = make([]int, 0, 9)
			candidates = updateCandidates(i, j, candidates, board)
		}
	}

	var backtrack func() bool
	backtrack = func() bool {
		x, y := chooseFromLessCandidates(board, candidates)
		if x == -1 { //we will return this when no candidates avaialble.
			return true
		}

		toModify := neighboors(x, y, board) // return an slice of coordinates [[1,1], [2,2], ...]
		for _, val := range toModify {
			updateCandidates(val[0], val[1], candidates, board)
		}

		for _, val := range candidates[x][y] {
			board[x][y] = '0' + byte(val)

			if backtrack() {
				return true
			}

			board[x][y] = byte('.') //unset the state

			for _, toM := range toModify {
				updateCandidates(toM[0], toM[1], candidates, board)
			}
		}
		return false
	}
	backtrack()

	return
}

func chooseFromLessCandidates(board [][]byte, candidates [][][]int) (int, int) {
	lessCandidates := 1000000000
	x, y := -1, -1
	for i := range candidates {
		for j := range candidates[i] {
			if board[i][j] == byte('.') && len(candidates[i][j]) < lessCandidates {
				lessCandidates = len(candidates[i][j])
				x = i
				y = j
			}
		}
	}

	return x, y
}

func neighboors(x, y int, board [][]byte) [][]int {
	neighboor := [][]int{}
	// columns
	for i := range board {
		if board[i][y] == byte('.') {
			neighboor = append(neighboor, []int{i, y})
		}
	}
	for j := range board[x] {
		if board[x][j] == byte('.') {
			neighboor = append(neighboor, []int{x, y})
		}
	}
	// 0,4
	xPos := x - x%3
	yPos := y - y%3
	for i := xPos; i < xPos+3; i++ {
		for j := yPos; j < yPos+3; j++ {
			if i == x || j == y { //we already have taken care of these elements
				continue
			}

			if board[i][j] == byte('.') {
				neighboor = append(neighboor, []int{i, y})
			}
		}
	}

	return neighboor
}

func updateCandidates(x, y int, candidates [][][]int, board [][]byte) [][][]int {
	can := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	candidates[x][y] = []int{}
	if board[x][y] != byte('.') {
		return candidates
	}

	for i := range board {
		if board[i][y] != byte('.') {
			val, _ := strconv.Atoi(string(board[i][y]))
			can[val-1] = 0
		}
	}

	for j := range board[x] {
		if board[x][j] != byte('.') {
			val, _ := strconv.Atoi(string(board[x][j]))
			can[val-1] = 0
		}
	}
	xPos := x - x%3
	yPos := y - y%3
	for i := xPos; i < xPos+3; i++ {
		for j := yPos; j < yPos+3; j++ {
			if i == x || j == y { //we already have taken care of these elements
				continue
			}

			if board[i][j] != byte('.') {
				val, _ := strconv.Atoi(string(board[i][j]))
				can[val-1] = 0
			}
		}
	}

	for _, val := range can {
		if val != 0 {
			candidates[x][y] = append(candidates[x][y], val)
		}
	}

	return candidates
}
