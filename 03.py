# =========================== Question 1 ===========================
    def move(self): # 根據方向移動蛇的坐標
        if self.dir == "up": #如果頭的方向朝上
            y = self.snake.rear.y - self.g #把頭的y座標往上移動一格給變數y
            x = self.snake.rear.x #x不變給變數x
            self.snake.enQueue(x, y) #在頭前面的方向加一個節點
            self.snake.deQueue() #把尾巴的節點刪掉

        if self.dir == "down":
            y = self.snake.rear.y + self.g #把頭的y座標往下移動一格給變數y
            x = self.snake.rear.x #x不變給變數x
            self.snake.enQueue(x, y) #在頭前面的方向加一個節點
            self.snake.deQueue() #把尾巴的節點刪掉

        if self.dir == "left":
            y = self.snake.rear.y #y不變給變數y
            x = self.snake.rear.x - self.g #把頭的x座標往上移動一格給變數x
            self.snake.enQueue(x, y) #在頭前面的方向加一個節點
            self.snake.deQueue() #把尾巴的節點刪掉

        if self.dir == "right":
            y = self.snake.rear.y #y不變給變數y
            x = self.snake.rear.x + self.g #把頭的x座標往下移動一格給變數x
            self.snake.enQueue(x, y) #在頭前面的方向加一個節點
            self.snake.deQueue() #把尾巴的節點刪掉
# =========================== Question 2 ===========================
    def add_tail(self): # 加一個節點到玩家蛇的尾端(此方法是在蛇吃掉食物的時候被呼叫)
        self.snake.reverse() #先將蛇的佇列反轉(蛇頭變成蛇尾)
        if self.dir == "up": #如果蛇頭(原蛇尾)朝上
            y = self.snake.rear.y - self.g #蛇頭(原蛇尾)的y座標往上移一格給變數y
            x = self.snake.rear.x #蛇頭(原蛇尾)的x座標不變給變數x

        if self.dir == "down": #如果蛇頭(原蛇尾)朝下
            y = self.snake.rear.y + self.g #蛇頭(原蛇尾)的y座標往下移一格給變數y
            x = self.snake.rear.x #蛇頭(原蛇尾)的x座標不變給變數x

        if self.dir == "left": #如果蛇頭(原蛇尾)朝左
            y = self.snake.rear.y #蛇頭(原蛇尾)的y座標不變給變數y
            x = self.snake.rear.x - self.g #蛇頭(原蛇尾)的x座標往左移一格給變數x

        if self.dir == "right": #如果蛇頭(原蛇尾)朝右
            y = self.snake.rear.y #蛇頭(原蛇尾)的y座標不變給變數y
            x = self.snake.rear.x + self.g #蛇頭(原蛇尾)的x座標往右移一格給變數x
        self.snake.reverse() #將蛇佇列反轉回原本方向

        new = Node(x, y) #初始化一個節點new
        new.next = self.snake.front #將new的下一個指向蛇尾
        self.snake.front.pre = new #將蛇尾的下一個指向new
        self.snake.front = new #將new變成新蛇尾
# =========================== Question 3 ===========================
    def eat_body(self): # 吃到玩家蛇的身體
        l = self.snake.len() - 1 #計算蛇身的總長減1
        cur = self.snake.rear.pre #將蛇頭的上一個指定給cur
        while cur: #當cur不是None
            if self.snake.rear.x == cur.x and self.snake.rear.y == cur.y: #假如蛇頭和蛇身座標重疊
                for i in range(l): #以被吃蛇身節點到蛇尾的長度為次數
                    self.snake.deQueue() #刪掉蛇尾
                self.play_effect("eat_body")
            else:
                l -= 1 #如果檢查的蛇身沒有被吃，被吃蛇身節點到蛇尾的長度減一
            cur = cur.pre #檢查下一個節點
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]: #假如頭的座標與道具座標重疊
                index = random.randrange(4) #隨機選取道具
                self.backpack.push(self.item_list[index]) #將道具放至背包
                self.itemBoxPos = None #道具從地圖上刪除

# =========================== Question 5 ===========================
    def use_item(self): # 使用道具
        self.item = self.backpack.top.item #用self.item儲存背包堆疊頂端的道具名稱字串
        if self.item == "BlackHole": #如果道具名稱字串是BlackHole
            self.item_BlackHole = True #道具BlackHole設為True代表使用

        if self.item == "Brake": #如果道具名稱字串是Brake
            self.item_Brake = True #道具Brake設為True代表使用

        if self.item == "FruitBasket": #如果道具名稱字串是FruitBasket
            self.item_FruitBasket = True #道具FruitBasket設為True代表使用

        if self.item == "Gamble": #如果道具名稱字串是Gamble
            self.item_Gamble = True #道具Gamble設為True代表使用
        
        self.backpack.pop()