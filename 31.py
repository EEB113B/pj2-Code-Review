# =========================== Question 1 ===========================
    def move(self): # 根據方向移動蛇的坐標
        headx = self.snake.rear.x
        heady = self.snake.rear.y
        if self.dir == "up":  #等於up時 
            heady -= self.g  #頭的y座標向上一個單位
            self.snake.enQueue(headx, heady) #把新座標設為蛇頭
            self.snake.deQueue() #刪除蛇尾 平衡蛇身數量

        if self.dir == "down":  
            heady += self.g   #頭的y座標向下一個單位
            self.snake.enQueue(headx, heady)
            self.snake.deQueue()  
        
        if self.dir == "left":  
            headx -= self.g   #頭的x座標向左一個單位
            self.snake.enQueue(headx, heady)
            self.snake.deQueue()  

        if self.dir == "right": 
            headx += self.g   #頭的x座標向右一個單位
            self.snake.enQueue(headx, heady)
            self.snake.deQueue()  
# =========================== Question 2 ===========================
    def add_tail(self): # 加一個節點到玩家蛇的尾端(此方法是在蛇吃掉食物的時候被呼叫)
        tailx = self.snake.front.x #蛇尾的x座標
        taily = self.snake.front.y #蛇尾的y座標
        newtail = Node(tailx, taily) #新增節點
        newtail.next = self.snake.front #將newtail新增在蛇尾前
        self.snake.front.pre = newtail
        self.snake.front = newtail
# =========================== Question 3 ===========================
    def eat_body(self): # 吃到玩家蛇的身體
        headx = self.snake.rear.x
        heady = self.snake.rear.y
        body = self.snake.rear.pre
        while body:
            if headx == body.x and heady == body.y:  #吃到身體時
                body.next.pre = None    #刪除蛇身
                self.snake.front = body.next
                self.play_effect("eat_body")
            body = body.pre
# =========================== Question 4 ===========================
    def eat_item(self): # 吃到道具方塊(黃色問號)即獲得道具
        if self.itemBoxPos != None: # if 道具方塊顯現
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]:  #吃到道具方塊
                p = random.randrange(0,4)  #道具隨機四選一
                item_new = self.item_list[p]
                self.backpack.push(item_new) #加入得到的道具
                self.play_effect("eat_item")
                self.itemBoxPos = None

        

# =========================== Question 5 ===========================
    def use_item(self): # 使用道具
        item = self.backpack.top.item
        if item == 'BlackHole':  
            self.item = 'BlackHole' #呼叫道具
            self.item_BlackHole = True
            self.backpack.pop() #清除道具
        
        if item == 'Brake':  
            self.item = 'Brake' #呼叫道具
            self.item_Brake = True 
            self.backpack.pop() #清除道具       
         
        if item == 'FruitBasket':  
            self.item = 'FruitBasket' #呼叫道具
            self.item_FruitBasket = True
            self.backpack.pop() #清除道具  

        if item == 'Gamble':  
            self.item = 'Gamble' #呼叫道具
            self.item_Gamble = True
            self.backpack.pop() #清除道具  

        self.backpack.top = None