# =========================== Question 1 ===========================
    def move(self):
        head = self.snake.rear      #以head body為一組
        body = self.snake.rear.pre
        headx = head.x              #紀錄元蛇頭的位置
        heady = head.y
        if self.dir == "up":        #根據輸入的方向而改變蛇頭的位置
            head.y -= self.g
        elif self.dir == "down":
            head.y += self.g
        elif self.dir == "left":
            head.x -= self.g
        elif self.dir == "right":
            head.x += self.g
        while body: 
            bodyx = body.x          #紀錄原蛇身的位置
            bodyy = body.y
            body.x = headx          #將原蛇頭的位置指定給蛇身
            body.y = heady
            headx = bodyx           #將原蛇身的位置紀錄為蛇頭
            heady = bodyy
            body = body.pre      

# =========================== Question 2 ===========================
    def add_tail(self):
        tail = self.snake.front
        if tail.x == tail.next.x and tail.y > tail.next.y:
            new = Node(tail.x , tail.y + self.g)
        elif tail.x == tail.next.x and tail.y < tail.next.y:
            new = Node(tail.x , tail.y - self.g)
        elif tail.x < tail.next.x and tail.y == tail.next.y:
            new = Node(tail.x - self.g, tail.y )
        elif tail.x > tail.next.x and tail.y == tail.next.y:
            new = Node(tail.x + self.g, tail.y )      
        new.next = self.snake.front
        self.snake.front.pre = new
        self.snake.front = new

# =========================== Question 3 ===========================
    def eat_body(self):
        head = self.snake.rear
        body = self.snake.rear.pre
        while body:
            if head.x == body.x and head.y == body.y:
                self.play_effect("eat_body")
                while self.snake.front != body.next:
                    self.snake.deQueue()
            body = body.pre

# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None:
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]:
                self.play_effect("eat_item")
                self.backpack.push(self.item_list[random.randrange(3)])
                self.itemBoxPos = None
# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top.item
        if self.item == "BlackHole":
            self.item_BlackHole = True
        elif self.item == "Brake":
            self.item_Brake = True
        elif self.item == "FruitBasket":
            self.item_FruitBasket = True
        elif self.item == "Gamble":
            self.item_Gamble = True
        self.backpack.pop()