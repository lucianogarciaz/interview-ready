# Python LeetCode Cheat Sheet (for Go Developers)

## Basic Syntax Differences

### Variable Declaration
```python
# Python
x = 5
y = "hello"
z = True

# Go
var x int = 5
y := "hello"
var z bool = true
```

### Function Definition
```python
# Python
def function_name(param1, param2):
    return param1 + param2

# Go
func functionName(param1, param2 int) int {
    return param1 + param2
}
```

### Control Structures
```python
# Python
if condition:
    do_something()
elif other_condition:
    do_something_else()
else:
    do_another_thing()

# Go
if condition {
    doSomething()
} else if otherCondition {
    doSomethingElse()
} else {
    doAnotherThing()
}
```

## Common Data Structures

### Lists (Python) vs Slices (Go)
```python
# Python
# Creating lists
arr = []              # Empty list
arr = [1, 2, 3]       # List with elements
arr = list(range(5))  # List from range: [0, 1, 2, 3, 4]

# List operations
arr.append(4)         # Add element at end: [1, 2, 3, 4]
arr.pop()            # Remove last element: [1, 2, 3]
arr.pop(0)           # Remove first element: [2, 3]
arr.insert(0, 0)     # Insert at index: [0, 2, 3]
arr[1:3]             # Slice from index 1 to 2: [2, 3]
arr[::-1]            # Reverse list: [3, 2, 0]
arr.sort()           # Sort in-place
arr.reverse()        # Reverse in-place
len(arr)             # Get length
arr.index(2)         # Find index of element
arr.count(2)         # Count occurrences
arr.extend([4, 5])   # Add multiple elements
arr.clear()          # Remove all elements

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Go
arr := []int{1, 2, 3}
arr = append(arr, 4)    // Add element
arr = arr[:len(arr)-1]  // Remove last element
arr = arr[1:]           // Remove first element
```

### Dictionaries (Python) vs Maps (Go)
```python
# Python
d = {}
d['key'] = 'value'      # Add/update
value = d.get('key')    # Get with default None
value = d.get('key', 'default')  # Get with custom default
del d['key']            # Remove key
'key' in d              # Check if key exists

# Go
d := make(map[string]string)
d["key"] = "value"      // Add/update
value, exists := d["key"]  // Get with existence check
delete(d, "key")        // Remove key
```

### Sets (Python) vs Maps (Go)
```python
# Python
s = set()
s.add(1)               # Add element
s.remove(1)            # Remove element
1 in s                 # Check membership
s1 | s2                # Union
s1 & s2                # Intersection
s1 - s2                # Difference

# Go
s := make(map[int]bool)
s[1] = true            // Add element
delete(s, 1)           // Remove element
_, exists := s[1]      // Check membership
```

## Common LeetCode Patterns

### Two Pointers
```python
# Python
left, right = 0, len(arr) - 1
while left < right:
    # Do something with arr[left] and arr[right]
    left += 1
    right -= 1

# Go
left, right := 0, len(arr)-1
for left < right {
    // Do something with arr[left] and arr[right]
    left++
    right--
}
```

### Sliding Window
```python
# Python
window = []
for right in range(len(arr)):
    window.append(arr[right])
    while condition:
        window.pop(0)  # Remove from left
    # Process window

# Go
window := []int{}
for right := 0; right < len(arr); right++ {
    window = append(window, arr[right])
    for condition {
        window = window[1:]  // Remove from left
    }
    // Process window
}
```

### BFS (Breadth-First Search)
```python
# Python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Go
func bfs(graph map[int][]int, start int) {
    queue := []int{start}
    visited := map[int]bool{start: true}
    
    for len(queue) > 0 {
        node := queue[0]
        queue = queue[1:]
        for _, neighbor := range graph[node] {
            if !visited[neighbor] {
                visited[neighbor] = true
                queue = append(queue, neighbor)
            }
        }
    }
}
```

### DFS (Depth-First Search)
```python
# Python
def dfs(graph, node, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)

# Go
func dfs(graph map[int][]int, node int, visited map[int]bool) {
    if visited[node] {
        return
    }
    visited[node] = true
    for _, neighbor := range graph[node] {
        dfs(graph, neighbor, visited)
    }
}
```

## Useful Python Built-ins

### Sorting
```python
# Sort list in-place
arr.sort()
# Sort with custom key
arr.sort(key=lambda x: x[1])
# Sort with reverse
arr.sort(reverse=True)
```

### List Comprehensions
```python
# Create new list
squares = [x**2 for x in range(10)]
# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```

### String Operations
```python
# Split string
words = "hello world".split()
# Join strings
sentence = " ".join(words)
# String formatting
name = "Alice"
age = 30
message = f"{name} is {age} years old"
```

### Collections Module
```python
from collections import defaultdict, Counter, deque

# Default dictionary
d = defaultdict(list)
d['key'].append(1)  # No need to check if key exists

# Counter
c = Counter([1, 1, 2, 3, 3, 3])
print(c[3])  # 3

# Deque (double-ended queue)
q = deque()
q.append(1)      # Add to right
q.appendleft(2)  # Add to left
q.pop()          # Remove from right
q.popleft()      # Remove from left
```

## Tips for LeetCode

1. **Use Python's built-in functions** when possible - they're often optimized
2. **List comprehensions** are more readable than explicit loops
3. **Sets** are great for O(1) lookups
4. **Dictionaries** are perfect for counting and caching
5. **Deque** is better than list for queue operations
6. **Use f-strings** for string formatting
7. **Use `enumerate()`** when you need both index and value
8. **Use `zip()`** to iterate over multiple lists simultaneously
9. **Use `any()`** and `all()`** for boolean operations on iterables
10. **Use `collections.defaultdict`** to avoid key existence checks 