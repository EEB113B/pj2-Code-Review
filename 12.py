# =========================== Question 1 ===========================
    def move(self): # 根據方向移動蛇的坐標
        head_x = self.snake.rear.x#蛇頭的X座標
        head_y = self.snake.rear.y#蛇頭的y座標
        if self.dir == 'up':#向上走
            head_y = head_y - self.g   
        if self.dir == 'down':#向上走
            head_y = head_y + self.g
        if self.dir == 'right':#向右走
            head_x = head_x + self.g
        if self.dir == 'left':#向左走
            head_x = head_x - self.g
        self.snake.enQueue(head_x,head_y)#讓身體跟上
        self.snake.deQueue()
# =========================== Question 2 ===========================
    def add_tail(self): # 加一個節點到玩家蛇的尾端(此方法是在蛇吃掉食物的時候被呼叫)
        tmp=self.snake.front#tmp指向尾巴
        new = Node(tmp.x, tmp.y)#新增新節點
        new.next = self.snake.front#新節點next指向原尾巴
        self.snake.front.pre = new#原尾巴pre指向新節點  
        self.snake.front = new#將新節點設為新尾巴
# =========================== Question 3 ===========================
    def eat_body(self): # 吃到玩家蛇的身體
        head_x=self.snake.rear.x#儲存蛇頭的x座標
        head_y=self.snake.rear.y#儲存蛇頭的y座標
        tmp=self.snake.rear.pre#tmp指向蛇頭下一個蛇身
        while tmp:#判定蛇頭是否碰到蛇身
            if tmp.x==head_x and tmp.y==head_y:#碰到的況
                while self.snake.front!=tmp:#從尾巴開始刪除直到碰撞位置
                    self.snake.front = self.snake.front.next#設定新尾巴
                    self.snake.front.pre = None#刪除原尾巴
                self.play_effect("eat_body")#音效
                break
            else:#沒碰到的情況
                tmp = tmp.pre#tmp指向下一個
# =========================== Question 4 ===========================
    def eat_item(self): # 吃到道具方塊(黃色問號)即獲得道具
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x==self.itemBoxPos[0] and self.snake.rear.y==self.itemBoxPos[1]:#判定是否碰到道具
                n=random.randrange(0,4)#隨機選擇某樣道具
                self.backpack.push(self.item_list[n])
                self.play_effect("eat_item")#音效
                self.itemBoxPos=None#將碰到的道具刪除
# =========================== Question 5 ===========================
    def use_item(self): # 使用道具
        self.item = self.backpack.top.item#儲存第一個道具
        if self.item == "BlackHole":#啟動BlackHole
            self.item_BlackHole=True
        elif self.item == "Brake":#啟動Brake
            self.item_Brake=True
        elif self.item == "Gamble": #啟動Gamble
            self.item_Gamble=True
        elif self.item == "FruitBasket":#啟動FruitBasket
            self.item_FruitBasket=True
        self.backpack.pop()#將道具刪除