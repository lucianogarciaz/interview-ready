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

func zeroMatrix2(m [][]int) [][]int {
	if len(m) <= 1 || len(m[0]) <= 1 {
		return m
	}

	rowLen := len(m)
	colLen := len(m[0])
	rows := map[int]bool{}
	cols := map[int]bool{}
	for i, r := range m {
		for j, val := range r {
			if val == 0 {
				rows[i] = true
				cols[j] = true
			}
		}
	}
	//     0 1
	// 0	1 1
	// 1	2 1
	// 2	0 1/0
	// 3	1 1

	for row := range rows {
		for j := 0; j < colLen; j++ {
			m[row][j] = 0
		}
	}
	for col := range cols {
		for i := 0; i < rowLen; i++ {
			m[i][col] = 0
		}
	}
	return m
}
