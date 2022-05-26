# =========================== Question 1 ===========================
    def move(self):
        if(self.dir == "right"):                     #判斷方向是否向右
            rear_x = self.snake.rear.x               #蛇頭X座標
            rear_y = self.snake.rear.y               #蛇頭Y座標
            self.snake.enQueue(rear_x+self.g, rear_y)#蛇頭前進方向加一個節點
            self.snake.deQueue()                     #刪除蛇尾節點
        if(self.dir== "left"):                       #判斷方向是否向左
            rear_x = self.snake.rear.x               #蛇頭X座標
            rear_y = self.snake.rear.y               #蛇頭Y座標
            self.snake.enQueue(rear_x-self.g, rear_y)#蛇頭前進方向加一個節點
            self.snake.deQueue()                     #刪除蛇尾節點
        if(self.dir == "up"):                        #判斷方向是否向上
            rear_x = self.snake.rear.x               #蛇頭X座標
            rear_y = self.snake.rear.y               #蛇頭Y座標
            self.snake.enQueue(rear_x, rear_y-self.g)#蛇頭前進方向加一個節點
            self.snake.deQueue()                     #刪除蛇尾節點
        if(self.dir == "down"):                      #判斷方向是否向下
            rear_x = self.snake.rear.x               #蛇頭X座標
            rear_y = self.snake.rear.y               #蛇頭Y座標
            self.snake.enQueue(rear_x, rear_y+self.g)#蛇頭前進方向加一個節點
            self.snake.deQueue()                     #刪除蛇尾節點
# =========================== Question 2 ===========================
    def add_tail(self):
        x = self.snake.front.x       #蛇尾X座標
        y = self.snake.front.y       #蛇尾y座標
        new_1 = Node(x,y)            #新節點
        new_1.next = self.snake.front#在蛇尾與新節點連接
        self.snake.front.pre = new_1 
        self.snake.front = new_1     #將新節點設為新蛇尾
# =========================== Question 3 ===========================
    def eat_body(self):
        head_pre = self.snake.rear.pre     #蛇頭後一個節點
        while(head_pre != self.snake.rear):#從head_pre開始檢查是否碰到蛇身
            if(head_pre != None):          #檢查到蛇尾
                if(head_pre.x == self.snake.rear.x and head_pre.y == self.snake.rear.y):#蛇頭碰到蛇身的座標
                    self.snake.front = head_pre  #設定新蛇尾，刪除從結點開始到蛇尾的所有節點
                    self.play_effect("eat_body")
                    break  
            else:
                break                       
            head_pre = head_pre.pre        #依序向後檢查
        

# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]:#蛇頭碰到道具方塊的座標
                self.itemBoxPos = None          #將道具方塊消除
                item_num = random.randint(0,3)  #從四個道具中隨機抽取一個
                item = self.item_list[item_num] #抽到的道具
                self.backpack.push(item)        #將道具放入背包堆疊中
                self.play_effect("eat_item")

# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top.item #背包頂端的道具
        if self.item == 'BlackHole':       #判斷道具是不是黑洞
            self.item_BlackHole = True     #將黑洞的參數設定為True
            self.backpack.pop()            #刪除頂端以使用的道具
            
        elif self.item == 'Brake':         #判斷是是不是煞車
            self.item_Brake = True         #將煞車的參數設定為True
            self.backpack.pop()            #刪除頂端以使用的道具
            
        elif self.item == 'Gamble':        #判斷是是不是賭博
            self.item_Gamble = True        #將賭博的參數設定為True
            self.backpack.pop()            #刪除頂端以使用的道具
            
        elif self.item == 'FruitBasket':   #判斷是是不是水果籃
            self.item_FruitBasket = True   #將水果籃的參數設定為True
            self.backpack.pop()            #刪除頂端以使用的道具