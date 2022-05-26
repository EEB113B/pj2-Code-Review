# =========================== Question 1 ===========================
    def move(self):
        if self.dir == "up":#向上
            #在蛇頭加入新節點，X座標不變，Y座標減一個單位
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y-self.g)
            #刪除蛇尾節點
            self.snake.deQueue()

        elif self.dir == "down":#向下
            #在蛇頭加入新節點，X座標不變，Y座標加一個單位
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y+self.g)
            #刪除蛇尾節點
            self.snake.deQueue()

        elif self.dir == "left":#向左
            #在蛇頭加入新節點，Y座標不變，X座標減一個單位
            self.snake.enQueue(self.snake.rear.x-self.g,self.snake.rear.y)
            #刪除蛇尾節點
            self.snake.deQueue()

        elif self.dir == "right":#向右
            #在蛇頭加入新節點，Y座標不變，X座標加一個單位
            self.snake.enQueue(self.snake.rear.x+self.g,self.snake.rear.y)
            #刪除蛇尾節點
            self.snake.deQueue()
# =========================== Question 2 ===========================
    def add_tail(self):
        add = Node(self.snake.front.x,self.snake.front.y)
        if self.snake.len() == 0: # 若佇列為空
            self.snake.rear = add
            self.snake.front = add
        else:
            #新節點向後指向原來蛇尾
            add.next = self.snake.front
            #原來蛇尾向前指向新節點
            self.snake.front.pre = add
            #將新節點設為蛇尾
            self.snake.front = add
# =========================== Question 3 ===========================
    def eat_body(self):
        tmp = self.snake.rear.pre#蛇頭前指標
        head_x = self.snake.rear.x#蛇頭X座標
        head_y = self.snake.rear.y#蛇頭Y座標
        while tmp :#從蛇頭前指標開始走訪
            #若與蛇頭座標重疊
            if head_x == tmp.x and head_y == tmp.y:
                #將蛇尾改為重疊部分的下一個
                self.snake.front = tmp.next
                #重疊部分及前、後指標都設為空，斷開身體
                tmp.next = None
                tmp.pre = None
                tmp = None
                self.play_effect("eat_body")
            else:    
                tmp = tmp.pre 
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            head_x = self.snake.rear.x#蛇頭X座標
            head_y = self.snake.rear.y#蛇頭Y座標
            #若蛇頭座標與道具方塊座標重疊
            if head_x == self.itemBoxPos[0] and head_y == self.itemBoxPos[1]:
                #隨機選取0~3
                r = random.randrange(4)
                #將該道具放入背包堆疊
                self.backpack.push(self.item_list[r])
                #道具方塊設空
                self.itemBoxPos = None
                self.play_effect("eat_item")
# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top.item#儲存堆疊頂端的道具名稱
        if self.item == 'BlackHole':
            self.item_BlackHole = True
        if self.item == 'Brake':
            self.item_Brake = True
        if self.item == 'FruitBasket':
            self.item_FruitBasket = True
        if self.item == 'Gamble':
            self.item_Gamble = True
        #使用後刪除
        self.backpack.pop()