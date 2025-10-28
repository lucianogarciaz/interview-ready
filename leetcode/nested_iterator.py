class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.has_next = self.iterator.hasNext()
        self.next_element = self.iterator.next()

class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """


class NestedIterator:
    def __init__(self, nestedIterator:[NestedIterator]):
        self.nested = []
        self._dfs(nestedIterator)
    
    def _dfs(self, nested):
        if len(nested) == 0:
            return
        if not nested.isInteger():
            self._dfs(nested.getList())
        else:
            self.nested.append(nested.getInteger())
        self._dfs(nested[1:])
    
    def next(self)->int:
        val = self.nested[0]
        self.nested = self.nested[1:]
        return val
    
    def hasNext(self)->bool:
        return True if not self.nested else False


class NestedIterator2:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack= nestedList.getList()[::-1]
    
    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self.stack.extend(top.getList[::-1])

    