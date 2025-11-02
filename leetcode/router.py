class Router:
    """
    3 
    A [1 4 90] true   [[1 4 90]]
    A [2 5 90] true    [[1 4 90], [2 5 90]]
    A [1 4 90] false   [[1 4 90], [2 5 90]]
    A [3 5 95] true  [[1 4 90], [2 5 90] [3 5 95]]
    A [4 5 104] true [[2 5 90] [3 5 95][4 5 104]]
    F [2 5 90]   [[3 5 95][4 5 104]]
    first try:
    init: o(1) o(1)
        mem, deque(q([s,d,t])), set, deque(timestamp)
    addPacket: (1) (1)
        source_destination_timestamp in set:
            return False
        if mem == len(q):
            q.popleft()
            t.popleft()
        q.append((sdt))
        t.append(t)
        return True
    forwardPacket: o(1)
        if not q:
            return []
        val = q.popleft()
        t.popleft()
        return val
    getCount():o(log n)
        if not t:
            return 0
        start_i = bisect.bisect_left(t, start)
        end_i = bisect.bisect_right(t,end)
        return t[start_i:end_i]

    """
    def __init__(self, memoryLimit: int):
        self.m = memoryLimit
        self.t = deque([])
        self.q = deque([])
        self.dest_map = defaultdict(list)
        self.set = set()
        
    def _getKey(self, source: int, destination: int, timestamp: int)->str:
        return f"{source}_{destination}_{timestamp}"
    
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        new_key = self._getKey(source, destination , timestamp)
        if new_key in self.set:
            return False
        if self.m == len(self.q):
            old_s,old_d,old_t = self.q.popleft()
            key = self._getKey(old_s,old_d,old_t)
            self.set.remove(key)
            self.t.popleft()
            arr = self.dest_map[old_d]
            i = bisect.bisect_left(arr, old_t)
            if i < len(arr) and arr[i] == old_t:
                arr.pop(i)
            if not arr:
                del self.dest_map[old_d]
        self.set.add(new_key)
        self.q.append((source,destination, timestamp))
        self.t.append(timestamp)
        self.dest_map[destination].append(timestamp)
        return True
        
    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        old_s,old_d,old_t = self.q.popleft()
        key = self._getKey(old_s,old_d,old_t)
        self.set.remove(key)
        self.t.popleft()
        arr = self.dest_map[old_d]
        i = bisect.bisect_left(arr, old_t)
        if i < len(arr) and arr[i] == old_t:
            arr.pop(i)
        if not arr:
            del self.dest_map[old_d]
        return [old_s,old_d,old_t]
        
    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if not self.t or self.t and (self.t[-1]<startTime or self.t[0]>endTime):
            return 0
        start_i = bisect.bisect_left(self.dest_map[destination],startTime)
        end_i = bisect.bisect_right(self.dest_map[destination],endTime)
        return end_i - start_i



# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)