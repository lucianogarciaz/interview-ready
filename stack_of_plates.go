package main

type SetOfStacks struct {
	stacks [][]int
	limit  int
}

func NewSetOfStacks(limit int) SetOfStacks {
	return SetOfStacks{
		stacks: [][]int{},
		limit:  limit,
	}
}

func (s *SetOfStacks) Push(value int) {
	for i, v := range s.stacks {
		if len(v) == s.limit {
			continue
		}
		s.stacks[i] = append(s.stacks[i], value)
		return
	}

	s.stacks = append(s.stacks, []int{value})
}

func (s *SetOfStacks) Pop() int {
	if len(s.stacks) == 0 {
		return 0
	}

	lastStack := s.stacks[len(s.stacks)-1]
	value := lastStack[len(lastStack)-1]
	lastStack = lastStack[:len(lastStack)-1]
	if len(lastStack) == 0 {
		s.stacks = s.stacks[:len(s.stacks)-1]
		return value
	}

	s.stacks[len(s.stacks)-1] = lastStack

	return value
}

func (s *SetOfStacks) PopAt(key int) int {
	if key >= len(s.stacks) {
		return 0
	}

	stack := s.stacks[key]
	value := stack[len(stack)-1]
	s.stacks[key] = stack[:len(stack)-1]

	if len(s.stacks[key]) == 0 {
		rightStacks := s.stacks[key+1:]
		leftStacks := s.stacks[:key]
		s.stacks = append(leftStacks, rightStacks...)
	}

	return value
}
