package main

//EXPLICACION DE QUITAR ELEMENTOS DE ARRAY:
// LA GRACIA ESTA EN TENER UN INDICE QUE LLEVARA LOS ELEMENTOS CORRECTOS.
// SOLO IMPORTA LA CONDICION QUE REQUIRE EL PROBLEMA, NO PENSAR EN LAS OTRAS.

// Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

// Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

// Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
// Return k.

func removeDuplicates(nums []int) int {
	// Input: nums = [1,1,2]
	// lastNumber -> used for comparing with the following numbers in the slice
	// nextIndex -> used for knowing where to place the following element
	// count
	if len(nums) == 0 {
		return 0
	}

	count := 1
	lastNumber := nums[0]
	nextIndex := 1
	for i := 1; i < len(nums); i++ {
		if lastNumber < nums[i] {
			nums[nextIndex] = nums[i]
			nextIndex++
			lastNumber = nums[i]
			count++
		}
	}

	return count
}

func removeElement(nums []int, val int) int {
	// [3,2,2,3], val = 3
	// [2,2]
	k := 0

	for i := 0; len(nums) > i; i++ {
		if val != nums[i] {
			nums[k] = nums[i]
			k++
		}
	}

	return k
}
