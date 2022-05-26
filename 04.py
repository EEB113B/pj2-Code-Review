# =========================== Question 1 ===========================
    def move(self):
        self.snake()
        self.g = 30
        self.dir = "right"
        for i in range(len(self.g) - 1, 0, -1):
            x = self.g[i-1].x
            y = self.g[i-1].y
            self.g[i] = SnakeGame(x, y)

        headx = self.snake.rear.x
        heady = self.snake.rear.y
        
        if self.dir == "down":
            heady += self.g
            self.snake.enQueue(headx, heady)
            self.snake.deQueue()
        if self.dir == "up":
            heady -= self.g
            self.snake.enQueue(headx, heady)
            self.snake.deQueue()
        if self.dir == "left":
            headx -= self.g
            self.snake.enQueue(headx, heady)
            self.snake.deQueue()
        if self.dir == "right":
            headx += self.g
            self.snake.enQueue(headx, heady)
            self.snake.deQueue()
# =========================== Question 2 ===========================
    def add_tail(self):
        self.snake = Queue()
        self.g = 30
        Node(tailx, taily)
        tailx = self.snake.front.x
        taily = self.snake.front.y
        newtail = Node(tailx, taily)
        newtail.next = self.snake.front
        self.snake.front.pre = newtail
        self.snake.front = newtail
# =========================== Question 3 ===========================
    def eat_body(self):
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None:
# =========================== Question 5 ===========================
    def use_item(self):