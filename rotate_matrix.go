package main

import (
	"slices"
)

// 7. *Rotate Matrix*:

// Given an image represented by an NxN matrix, where each pixel in the image is 4
// bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
//             i,j           i,j            i,j    i,j
//  123     1: 0,0 -> 0,2  2:0,1 -> 1,2  3: 0,2 -> 2,2
//  456     4: 1,0 -> 0,1  5:1,1 -> 1,1  6: 1,2 -> 2,1
//  789     7: 2,0 -> 0,0  8:2,1 -> 1,0  9: 2,2 -> 2,0

func rotateMatrix(n [][]int) [][]int {
	if len(n) <= 1 {
		return n
	}

	// initializing matrix.
	output := make([][]int, len(n[0]))
	for i := range output {
		output[i] = make([]int, len(n))
	}

	for i, row := range n {
		for j, r := range row {
			newRow := j
			newCol := len(row) - 1 - i

			output[newRow][newCol] = r
		}
	}
	rotateMatrixInPlace(n)
	return output
}

func rotateMatrixInPlace(n [][]int) [][]int {
	for i := range n {
		for j := i + 1; j < len(n[0]); j++ {
			temp := n[i][j]
			n[i][j] = n[j][i]
			n[j][i] = temp
		}
	}
	for i := range n {
		slices.Reverse(n[i])
	}
	return n
}
