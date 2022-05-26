# =========================== Question 1 ===========================
    def move(self):

        head = self.snake.rear #以head, body為一組
        body = self.snake.rear.pre
        headx = head.x #紀錄元蛇頭的位置
        heady = head.y
        if self.dir == "up": #根據輸入的方向而改變蛇頭的位置
            head.y -= self.g
        elif self.dir == "down":
            head.y += self.g
        elif self.dir == "left":
            head.x -= self.g
        elif self.dir == "right":
            head.x += self.g
        while body: 
            bodyx = body.x #紀錄原蛇身的位置
            bodyy = body.y
            body.x = headx #將原蛇頭的位置指定給蛇身
            body.y = heady
            headx = bodyx #將原蛇身的位置紀錄為蛇頭
            heady = bodyy
            body = body.pre

# =========================== Question 2 ===========================
    def add_tail(self):

        tail = self.snake.front 

        if tail.x == tail.next.x and tail.y > tail.next.y: #判定蛇尾後2個一直線的方向是否為尾巴朝下
            new = Node(tail.x , tail.y + self.g) #紀錄尾巴後方要新增節點的位置(x, y+30)
        elif tail.x == tail.next.x and tail.y < tail.next.y: #判定蛇尾後2個一直線的方向是否為尾巴朝上
            new = Node(tail.x , tail.y - self.g) #紀錄尾巴後方要新增節點的位置(x, y-30)
        elif tail.x < tail.next.x and tail.y == tail.next.y: #判定蛇尾後2個一直線的方向是否為尾巴朝左
            new = Node(tail.x - self.g, tail.y ) #紀錄尾巴後方要新增節點的位置(x-30, y)
        elif tail.x > tail.next.x and tail.y == tail.next.y: #判定蛇尾後2個一直線的方向是否為尾巴朝右
            new = Node(tail.x + self.g, tail.y ) #紀錄尾巴後方要新增節點的位置(x+30, y)

        new.next = self.snake.front #新節點前方指定為蛇尾
        self.snake.front.pre = new #蛇尾後方指定為新節點
        self.snake.front = new #新節點成為新的蛇尾

# =========================== Question 3 ===========================
    def eat_body(self):

        head = self.snake.rear
        body = self.snake.rear.pre

        while body: #檢查每個蛇身
            if head.x == body.x and head.y == body.y: #蛇頭是否碰到蛇身
                self.play_effect("eat_body") 
                while self.snake.front != body.next: #將蛇尾至該節點的蛇身都刪除
                    self.snake.deQueue()
            body = body.pre

# =========================== Question 4 ===========================
    def eat_item(self):

        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]: #蛇頭是否碰到道具方塊
                self.play_effect("eat_item")
                self.backpack.push(self.item_list[random.randrange(3)]) #隨機抽取一個道具放入背包
                self.itemBoxPos = None #刪除道具方塊的位置

# =========================== Question 5 ===========================
    def use_item(self):

        self.item = self.backpack.top.item #儲存頂層道具

        if self.item == "BlackHole": #啟用BlackHole
            self.item_BlackHole = True
        elif self.item == "Brake": #啟用Brake
            self.item_Brake = True
        elif self.item == "FruitBasket": #啟用FruitBasket
            self.item_FruitBasket = True
        elif self.item == "Gamble": #啟用Gamble
            self.item_Gamble = True

        self.backpack.pop() #刪除所使用的頂層道具