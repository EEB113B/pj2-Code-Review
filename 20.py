# =========================== Question 1 ===========================
    def move(self):
        self.snake=[0,0]
        if self.dir == "up":
            self.g = [0, 1]
            self.snake = self.snake + self.g
        if self.dir == "down":
            self.g = [0, -1]
            self.snake = self.snake + self.g
        if self.dir == "left":
            self.g = [-1, 0]
            self.snake = self.snake + self.g
        if self.dir == "right":
            self.g = [1, 0]
            self.snake = self.snake + self.g
# =========================== Question 2 ===========================
    def add_tail(self):
        self.snake.front = -1
        self.snake.rear = -1
        self.snake.rear = self.snake.rear + 1
# =========================== Question 3 ===========================
    def eat_body(self):
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None:
# =========================== Question 5 ===========================
    def use_item(self):