package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSortStack(t *testing.T) {
	t.Run("push elements in sorted order", func(t *testing.T) {
		stack := NewSortStack()

		// Push elements in random order
		stack.push(5)
		stack.push(2)
		stack.push(7)
		stack.push(1)
		stack.push(3)

		// Elements should be popped in ascending order (smallest on top)
		assert.Equal(t, 1, stack.pop())
		assert.Equal(t, 2, stack.pop())
		assert.Equal(t, 3, stack.pop())
		assert.Equal(t, 5, stack.pop())
		assert.Equal(t, 7, stack.pop())
		assert.True(t, stack.isEmpty())
	})

	t.Run("push elements in reverse order", func(t *testing.T) {
		stack := NewSortStack()

		// Push elements in descending order
		stack.push(10)
		stack.push(8)
		stack.push(6)
		stack.push(4)
		stack.push(2)

		// Elements should still be popped in ascending order
		assert.Equal(t, 2, stack.pop())
		assert.Equal(t, 4, stack.pop())
		assert.Equal(t, 6, stack.pop())
		assert.Equal(t, 8, stack.pop())
		assert.Equal(t, 10, stack.pop())
		assert.True(t, stack.isEmpty())
	})

	t.Run("push elements with duplicates", func(t *testing.T) {
		stack := NewSortStack()

		// Push elements with duplicates
		stack.push(3)
		stack.push(1)
		stack.push(3)
		stack.push(5)
		stack.push(1)

		// Elements should be popped in ascending order with duplicates
		assert.Equal(t, 1, stack.pop())
		assert.Equal(t, 1, stack.pop())
		assert.Equal(t, 3, stack.pop())
		assert.Equal(t, 3, stack.pop())
		assert.Equal(t, 5, stack.pop())
		assert.True(t, stack.isEmpty())
	})

	t.Run("empty stack", func(t *testing.T) {
		stack := NewSortStack()

		assert.True(t, stack.isEmpty())
	})

	t.Run("push after pop", func(t *testing.T) {
		stack := NewSortStack()

		stack.push(5)
		stack.push(3)

		assert.Equal(t, 3, stack.pop())

		stack.push(1)
		stack.push(4)

		assert.Equal(t, 1, stack.pop())
		assert.Equal(t, 4, stack.pop())
		assert.Equal(t, 5, stack.pop())
		assert.True(t, stack.isEmpty())
	})
}
