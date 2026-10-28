class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        # Initialize position at (0,0)
        self.x = 0
        self.y = 0
        # 0: East, 1: North, 2: West, 3: South
        self.d = 0 
        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.dir_names = ["East", "North", "West", "South"]

    def step(self, num: int) -> None:
        # Your perimeter logic
        total = (self.width + self.height - 2) * 2
        num %= total
        
        # Obnoxious Edge Case: If num % total == 0 
        # and the robot has actually moved, it faces "South"
        if num == 0: 
            num = total
            
        for _ in range(num):
            nx, ny = self.x + self.dirs[self.d][0], self.y + self.dirs[self.d][1]
            # If out of bounds, turn 90 degrees counter-clockwise
            while not (0 <= nx < self.width and 0 <= ny < self.height):
                self.d = (self.d + 1) % 4
                nx, ny = self.x + self.dirs[self.d][0], self.y + self.dirs[self.d][1]
            self.x, self.y = nx, ny

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.dir_names[self.d]