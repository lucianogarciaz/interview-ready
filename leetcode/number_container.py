class NumberContainers:
    """
    [10] ->-1
    2:10 ->[ 2:10 ]
    1:10->[ 1:10, 2:10 ]
    3:10->[ 1:10, 2:10, 3:10 ]
    5:10 ->[ 1:10, 2:10, 3:10, 5:10 ]
    10: [ 1:10, 2:10, 3:10, 5:10 ] -> 1
    1:20->[ 1:20, 2:10, 3:10, 5:10 ]
    

    first try:
    init:
        map_index:{}
        map_value:{}
    
    change():
        2:10 ->map_index:{2:10}, map_value:{10:[2]}
        1:10->map_index:{1:10, 2:10}, map_value:{10:[1,2]}
        3:10->map_index:{1:10, 2:10, 3:10}, map_value:{10:[1,2,3]}
        5:10 ->map_index:{1:10, 2:10, 3:10, 5:10}, map_value:{10:[1,2,3,5]}
        10: map_value[10][0]
        1:20->map_index:{1:10, 2:10, 3:10, 5:10}, map_value:{20:[1], 10:[2,3,5]}
        if index not in map_index:
            map_index[index] = number
        else:
            prev_number = map_index[index]
            map_index[index] = number
            # remove prev number
            i = bisect.bisect_left(map_value[prev_number])
            del map_value[prev_number][i]
        
        if number not in map_value:
                map_value[number] = [index]
        else
            bisect.insort(map_value[number],index)

    """
    def __init__(self):
        self.map_index = {}
        self.map_value = {}        

    def change(self, index: int, number: int) -> None:
        if index not in self.map_index:
            self.map_index[index] = number
        else:
            prev_number = self.map_index[index]
            self.map_index[index] = number
            i = bisect.bisect_left(self.map_value[prev_number],index)
            del self.map_value[prev_number][i]
            if not self.map_value[prev_number]:
                del self.map_value[prev_number]
        
        if number not in self.map_value:
            self.map_value[number] = [index]
        else:
            bisect.insort(self.map_value[number],index)


    def find(self, number: int) -> int:
        if number not in self.map_value:
            return -1
        return self.map_value[number][0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)


class NumberContainersWithHeap:
    """
    [10] ->-1
    2:10 ->[ 2:10 ]
    1:10->[ 1:10, 2:10 ]
    3:10->[ 1:10, 2:10, 3:10 ]
    5:10 ->[ 1:10, 2:10, 3:10, 5:10 ]
    10: [ 1:10, 2:10, 3:10, 5:10 ] -> 1
    1:20->[ 1:20, 2:10, 3:10, 5:10 ]
    

    first try:
    init:
        map_index:{}
        map_value:{}
    
    change():
        2:10 ->map_index:{2:10}, map_value:{10:[2]}
        1:10->map_index:{1:10, 2:10}, map_value:{10:[1,2]}
        3:10->map_index:{1:10, 2:10, 3:10}, map_value:{10:[1,2,3]}
        5:10 ->map_index:{1:10, 2:10, 3:10, 5:10}, map_value:{10:[1,2,3,5]}
        10: map_value[10][0]
        1:20->map_index:{1:10, 2:10, 3:10, 5:10}, map_value:{20:[1], 10:[2,3,5]}
        if index not in map_index:
            map_index[index] = number
        else:
            prev_number = map_index[index]
            map_index[index] = number
            # remove prev number
            i = bisect.bisect_left(map_value[prev_number])
            del map_value[prev_number][i]
        
        if number not in map_value:
                map_value[number] = [index]
        else
            bisect.insort(map_value[number],index)

    """
    def __init__(self):
        self.map_index = {}
        self.map_value = {}

    def change(self, index: int, number: int) -> None:
        self.map_index[index] = number
        if number not in self.map_value:
            self.map_value[number] = []
        heapq.heappush(self.map_value[number],index)


    def find(self, number: int) -> int:
        if number not in self.map_value:
            return -1
        heap = self.map_value[number]
        while heap:
            cand = heap[0]
            if self.map_index.get(cand) == number:
                return cand
            heapq.heappop(heap)
        return -1 
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)