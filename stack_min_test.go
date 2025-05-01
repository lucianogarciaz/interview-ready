package main

import (
	"testing"
)

func TestStackMin(t *testing.T) {
	t.Run("Empty stack", func(t *testing.T) {
		stack := NewStack()

		// Test min on empty stack
		if stack.min() != 0 {
			t.Errorf("Expected min of empty stack to be 0, got %d", stack.min())
		}

		// Test pop on empty stack
		if stack.Pop() != 0 {
			t.Errorf("Expected pop on empty stack to return 0, got %d", stack.Pop())
		}

		// Test peak on empty stack
		if stack.Peak() != 0 {
			t.Errorf("Expected peak on empty stack to return 0, got %d", stack.Peak())
		}
	})

	t.Run("Push and min operations", func(t *testing.T) {
		stack := NewStack()

		// Push values and check min
		stack.Push(5)
		if stack.min() != 5 {
			t.Errorf("Expected min to be 5, got %d", stack.min())
		}

		stack.Push(3)
		if stack.min() != 3 {
			t.Errorf("Expected min to be 3, got %d", stack.min())
		}

		stack.Push(7)
		if stack.min() != 3 {
			t.Errorf("Expected min to be 3, got %d", stack.min())
		}

		stack.Push(2)
		if stack.min() != 2 {
			t.Errorf("Expected min to be 2, got %d", stack.min())
		}
	})

	t.Run("Pop operations and min updates", func(t *testing.T) {
		stack := NewStack()

		// Setup stack with values
		stack.Push(5)
		stack.Push(3)
		stack.Push(7)
		stack.Push(2)

		// Pop and check min updates correctly
		if val := stack.Pop(); val != 2 {
			t.Errorf("Expected popped value to be 2, got %d", val)
		}

		if stack.min() != 3 {
			t.Errorf("Expected min to be 3 after pop, got %d", stack.min())
		}

		if val := stack.Pop(); val != 7 {
			t.Errorf("Expected popped value to be 7, got %d", val)
		}

		if stack.min() != 3 {
			t.Errorf("Expected min to be 3 after pop, got %d", stack.min())
		}

		if val := stack.Pop(); val != 3 {
			t.Errorf("Expected popped value to be 3, got %d", val)
		}

		if stack.min() != 5 {
			t.Errorf("Expected min to be 5 after pop, got %d", stack.min())
		}
	})

	t.Run("Peak operation", func(t *testing.T) {
		stack := NewStack()

		stack.Push(10)
		stack.Push(20)

		if stack.Peak() != 20 {
			t.Errorf("Expected peak to return 20, got %d", stack.Peak())
		}

		// Peak shouldn't remove the element
		if stack.Peak() != 20 {
			t.Errorf("Expected peak to still return 20, got %d", stack.Peak())
		}
	})

	t.Run("Multiple push and pop operations", func(t *testing.T) {
		stack := NewStack()

		// Push values in decreasing order
		stack.Push(5)
		stack.Push(4)
		stack.Push(3)
		stack.Push(2)
		stack.Push(1)

		// Min should be the smallest value
		if stack.min() != 1 {
			t.Errorf("Expected min to be 1, got %d", stack.min())
		}

		// Pop values and check min updates
		for i := 1; i <= 5; i++ {
			if val := stack.Pop(); val != i {
				t.Errorf("Expected popped value to be %d, got %d", i, val)
			}

			if i < 5 {
				if stack.min() != i+1 {
					t.Errorf("Expected min to be %d after pop, got %d", i+1, stack.min())
				}
			}
		}
	})
}
