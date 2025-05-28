from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        cur = head
        oldCopy={None:None}
        while cur:
            oldCopy[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            node = oldCopy[cur]
            node.next = oldCopy[cur.next]
            node.random = oldCopy[cur.random]
            cur = cur.next
        
        return oldCopy[head]

        