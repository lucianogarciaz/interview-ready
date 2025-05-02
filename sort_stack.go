package main

type SortStack struct {
	stack []int
}

func NewSortStack() *SortStack {
	return &SortStack{
		stack: []int{},
	}
}

func (s *SortStack) push(value int) {
	if s.isEmpty() {
		s.stack = []int{value}
		return
	}

	tmp := NewStack()
	for value > s.peak() && !s.isEmpty() {
		tmp.Push(s.pop())
	}

	s.stack = append(s.stack, value)

	for !tmp.IsEmpty() {
		s.stack = append(s.stack, tmp.Pop())
	}

}

func (s *SortStack) pop() int {
	if s.isEmpty() {
		return 0
	}

	value := s.stack[len(s.stack)-1]
	s.stack = s.stack[:len(s.stack)-1]
	return value
}

func (s *SortStack) peak() int {
	if s.isEmpty() {
		return 0
	}
	return s.stack[len(s.stack)-1]
}

func (s *SortStack) isEmpty() bool {
	return len(s.stack) == 0
}
