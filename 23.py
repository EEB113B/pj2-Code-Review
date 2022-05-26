# =========================== Question 1 ===========================
    def move(self):
        if self.dir == "right":                                                 #如果前進方向往右
            self.snake.enQueue(self.snake.rear.x + self.g,self.snake.rear.y)    #蛇身於右30px加入一蛇身
            self.snake.deQueue()                                                #將蛇尾刪除
        elif self.dir == "left":                                                #如果前進方向往左
            self.snake.enQueue(self.snake.rear.x - self.g,self.snake.rear.y)    #蛇身於左30px加入一蛇身
            self.snake.deQueue()                                                #將蛇尾刪除
        elif self.dir == "up":                                                  #如果前進方向往上
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y - self.g)    #蛇身於上30px加入一蛇身
            self.snake.deQueue()                                                #將蛇尾刪除
        elif self.dir == "down":                                                #如果前進方向往下
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y + self.g)    #蛇尾於下30px加入一蛇身
            self.snake.deQueue()                                                #將蛇尾刪除
# =========================== Question 2 ===========================
    def add_tail(self):
        if self.dir == "right":                                                 #如果前進方向往右            
            self.snake.enQueue(self.snake.rear.x + self.g,self.snake.rear.y)    #蛇身於右30px加入一蛇身           
        elif self.dir == "left":                                                #如果前進方向往左
            self.snake.enQueue(self.snake.rear.x - self.g,self.snake.rear.y)    #蛇身於左30px加入一蛇身
        elif self.dir == "up":                                                  #如果前進方向往上
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y - self.g)    #蛇身於上30px加入一蛇身
        elif self.dir == "down":                                                #如果前進方向往下
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y + self.g)    #蛇身於下30px加入一蛇身
# =========================== Question 3 ===========================
    def eat_body(self):
        
        cur = self.snake.rear.pre                                           #設cur為蛇身
        while cur != None:                                                  #將每一段蛇身都視為cur
            if self.snake.rear.x == cur.x and self.snake.rear.y == cur.y:   #如果蛇頭與蛇身重疊
                self.snake.front = cur.next                                 #將那一段蛇身至蛇尾刪除    
                self.snake.front.pre = None                                 
                self.play_effect("eat_body")                                #撥放吃蛇身音效
                break
            cur = cur.pre
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None:                                                                 #若道具方塊有顯現的話
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]: #如果蛇頭與道具箱重疊
                causal_number = random.randrange(0,4)                                               #亂數抽一數字0~3
                item = self.item_list[causal_number]                                                #依照亂數從list中決定道具
                self.backpack.push(item)                                                            #將道具加入背包
                self.itemBoxPos = None                                                              #刪除道具箱
                self.play_effect("eat_item")                                                        #播放吃道具箱音效
# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top.item                 #將背包最上層道具設為item

        if self.item == "Brake":                           #如果為剎車，啟動剎車
            self.item_Brake = True
            
        if self.item == "BlackHole":                       #如果為黑洞，啟動黑洞
            self.item_BlackHole = True

        if self.item == "FruitBasket":                     #如果為水果籃，啟動水果籃
            self.item_FruitBasket = True

        if self.item == "Gamble":                          #如果為賭博，啟動賭博
            self.item_Gamble = True

        self.backpack.pop()                                #使用道具後刪除道具