# Python LeetCode Cheat Sheet

## Table of Contents
1. [Basic Syntax](#basic-syntax)
2. [Data Structures](#data-structures)
3. [Built-in Functions](#built-in-functions)
4. [String Operations](#string-operations)
5. [Math Operations](#math-operations)
6. [Random Module](#random-module)
7. [Common Patterns](#common-patterns)
8. [Collections Module](#collections-module)
9. [Heapq Module](#heapq-module)
10. [Itertools Module](#itertools-module)
11. [Sorting](#sorting)
12. [Binary Search](#binary-search)
13. [Bit Manipulation](#bit-manipulation)
14. [Tips & Tricks](#tips--tricks)

## Basic Syntax

### Variable Declaration
```python
x = 5
y = "hello"
z = True
arr = [1, 2, 3]
matrix = [[1, 2], [3, 4]]
```

### Function Definition
```python
def function_name(param1, param2):
    return param1 + param2

def with_type_hints(param1: int, param2: int) -> int:
    return param1 + param2
```

### Control Structures
```python
if condition:
    pass
elif other_condition:
    pass
else:
    pass

for i in range(10):
    pass

for item in arr:
    pass

for i, val in enumerate(arr):
    pass

while condition:
    pass
```

### Multiple Assignment
```python
a, b = 1, 2
a, b = b, a  # Swap
x = y = z = 0
```

## Data Structures

### Lists
```python
arr = []                    # Empty list - O(1)
arr = [1, 2, 3]            # With elements - O(n)
arr = [0] * 5              # [0, 0, 0, 0, 0] - O(n)
arr = list(range(5))       # [0, 1, 2, 3, 4] - O(n)

arr.append(4)              # Add at end - O(1) amortized
arr.insert(0, 0)           # Insert at index - O(n)
arr.pop()                  # Remove and return last - O(1)
arr.pop(0)                 # Remove and return at index - O(n)
arr.remove(value)          # O(n)
del arr[2]                 # Deletes element at index 2 - O(n)
arr.clear()                # Remove all - O(n)

arr[1:3]                   # Slice [1, 2] - O(k) where k is slice size
arr[:2]                    # First 2 elements - O(k)
arr[2:]                    # From index 2 to end - O(k)
arr[-1]                    # Last element - O(1)
arr[-2:]                   # Last 2 elements - O(k)
arr[::-1]                  # Reverse - O(n)
arr[::2]                   # Every 2nd element - O(n)

arr.sort()                 # Sort in-place - O(n log n)
arr.reverse()              # Reverse in-place - O(n)
arr.index(value)           # Find index (raises ValueError if not found) - O(n)
arr.count(value)           # Count occurrences - O(n)
arr.extend([4, 5])         # Add multiple elements - O(k) where k is length of extension

len(arr)                   # Length - O(1)
min(arr)                   # Minimum - O(n)
max(arr)                   # Maximum - O(n)
sum(arr)                   # Sum - O(n)

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
matrix = [[0] * n for _ in range(m)]  # m x n matrix
```

### Dictionaries
```python
d = {}                              # Empty dict - O(1)
d = {'key': 'value'}               # With items - O(n)
d = dict()                         # Using constructor - O(1)

d['key'] = 'value'                 # Add/update - O(1) average
value = d.get('key')               # Get (returns None if not found) - O(1) average
value = d.get('key', 'default')    # Get with default - O(1) average
value = d.pop('key')               # Remove and return - O(1) average
value = d.pop('key', 'default')    # Pop with default - O(1) average
del d['key']                       # Delete key - O(1) average

'key' in d                         # Check existence - O(1) average
list(d.keys())                     # All keys - O(n)
list(d.values())                   # All values - O(n)
list(d.items())                    # All (key, value) pairs - O(n)

d.update({'key2': 'value2'})       # Merge dicts - O(k) where k is size of update dict
d.clear()                          # Remove all - O(n)

# Dict comprehension
squares = {x: x**2 for x in range(5)}
```

### Sets
```python
s = set()                  # Empty set - O(1)
s = {1, 2, 3}             # With elements - O(len(s))
s = set([1, 2, 3])        # From list - O(len(list))

s.add(4)                  # Add element - O(1) average
s.remove(1)               # Remove (raises KeyError if not found) - O(1) average
s.discard(1)              # Remove (no error if not found) - O(1) average
s.pop()                   # Remove and return arbitrary element - O(1)
s.clear()                 # Remove all - O(n)

1 in s                    # Check membership - O(1) average
len(s)                    # Size - O(1)

s1 | s2                   # Union - O(len(s1) + len(s2))
s1 & s2                   # Intersection - O(min(len(s1), len(s2)))
s1 - s2                   # Difference - O(len(s1))
s1 ^ s2                   # Symmetric difference - O(len(s1) + len(s2))
s1.issubset(s2)          # Check if s1 ⊆ s2 - O(len(s1))
s1.issuperset(s2)        # Check if s1 ⊇ s2 - O(len(s2))

# Set comprehension
even_set = {x for x in range(10) if x % 2 == 0}
```

### Tuples
```python
t = ()                    # Empty tuple - O(1)
t = (1,)                  # Single element (note the comma) - O(1)
t = (1, 2, 3)            # Multiple elements - O(n)
t = 1, 2, 3              # Without parentheses - O(n)

a, b, c = t              # Unpacking - O(n)
a, *rest = t             # Extended unpacking - O(n)

t[0]                     # Access by index - O(1)
t[1:3]                   # Slicing - O(k) where k is slice size
len(t)                   # Length - O(1)
t.count(value)           # Count occurrences - O(n)
t.index(value)           # Find index - O(n)
```

### Strings
```python
s = "hello"
s = 'hello'
s = """multi
line"""

s[0]                     # Access by index: 'h' - O(1)
s[1:3]                   # Slice: 'el' - O(k) where k is slice size
s[::-1]                  # Reverse: 'olleh' - O(n)
len(s)                   # Length: 5 - O(1)

s.lower()                # Convert to lowercase - O(n)
s.upper()                # Convert to uppercase - O(n)
s.strip()                # Remove whitespace - O(n)
s.split()                # Split by whitespace - O(n)
s.split(',')             # Split by delimiter - O(n)
''.join(['a', 'b'])      # Join: 'ab' - O(n) where n is total chars

s.startswith('he')       # True - O(k) where k is length of prefix
s.endswith('lo')         # True - O(k) where k is length of suffix
s.find('ll')             # Index or -1: 2 - O(n)
s.index('ll')            # Index or ValueError: 2 - O(n)
s.count('l')             # Count: 2 - O(n)
s.replace('l', 'L')      # Replace: 'heLLo' - O(n)

s.isalpha()              # All alphabetic - O(n)
s.isdigit()              # All digits - O(n)
s.isalnum()              # All alphanumeric - O(n)
s.islower()              # All lowercase - O(n)
s.isupper()              # All uppercase - O(n)

# String formatting
name = "Alice"
age = 30
f"{name} is {age} years old"
```

### Deque (from collections)
```python
from collections import deque

dq = deque()              # Empty deque - O(1)
dq = deque([1, 2, 3])    # From list - O(n)

dq.append(4)             # Add to right: [1, 2, 3, 4] - O(1)
dq.appendleft(0)         # Add to left: [0, 1, 2, 3, 4] - O(1)
dq.pop()                 # Remove from right: 4 - O(1)
dq.popleft()             # Remove from left: 0 - O(1)
dq.extend([5, 6])        # Extend right - O(k) where k is length of extension
dq.extendleft([7, 8])    # Extend left - O(k)
dq.rotate(1)             # Rotate right - O(k) where k is rotation steps
dq.rotate(-1)            # Rotate left - O(k)

len(dq)                  # Length - O(1)
dq[0]                    # Access by index - O(n)
dq.remove(value)         # Remove first occurrence - O(n)
dq.count(value)          # Count occurrences - O(n)
```

## Built-in Functions

### Common Functions
```python
len(obj)                 # Length - O(1)
min(arr)                 # Minimum - O(n)
max(arr)                 # Maximum - O(n)
sum(arr)                 # Sum - O(n)
abs(x)                   # Absolute value - O(1)
pow(x, y)                # x to power y - O(log y) for integer exponentiation
divmod(a, b)            # (a // b, a % b) - O(1)

range(n)                 # 0 to n-1 - O(1) to create, O(n) to iterate
range(start, end)        # start to end-1 - O(1)
range(start, end, step)  # with step - O(1)

sorted(arr)              # Return sorted copy - O(n log n)
reversed(arr)            # Return reversed iterator - O(1) to create, O(n) to iterate

any([True, False])       # True if any is True - O(n) worst case
all([True, True])        # True if all are True - O(n) worst case

map(func, arr)           # Apply function to each - O(1) to create, O(n) to iterate
filter(func, arr)        # Filter by function - O(1) to create, O(n) to iterate
zip(arr1, arr2)          # Combine iterables - O(1) to create, O(n) to iterate

enumerate(arr)           # (index, value) pairs - O(1) to create, O(n) to iterate
enumerate(arr, start=1)  # Start from 1 - O(1) to create

isinstance(obj, type)    # Check type - O(1)
type(obj)               # Get type - O(1)
```

### Type Conversions
```python
int('123')               # String to int: 123 - O(n) where n is string length
float('3.14')           # String to float: 3.14 - O(n)
str(123)                # Int to string: '123' - O(log n) where n is the number
chr(65)                 # ASCII to char: 'A' - O(1)
ord('A')                # Char to ASCII: 65 - O(1)

list('abc')             # String to list: ['a', 'b', 'c'] - O(n)
list(range(5))          # Range to list: [0, 1, 2, 3, 4] - O(n)
tuple([1, 2, 3])        # List to tuple - O(n)
set([1, 2, 2, 3])       # List to set: {1, 2, 3} - O(n)

bin(10)                 # To binary: '0b1010' - O(log n)
hex(255)                # To hex: '0xff' - O(log n)
oct(8)                  # To octal: '0o10' - O(log n)
```

## String Operations

### Common Methods
```python
s = "  Hello World  "

s.strip()               # Remove whitespace: "Hello World"
s.lstrip()              # Left strip
s.rstrip()              # Right strip

s.split()               # ['Hello', 'World']
s.split('o')            # ['  Hell', ' W', 'rld  ']
'a,b,c'.split(',')      # ['a', 'b', 'c']

','.join(['a', 'b'])    # 'a,b'
' '.join(['hello'])     # 'hello'

s.replace('World', 'Python')
s.find('World')         # Index or -1
s.index('World')        # Index or ValueError
s.count('l')            # Count occurrences

s.startswith('Hello')
s.endswith('World')

s.lower()
s.upper()
s.capitalize()          # First char upper
s.title()               # Title Case

s.isalpha()             # All alphabetic
s.isdigit()             # All digits
s.isalnum()             # Alphanumeric
s.isspace()             # All whitespace
```

### String Formatting
```python
name = "Alice"
age = 30

f"{name} is {age}"                    # f-strings
f"{name:>10}"                         # Right align
f"{age:05d}"                          # Zero padding: 00030
f"{3.14159:.2f}"                      # 2 decimals: 3.14

"{} {}".format("Hello", "World")
"{0} {1}".format("Hello", "World")
"{name} {age}".format(name="Alice", age=30)
```

## Math Operations

### Basic Operations
```python
import math

math.ceil(3.2)          # 4
math.floor(3.8)         # 3
math.trunc(3.8)         # 3
round(3.5)              # 4 (banker's rounding)

math.sqrt(16)           # 4.0
math.pow(2, 3)          # 8.0
pow(2, 3)               # 8
2 ** 3                  # 8

math.log(8, 2)          # 3.0 (log base 2)
math.log10(100)         # 2.0
math.log(2.718281828)   # 1.0 (natural log)

math.gcd(12, 18)        # 6
math.factorial(5)       # 120

math.inf                # Infinity
math.pi                 # 3.141592...
math.e                  # 2.718281...
```

### Division Operations
```python
7 / 2                   # 3.5 (float division)
7 // 2                  # 3 (floor division)
-7 // 2                 # -4 (floor division)
7 % 2                   # 1 (modulo)
divmod(7, 2)            # (3, 1)
```

## Random Module

### Basic Random Operations
```python
import random

random.random()                    # Float [0.0, 1.0) -> 0.8444218515250481
random.uniform(1, 10)              # Float [1, 10] -> 7.892234132
random.randint(1, 10)              # Int [1, 10] (inclusive) -> 7
random.randrange(0, 10)            # Int [0, 10) (exclusive end) -> 5
random.randrange(0, 10, 2)         # Int [0, 10) with step 2 -> 4 (0, 2, 4, 6, 8)
```

### Random Selection
```python
import random

arr = [1, 2, 3, 4, 5]

random.choice(arr)                 # Single random element -> 3
random.choices(arr, k=3)           # 3 elements with replacement -> [2, 5, 2]
random.sample(arr, 3)              # 3 unique elements without replacement -> [4, 1, 5]

weights = [1, 2, 3, 4, 5]
random.choices(arr, weights=weights, k=3)  # Weighted random selection -> [5, 4, 5]
```

### Shuffling
```python
import random

arr = [1, 2, 3, 4, 5]
random.shuffle(arr)                # Shuffle in-place
# arr is now -> [3, 5, 1, 4, 2]
```

### Setting Seed (for reproducibility)
```python
import random

random.seed(42)                    # Set seed for reproducibility
random.random()                    # -> 0.6394267984578837
random.randint(1, 10)              # -> 1

random.seed(42)                    # Reset same seed
random.random()                    # -> 0.6394267984578837 (same as before!)
random.randint(1, 10)              # -> 1 (same as before!)
```

### Random with Range
```python
import random

random.randint(1, 6)               # Dice roll (1-6) -> 4
random.randint(0, 1)               # Coin flip (0 or 1) -> 0
random.choice([True, False])       # Boolean -> True
random.choice(['Heads', 'Tails'])  # Coin flip -> 'Heads'

random.getrandbits(8)              # Random 8-bit integer (0-255) -> 142
```

### Common Use Cases
```python
import random

random_password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=8))
# -> 'j8x3k9m2'

arr = [10, 20, 30, 40, 50]
random_index = random.randint(0, len(arr) - 1)
# -> 3

shuffled = random.sample(arr, len(arr))
# -> [30, 10, 50, 20, 40]

random_subset = random.sample(range(100), 10)
# -> [72, 15, 43, 88, 9, 56, 31, 67, 2, 94]

random_float_range = random.uniform(0.5, 9.5)
# -> 6.234891234
```

## Common Patterns

### Two Pointers
```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target:
            return [left, right]
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
```

### Sliding Window (Fixed Size)
```python
def sliding_window_fixed(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### Sliding Window (Variable Size)
```python
def sliding_window_variable(arr):
    left = 0
    result = 0
    window_sum = 0
    
    for right in range(len(arr)):
        window_sum += arr[right]
        
        while window_sum > target:
            window_sum -= arr[left]
            left += 1
        
        result = max(result, right - left + 1)
    
    return result
```

### Fast and Slow Pointers
```python
def has_cycle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False
```

### BFS (Breadth-First Search)
```python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### BFS with Levels
```python
def bfs_levels(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

### DFS (Depth-First Search) - Recursive
```python
def dfs_recursive(graph, node, visited):
    if node in visited:
        return
    
    visited.add(node)
    
    for neighbor in graph[node]:
        dfs_recursive(graph, neighbor, visited)
```

### DFS - Iterative
```python
def dfs_iterative(graph, start):
    stack = [start]
    visited = set()
    
    while stack:
        node = stack.pop()
        
        if node in visited:
            continue
        
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
```

### Tree Traversals
```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

### Backtracking Template
```python
def backtrack(path, choices):
    if is_valid(path):
        result.append(path[:])
        return
    
    for choice in choices:
        if is_valid_choice(choice):
            path.append(choice)
            backtrack(path, choices)
            path.pop()
```

### Dynamic Programming (Memoization)
```python
def dp_memo(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = dp_memo(n - 1, memo) + dp_memo(n - 2, memo)
    return memo[n]

from functools import lru_cache

@lru_cache(maxsize=None)
def dp_lru(n):
    if n <= 1:
        return n
    return dp_lru(n - 1) + dp_lru(n - 2)
```

### Dynamic Programming (Tabulation)
```python
def dp_tabulation(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
```

## Collections Module

### Counter
```python
from collections import Counter

c = Counter([1, 1, 2, 3, 3, 3])  # O(n)
c = Counter('abracadabra')        # O(n)

c['a']                          # Count of 'a': 5 - O(1) average
c.most_common(2)                # [('a', 5), ('b', 2)] - O(n log k) where k is argument
c.elements()                    # Iterator over elements - O(1) to create, O(n) to iterate
c.total()                       # Sum of counts - O(n)
c.update(['a', 'b'])            # Add more elements - O(k) where k is size of update
c.subtract(['a', 'a'])          # Subtract elements - O(k)

c1 + c2                         # Add counts - O(len(c1) + len(c2))
c1 - c2                         # Subtract (keep positive only) - O(len(c1) + len(c2))
c1 & c2                         # Intersection (min) - O(min(len(c1), len(c2)))
c1 | c2                         # Union (max) - O(len(c1) + len(c2))
```

### defaultdict
```python
from collections import defaultdict

d = defaultdict(int)            # Default 0 - O(1)
d = defaultdict(list)           # Default [] - O(1)
d = defaultdict(set)            # Default set() - O(1)
d = defaultdict(lambda: 'default')  # O(1)

d['key']                        # Access/create with default - O(1) average
d['key'].append(1)              # No KeyError - O(1) average for access
```

### OrderedDict
```python
from collections import OrderedDict

d = OrderedDict()                 # O(1)
d['a'] = 1                        # O(1) average
d['b'] = 2                        # O(1) average

d.move_to_end('a')              # Move to end - O(1)
d.move_to_end('b', last=False)  # Move to beginning - O(1)
d.popitem(last=True)            # Pop from end - O(1)
d.popitem(last=False)           # Pop from beginning - O(1)
```

### namedtuple
```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])  # O(1) - creates class
p = Point(1, 2)                          # O(1) - creates instance

p.x                             # 1 - O(1)
p.y                             # 2 - O(1)
p[0]                            # 1 - O(1)
```

## Heapq Module

### Min Heap
```python
import heapq

heap = []                       # O(1)
heapq.heappush(heap, 3)         # Add element - O(log n)
heapq.heappush(heap, 1)         # O(log n)
heapq.heappush(heap, 2)         # O(log n)

heapq.heappop(heap)             # Remove and return min: 1 - O(log n)
heap[0]                         # Peek at min: 2 - O(1)

heapq.heapify([3, 1, 2])        # Convert list to heap - O(n)
heapq.nlargest(2, arr)          # 2 largest elements - O(n log k) where k is argument
heapq.nsmallest(2, arr)         # 2 smallest elements - O(n log k)
```

### Max Heap
```python
import heapq

heap = []                       # O(1)
heapq.heappush(heap, -3)        # Negate values - O(log n)
heapq.heappush(heap, -1)        # O(log n)
heapq.heappush(heap, -2)        # O(log n)

max_val = -heapq.heappop(heap)  # Get max: 3 - O(log n)
```

### Heap with Custom Objects
```python
import heapq

heap = []                                    # O(1)
heapq.heappush(heap, (priority, item))       # O(log n)
priority, item = heapq.heappop(heap)         # O(log n)
```

## Itertools Module

### Common Functions
```python
from itertools import *

# Infinite iterators
count(10)                       # 10, 11, 12, ...
cycle([1, 2, 3])               # 1, 2, 3, 1, 2, 3, ...
repeat(10, 3)                  # 10, 10, 10

# Combinatoric iterators
permutations([1, 2, 3])        # All permutations
permutations([1, 2, 3], 2)     # Length 2 permutations
combinations([1, 2, 3], 2)     # [(1,2), (1,3), (2,3)]
combinations_with_replacement([1, 2], 2)  # [(1,1), (1,2), (2,2)]
product([1, 2], [3, 4])        # [(1,3), (1,4), (2,3), (2,4)]

# Other iterators
chain([1, 2], [3, 4])          # [1, 2, 3, 4]
compress([1,2,3], [1,0,1])     # [1, 3]
dropwhile(lambda x: x<5, [1,4,6,4,1])  # [6, 4, 1]
takewhile(lambda x: x<5, [1,4,6,4,1])  # [1, 4]
groupby([1,1,2,2,3])           # Group consecutive
islice([1,2,3,4,5], 2)         # First 2: [1, 2]
```

## Sorting

### Basic Sorting
```python
arr = [3, 1, 2]

arr.sort()                      # Sort in-place - O(n log n)
arr.sort(reverse=True)          # Descending - O(n log n)

sorted(arr)                     # Return sorted copy - O(n log n)
sorted(arr, reverse=True)       # Descending copy - O(n log n)
```

### Custom Sorting
```python
# Sort by key function - O(n log n) but key function called O(n log n) times
arr.sort(key=lambda x: x[1])    # By 2nd element
arr.sort(key=lambda x: (x[0], -x[1]))  # Multiple keys
arr.sort(key=str.lower)         # Case-insensitive

# Custom comparison (Python 3) - O(n log n) with comparison function
from functools import cmp_to_key

def compare(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0

arr.sort(key=cmp_to_key(compare))
```

### Sorting Complex Objects
```python
students = [
    ('Alice', 25, 90),
    ('Bob', 20, 85),
    ('Charlie', 22, 95)
]

students.sort(key=lambda x: x[2], reverse=True)  # By score - O(n log n)
students.sort(key=lambda x: (x[1], -x[2]))       # By age, then score desc - O(n log n)
```

## Binary Search

### Built-in Binary Search
```python
import bisect

arr = [1, 3, 4, 4, 6, 8]

bisect.bisect_left(arr, 4)      # 2 (leftmost insertion point) - O(log n)
bisect.bisect_right(arr, 4)     # 4 (rightmost insertion point) - O(log n)
bisect.bisect(arr, 4)           # Same as bisect_right - O(log n)

bisect.insort_left(arr, 5)      # Insert maintaining order - O(n)
bisect.insort_right(arr, 5)     # O(n)
bisect.insort(arr, 5)           # O(n)
```

### Manual Binary Search
```python
# O(log n) - Binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# O(log n) - Find leftmost insertion point
def binary_search_leftmost(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

# O(log n) - Find rightmost insertion point
def binary_search_rightmost(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left
```

## Bit Manipulation

### Basic Operations
```python
x & y                   # AND - O(1)
x | y                   # OR - O(1)
x ^ y                   # XOR - O(1)
~x                      # NOT - O(1)
x << n                  # Left shift (multiply by 2^n) - O(1)
x >> n                  # Right shift (divide by 2^n) - O(1)

x & 1                   # Check if odd - O(1)
x & (x - 1)             # Clear rightmost bit - O(1)
x & -x                  # Get rightmost bit - O(1)
x | (1 << n)            # Set nth bit - O(1)
x & ~(1 << n)           # Clear nth bit - O(1)
x ^ (1 << n)            # Toggle nth bit - O(1)
(x >> n) & 1            # Get nth bit - O(1)

bin(x)                  # To binary string - O(log x)
int('1010', 2)          # Binary string to int - O(n) where n is string length

x.bit_length()          # Number of bits - O(1)
x.bit_count()           # Number of 1s (Python 3.10+) - O(1)
```

### Common Patterns
```python
# O(k) where k is number of 1 bits
def count_ones(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

# O(1) - Check if power of two
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# O(1) - Swap without temp variable
def swap_without_temp(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b
```

## Tips & Tricks

### List Operations
```python
arr = [1, 2, 3, 4, 5]

arr[-1]                         # Last element
arr[-2:]                        # Last 2 elements
arr[::2]                        # Every 2nd element
arr[::-1]                       # Reverse
arr * 2                         # [1,2,3,4,5,1,2,3,4,5]

max(arr)                        # Maximum
min(arr)                        # Minimum
sum(arr)                        # Sum

[x for x in arr if x > 2]       # Filter
[x * 2 for x in arr]            # Map
[x if x > 2 else 0 for x in arr]  # Conditional
```

### Dictionary Operations
```python
d = {'a': 1, 'b': 2, 'c': 3}

d.get('d', 0)                   # Get with default
d.setdefault('d', 0)            # Set if not exists

{k: v for k, v in d.items() if v > 1}  # Dict comprehension
{v: k for k, v in d.items()}    # Swap keys and values

dict(zip(keys, values))         # Create from lists
```

### Useful Patterns
```python
# Check if all elements are unique
len(arr) == len(set(arr))

# Flatten 2D list
flat = [item for sublist in matrix for item in sublist]

# Transpose matrix
transposed = list(zip(*matrix))

# Remove duplicates preserving order
seen = set()
result = [x for x in arr if not (x in seen or seen.add(x))]

# Get indices of all occurrences
indices = [i for i, x in enumerate(arr) if x == target]

# Split list into chunks
chunks = [arr[i:i+n] for i in range(0, len(arr), n)]

# Merge two sorted lists
merged = sorted(list1 + list2)

# Find max/min with index
max_idx = arr.index(max(arr))
min_idx = arr.index(min(arr))
```

### String Tricks
```python
# Check if palindrome
s == s[::-1]

# Remove duplicates from string
''.join(dict.fromkeys(s))

# Count vowels
sum(c in 'aeiou' for c in s.lower())

# Anagram check
sorted(s1) == sorted(s2)

# All permutations
from itertools import permutations
[''.join(p) for p in permutations('abc')]
```

### Math Tricks
```python
import math

# Round up division
(a + b - 1) // b
math.ceil(a / b)

# Check if even/odd
x % 2 == 0          # Even
x & 1 == 0          # Even (faster)

# Absolute difference
abs(a - b)

# Sign of number
(x > 0) - (x < 0)

# Clamp value
max(min_val, min(x, max_val))
```

### Performance Tips
```python
# Use set for O(1) lookups instead of list
seen = set()
if x in seen:       # O(1)
    pass

# Use collections.Counter for counting
from collections import Counter
counter = Counter(arr)

# Use enumerate instead of range(len())
for i, val in enumerate(arr):
    pass

# Use zip for parallel iteration
for a, b in zip(list1, list2):
    pass

# Use any/all for boolean checks
any(x > 0 for x in arr)
all(x > 0 for x in arr)

# Use generator expressions for memory efficiency
sum(x**2 for x in range(1000000))  # Better than [x**2 for x in range(1000000)]
```

### Edge Cases to Remember
```python
# Empty inputs
if not arr:
    return []

# Single element
if len(arr) == 1:
    return arr[0]

# Integer overflow (not an issue in Python)
# But be careful with very large numbers

# Division by zero
if denominator != 0:
    result = numerator / denominator

# Negative indices
arr[-1]             # Last element
arr[-2]             # Second to last

# None checks
if x is None:
    pass
if x is not None:
    pass
```
