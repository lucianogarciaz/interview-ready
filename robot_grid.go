package main

func findPath(grid [][]bool) [][]int {
	path, _ := testPath(grid, 0, 0)
	return path
}

func testPath(grid [][]bool, x, y int) ([][]int, bool) {
	if !grid[x][y] {
		return nil, false
	}
	if x == len(grid)-1 && y == len(grid[0])-1 {
		return [][]int{{x, y}}, true
	}

	output := [][]int{{x, y}}
	if y+1 < len(grid) {
		if path, ok := testPath(grid, x, y+1); ok {
			return append(output, path...), true
		}
		// if ok {
		// 	return append(output, path...), true
		// }
		// if !ok {
		// 	return nil, false
		// }
	}

	if x+1 < len(grid[0]) {
		if path, ok := testPath(grid, x+1, y); ok {
			return append(output, path...), true
		}
		// if ok {
		// 	output = append(output, path...)
		// }
		// if !ok {
		// 	return nil, false
		// }
	}

	return nil, false
}
