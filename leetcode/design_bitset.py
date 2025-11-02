class Bitset:
    """
    bitset 5 = 0000
    F 3 True 0001
    F 1 True 0101 
    Flip 1010
    All False 1010
    U True 0010
    C 1 0010
    toString 0010

    first try:
    init:
        size, count, is_fliped, bs
    fix:
       if bs[i]=="1" and not is_fliped:
        return False 
       count +=1
    unfix
        if bs[i]=="0" and not is_fliped:
            return False
        count -=1    
    all:
        return count == size
    one:
        return count >0
    toString:
        if not is_fliped:
            return bs
        return "".join("1" if v=="0" else "0" for v in bs)
    """
    def __init__(self, size: int):
        self.size = size
        self.co = 0 
        self.is_fliped = False
        self.bs = ["0" for _ in range(size)]

    def fix(self, idx: int) -> None:
        if (self.bs[idx] == "1" and not self.is_fliped) or (self.bs[idx] == "0" and self.is_fliped):
            return
        
        if self.is_fliped:
            self.co -= 1
            self.bs[idx] = "0"
            return
        self.co +=1
        self.bs[idx] = "1"

    def unfix(self, idx: int) -> None:
        if (self.bs[idx] == "0" and not self.is_fliped) or (self.bs[idx] == "1" and self.is_fliped):
            return
        
        if self.is_fliped:
            self.bs[idx] = "1"
            self.co +=1
            return
        self.co -= 1
        self.bs[idx] = "0"
    
    def flip(self) -> None:
        self.is_fliped = not self.is_fliped

    def all(self) -> bool:
        if not self.is_fliped:
            return self.co==self.size
        return self.co==0

    def one(self) -> bool:
        if not self.is_fliped:
            return self.co > 0
        return self.size-self.co !=0

    def count(self) -> int:
        if self.is_fliped:
            return self.size-self.co
        return self.co
        

    def toString(self) -> str:
        if not self.is_fliped:
            return "".join(v for v in self.bs)
        return "".join("1" if v=="0" else "0" for v in self.bs)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.co()
# param_7 = obj.toString()