class Allocator:
    def __init__(self, n: int):
        self.arr = [None] * n
        self.map_ids = {}
        self.n = n
        """
        [-,-,-,-,-,-,-,-,-,-]
        allocate(1,1) -> 0
        [1,-,-,-,-,-,-,-,-,-]
        allocate(1,2) -> 1
        [1,2,-,-,-,-,-,-,-,-]
        allocate(1,3) -> 2
        [1,2,3,-,-,-,-,-,-,-]
        freeMemory(2) -> 1
        [1,-,3,-,-,-,-,-,-,-]
        allocate(3, 4) -> 3
        [1,-,3,4,4,4,-,-,-,-]
        loc.allocate(1, 1) -> 1
        [1,1,3,4,4,4,-,-,-,-]
        freeMemory(1) -> 2
        [-,-,3,4,4,4,-,-,-,-]
        allocate(10, 2) -> -1
        [-,-,3,4,4,4,-,-,-,-]
        freeMemory(7) -> 0
        [-,-,3,4,4,4,-,-,-,-]

        first iteration:
        init:
            arr = [], n, map_ids:{mID:[2,4,5]}
        
        findLeftMost():
            i = 0
            j=0
            
            while i < n:
                while j< n and not arr[j]:
                    if j-i == size-1:
                        return i
                    j+=1
                j+=1
                i =j
            return -1
        
        allocate:
            pos = _findLeftMost()
            for i in range(size):
                arr[size+pos] = mid
            return pos


        free:
            mID not map_ids: return 0
            map_ids[mId]: loop: del arr[pos] count +=1
            return count
        
        second iteration:
        init:
            arr = [], n, map_ids:{mID:[2,4,5]}
        
          allocate:
            0 -> first element
            [1,2,3,4,5] 4-4 -1 = -1  
            if n - ult_pos = 5:
        """  
    
    
    def _findLeftMost(self, size)->int:
        count = 0
        start = 0
        for i in range(self.n):
            if self.arr[i] is None:
                count +=1
                if count == size:
                    return start
            else:
                count=0
                start = i+1
        return -1


    def allocate(self, size: int, mID: int) -> int:
        pos = self._findLeftMost(size)
        if pos == -1:
            return -1
        elem = self.map_ids.get(mID, [])
        for i in range(pos, size+pos):
            self.arr[i]=mID
            elem.append(i)
        self.map_ids[mID] = elem

        return pos

    def freeMemory(self, mID: int) -> int:
        if mID not in self.map_ids:
            return 0
        elem = self.map_ids[mID]
        for i in elem:
            self.arr[i] = None
        del self.map_ids[mID]
        return len(elem)
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)