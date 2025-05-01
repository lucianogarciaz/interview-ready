package main

type Stack struct {
	stack []int
	mins  []int
}

func NewStack() Stack {
	return Stack{
		stack: []int{},
		mins:  []int{},
	}
}

func (s *Stack) Pop() int {
	if len(s.stack) == 0 {
		return 0
	}
	value := s.stack[len(s.stack)-1]

	s.stack = s.stack[:len(s.stack)-1]
	min := s.min()

	if value == min {
		s.mins = s.mins[:len(s.mins)-1]
	}

	return value
}

func (s *Stack) Push(value int) {
	s.stack = append(s.stack, value)

	if len(s.mins) == 0 {
		s.mins = append(s.mins, value)
		return
	}

	if value < s.min() {
		s.mins = append(s.mins, value)
	}
}

func (s *Stack) Peak() int {
	if len(s.stack) == 0 {
		return 0
	}
	return s.stack[len(s.stack)-1]
}

func (s *Stack) min() int {
	if len(s.mins) == 0 {
		return 0
	}

	return s.mins[len(s.mins)-1]
}
