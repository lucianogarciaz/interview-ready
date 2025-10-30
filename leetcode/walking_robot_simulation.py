class Robot:
    """
    0,1   1,1
            ^
            |
    0,0 ->  0,1 

    pos = (0,0)
    dir = 0 ,1 ,2, 3

    first it:
        init: o(1)
            width, height, posX =0 posY=0, dir = 0, dir_map={0: East,1:North,2:South,3:West}
        step:
            iterate num times:
                not nextIsValid():
                    changeDirection
                move()
        getPos o(1)
            return [posX,posY]
        getDir o(1)
            return dir_map[dir] 
                

    """
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos_x = 0
        self.pos_y = 0
        self.dir =0
        self.dir_map = {0: "East", 1:"North", 2: "West",3:"South"}

    def _next_valid(self):
        x = self.pos_x
        y = self.pos_y
        match self.dir:
            case 0:
                x +=1
            case 1:
                y +=1
            case 2:
                x -=1
            case 3:
                y -=1
        if x >= self.width or x <0:
            return False
        if y >= self.height or y <0:
            return False
        return True

    def _move(self):
        match self.dir:
            case 0:
                self.pos_x +=1
            case 1:
                self.pos_y +=1
            case 2:
                self.pos_x -=1
            case 3:
                self.pos_y -=1
    def _change_dir(self):
        self.dir += 1
        if self.dir > 3:
            self.dir = 0

    def step(self, num: int) -> None:
        """
        total_steps = width*2 + height*2
        """
        if num == 0:
            return
        total_steps = (self.width-1)*2 + (self.height-1)*2
        remaining = num
        if num > total_steps:
            remaining = num%total_steps

        if remaining == 0:
            remaining = total_steps
        for i in range(remaining):
            if not self._next_valid():
                self._change_dir()
            self._move()

    def getPos(self) -> List[int]:
        return [self.pos_x, self.pos_y]

    def getDir(self) -> str:
        return self.dir_map[self.dir]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()