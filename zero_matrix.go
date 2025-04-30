package main

func zeroMatrix(m [][]int) [][]int {
	type coordinates struct {
		x int
		y int
	}
	zeros := []coordinates{}
	for i, rows := range m {
		for j, v := range rows {
			if v == 0 {
				zeros = append(zeros, coordinates{i, j})
			}
		}
	}

	for _, c := range zeros {
		for i, rows := range m {
			for j := range rows {
				if i == c.x {
					m[i][j] = 0
				}
				if j == c.y {
					m[i][j] = 0
				}

			}
		}
	}

	return m
}
