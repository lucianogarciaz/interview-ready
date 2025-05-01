package main

import (
	"testing"
)

func TestSetOfStacks(t *testing.T) {
	t.Run("Basic push and pop operations", func(t *testing.T) {
		stacks := NewSetOfStacks(3) // Each stack can hold 3 plates

		// Push values and check they can be popped in reverse order
		stacks.Push(1)
		stacks.Push(2)
		stacks.Push(3)
		stacks.Push(4) // This should create a new stack
		stacks.Push(5)

		// Pop values and verify they come out in reverse order
		if val := stacks.Pop(); val != 5 {
			t.Errorf("Expected popped value to be 5, got %d", val)
		}
		if val := stacks.Pop(); val != 4 {
			t.Errorf("Expected popped value to be 4, got %d", val)
		}
		if val := stacks.Pop(); val != 3 {
			t.Errorf("Expected popped value to be 3, got %d", val)
		}
		if val := stacks.Pop(); val != 2 {
			t.Errorf("Expected popped value to be 2, got %d", val)
		}
		if val := stacks.Pop(); val != 1 {
			t.Errorf("Expected popped value to be 1, got %d", val)
		}
	})

	t.Run("Empty stack operations", func(t *testing.T) {
		stacks := NewSetOfStacks(2)

		// Pop on empty stack should return 0
		if val := stacks.Pop(); val != 0 {
			t.Errorf("Expected pop on empty stack to return 0, got %d", val)
		}

		// Push and pop to verify functionality after empty pop
		stacks.Push(10)
		if val := stacks.Pop(); val != 10 {
			t.Errorf("Expected popped value to be 10, got %d", val)
		}
	})

	t.Run("Multiple stacks creation and removal", func(t *testing.T) {
		stacks := NewSetOfStacks(2)

		// Push enough values to create multiple stacks
		for i := 1; i <= 6; i++ {
			stacks.Push(i)
		}

		// Should have created 3 stacks with 2 items each
		if len(stacks.stacks) != 3 {
			t.Errorf("Expected 3 stacks, got %d", len(stacks.stacks))
		}

		// Pop all values and check stacks are removed
		for i := 6; i >= 1; i-- {
			if val := stacks.Pop(); val != i {
				t.Errorf("Expected popped value to be %d, got %d", i, val)
			}
		}

		// All stacks should be removed
		if len(stacks.stacks) != 0 {
			t.Errorf("Expected 0 stacks after popping all values, got %d", len(stacks.stacks))
		}
	})

	t.Run("PopAt specific stack", func(t *testing.T) {
		stacks := NewSetOfStacks(3)

		// Push 7 values (should create 3 stacks: [1,2,3], [4,5,6], [7])
		for i := 1; i <= 7; i++ {
			stacks.Push(i)
		}

		// Pop from the second stack (index 1)
		if val := stacks.PopAt(1); val != 6 {
			t.Errorf("Expected PopAt(1) to return 6, got %d", val)
		}

		// Pop from the first stack (index 0)
		if val := stacks.PopAt(0); val != 3 {
			t.Errorf("Expected PopAt(0) to return 3, got %d", val)
		}
		// Pop from the first stack (index 0)
		if val := stacks.PopAt(0); val != 2 {
			t.Errorf("Expected PopAt(0) to return 3, got %d", val)
		}

		// Pop from the first stack (index 0)
		if val := stacks.PopAt(0); val != 1 {
			t.Errorf("Expected PopAt(0) to return 3, got %d", val)
		}

		// Pop from the first stack (index 0)
		if val := stacks.PopAt(0); val != 5 {
			t.Errorf("Expected PopAt(0) to return 3, got %d", val)
		}

		// Pop from an invalid stack index
		if val := stacks.PopAt(5); val != 0 {
			t.Errorf("Expected PopAt(5) to return 0 for invalid index, got %d", val)
		}

		// Continue normal popping
		if val := stacks.Pop(); val != 7 {
			t.Errorf("Expected Pop() to return 7, got %d", val)
		}
		if val := stacks.Pop(); val != 4 {
			t.Errorf("Expected Pop() to return 5, got %d", val)
		}
	})
}
