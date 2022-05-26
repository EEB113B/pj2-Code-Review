# =========================== Question 1 ===========================
    def move(self):
        head = self.snake.rear     #蛇頭
        body = self.snake.rear.pre #蛇身
        headx = head.x             #標記原始蛇頭位置
        heady = head.y
        if self.dir == "up":       #輸入"上"的指示時
            head.y -= self.g       #改變y座標使蛇頭位置往上
        elif self.dir == "down":   #輸入"下"的指示時
            head.y += self.g       #改變y座標使蛇頭位置往下
        elif self.dir == "left":   #輸入"左"的指示時
            head.x -= self.g       #改變x座標使蛇頭位置往左
        elif self.dir == "right":  #輸入"右"的指示時
            head.x += self.g       #改變x座標使蛇頭位置往右
        while body: 
            bodyx = body.x         #標記原始蛇身位置
            bodyy = body.y
            body.x = headx         #將原本蛇頭位置標記給蛇身
            body.y = heady
            headx = bodyx          #將原本蛇身的位置標記為蛇頭
            heady = bodyy
            body = body.pre   
# =========================== Question 2 ===========================
    def add_tail(self):
        tail = self.snake.front                                  #蛇尾
        if tail.x == tail.next.x and tail.y > tail.next.y:       #標示蛇尾四種移動方向
            new = Node(tail.x , tail.y + self.g)                 #新增節點至其後
        elif tail.x == tail.next.x and tail.y < tail.next.y:
            new = Node(tail.x , tail.y - self.g)
        elif tail.x < tail.next.x and tail.y == tail.next.y:
            new = Node(tail.x - self.g, tail.y )
        elif tail.x > tail.next.x and tail.y == tail.next.y:
            new = Node(tail.x + self.g, tail.y )      
        new.next = self.snake.front                              #將新增的位置標記為蛇尾
        self.snake.front.pre = new
        self.snake.front = new
# =========================== Question 3 ===========================
    def eat_body(self):
        head = self.snake.rear
        body = self.snake.rear.pre
        while body:
            if head.x == body.x and head.y == body.y:    #蛇頭碰到蛇身
                self.play_effect("eat_body")             #撥放音效
                while self.snake.front != body.next:
                    self.snake.deQueue()                 
            body = body.pre

# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]:
                self.play_effect("eat_item")                              #撥放音效
                self.backpack.push(self.item_list[random.randrange(3)])   #放入背包堆疊
                self.itemBoxPos = None                                    #重置座標

# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top.item
        if self.item == "BlackHole":
            self.item_BlackHole = True           #啟用道具"BlackHole"
        elif self.item == "Brake":
            self.item_Brake = True               #啟用道具"Brake"
        elif self.item == "FruitBasket":
            self.item_FruitBasket = True         #啟用道具"FruitBasket" 
        elif self.item == "Gamble":              
            self.item_Gamble = True              #啟用道具"Gamble"
        self.backpack.pop()                      #將堆疊頂端道具從背包移除