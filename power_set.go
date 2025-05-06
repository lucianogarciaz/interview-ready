package main

func powerSet(a []int) [][]int {
	if len(a) == 0 {
		return [][]int{{}}
	}
	if len(a) == 1 {
		return [][]int{{}, {a[0]}}
	}

	previous := powerSet(a[1:])
	output := previous
	for _, v := range previous {
		couple := append([]int{a[0]}, v...)
		output = append(output, couple)
	}

	return output
}
