package main

// 1  2  3  4
// 12 13 14 5
// 11 16 15 6
// 10 9  8  7

// right -> down -> left -> up -> loop
// time: o(n*n)
// space: o(n*n)
// valid = if it's within the matrix AND value was NOT set -> != 0
// i: [1,-1] [up, down]
// j: [1,-1] [right, left]
// move: 0-3
func generateMatrix(n int) [][]int {
	output := make([][]int, n)
	for i := range output {
		output[i] = make([]int, n)
	}

	value := 1
	dir := 0
	i, j := 0, 0
	output[0][0] = 1
	for value < n*n {
		potI, potJ := calculateNextPosition(dir, i, j)
		if 0 <= potI && potI < n && 0 <= potJ && potJ < n && output[potI][potJ] == 0 {
			i = potI
			j = potJ
			value++
			output[i][j] = value
		} else {
			dir = nextDirection(dir)
		}
	}
	return output
}

func calculateNextPosition(dir, i, j int) (int, int) {
	switch dir {
	case 0:
		return i, j + 1
	case 1:
		return i + 1, j
	case 2:
		return i, j - 1
	case 3:
		return i - 1, j
	default:
		return i + 1, j + 1
	}
}

func nextDirection(previousMove int) int {
	if previousMove == 3 {
		return 0
	}

	return previousMove + 1
}
