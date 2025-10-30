class RecentCounter:
    """
    [1]
     1,
    [1, 100]
     2
    [1, 100, 3001]
        3
    [100, 3001, 3002 ]
    3
    first try:
     __init__
     q = deque([])
    ping: 
        q.append(t)
        while t-3000 < q[0] :
            q.popleft()
        return len(q)
    """
    def __init__(self):
        self. q = deque([])

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q and (t-3000) > self.q[0]:
            self.q.popleft()
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)