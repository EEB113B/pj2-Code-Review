# =========================== Question 1 ===========================
    def move(self):                 # 根據方向移動蛇的坐標
        if self.dir == 'right': 
            cur = self.snake.rear   # cur(目前節點)設為蛇頭節點
            x = cur.x               # 將鍵盤觸發當下時的蛇頭座標assign給暫存座標
            y = cur.y
            cur.x = cur.x + self.g  # 蛇頭節點每幀向右移動30px                                 
                                    # !蛇頭是佇列末節點
            
        elif self.dir == 'up':  
            cur = self.snake.rear
            x = cur.x
            y = cur.y
            cur.y = cur.y - self.g  # 蛇頭節點每幀向上移動30px
        elif self.dir == 'left':
            cur = self.snake.rear
            x = cur.x
            y = cur.y
            cur.x = cur.x - self.g  # 蛇頭節點每幀向左移動30px
        elif self.dir == 'down':  
            cur = self.snake.rear
            x = cur.x
            y = cur.y
            cur.y = cur.y + self.g  # 蛇頭節點每幀向下移動30px

        while cur.pre:              # 當有前一節點(有前一節身體)
                                    # 身體承接上一節點的節點座標
                tmp_x = cur.pre.x
                tmp_y = cur.pre.y   # 前一節的節點座標(承接前)
                cur.pre.x = x       # 承接
                cur.pre.y = y       # 承接
                cur = cur.pre       # 更改目前節點
                x = tmp_x        
                y = tmp_y   # 更改暫存節點承接前的x座標tmp_x  
# =========================== Question 2 ===========================
    def add_tail(self): # 加一個節點到玩家蛇的尾端(此方法是在蛇吃掉食物的時候被呼叫)
        # 在玩家蛇的尾端(front)新增一個節點
        # 新節點的座標要往蛇尾的方向延伸
        
        tail_dir_x = self.snake.front.next.x - self.snake.front.x   # 用座標判斷左右延伸的方向
        tail_dir_y = self.snake.front.next.y - self.snake.front.y   # 用座標判斷上下延伸的方向

        extend_left  = self.snake.front.x - self.g                  # 向蛇尾左邊延伸一個新節點
        extend_right = self.snake.front.x + self.g                  # 向蛇尾右邊延伸一個新節點
        extend_up = self.snake.front.y - self.g                     # 向蛇尾的上方延伸一個新節點
        extend_down = self.snake.front.y + self.g                   # 向蛇尾的下方延伸一個新節點


        if tail_dir_x >0:# 向右延伸一個像素，上下不變
            new = Node(extend_right , self.snake.front.y)
            new.next = self.snake.front
            self.snake.front.pre = new
            self.snake.front = new # 將蛇尾指向新節點
        elif tail_dir_x <0:# 向左延伸一個像素 ， 上下不變
            new = Node(extend_left , self.snake.front.y)
            new.next = self.snake.front
            self.snake.front.pre = new
            self.snake.front = new
        elif tail_dir_y >0:# 向上延伸一個像素 ， 左右不變
            new = Node(self.snake.front.x , extend_up)
            new.next = self.snake.front
            self.snake.front.pre = new
            self.snake.front = new
        elif tail_dir_y <0:# 向下延伸一個像素 ， 左右不變
            new = Node(self.snake.front.x , extend_down)
            new.next = self.snake.front
            self.snake.front.pre = new
            self.snake.front = new

# =========================== Question 3 ===========================

    def eat_body(self):                 # 吃到玩家蛇的身體
        cur = self.snake.rear.pre       # 將cur設定為目前的蛇身

        while cur:                      # 檢查蛇身的每個節點
            if self.snake.rear.x == cur.x and self.snake.rear.y == cur.y: # 如果蛇頭撞到蛇身當下的蛇身節點
                                        # 從蛇尾開始刪除佇列元素，直到刪掉被撞的蛇身節點
                while self.snake.front !=cur.next:
                    self.snake.deQueue()
                break                   # 刪完後，蛇尾也變成了cur.next(被撞節點的前一節)，並跳出while
            
            else:                       # cur蛇身沒被撞到
                cur = cur.pre           # 將cur指向下一關節

# =========================== Question 4 ===========================
    def eat_item(self): # 吃到道具方塊(黃色問號)即獲得道具

        if self.itemBoxPos != None: # 若道具方塊有顯現的話
                                    # 判斷蛇頭是否吃到道具
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]:
                # print('吃到道具')
                self.play_effect("eat_item")
                # 隨機指定道具
                random_item = random.randrange(0,3)
                # print(self.item_list[random_item])
                # 放入背包堆疊
                self.backpack.push(self.item_list[random_item])
                self.itemBoxPos = None # 重置道具座標
                
# =========================== Question 5 ===========================
    def use_item(self): # 使用道具
        self.item = self.backpack.top.item # item是背包最上層的道具名稱
        if self.item == "BlackHole":    # 黑洞
            self.item_BlackHole = True  # 啟動道具
            self.backpack.pop()         # 消耗此道具

        elif self.item == "Gamble":       # 機率賭博
            self.item_Gamble =True      # 啟動道具
            self.backpack.pop()

        elif self.item == "FruitBasket":  # 水果噴發
            self.backpack.printStack()  # 啟動道具
            self.item_FruitBasket = True
            self.backpack.pop()

        elif self.item == "Brake":        # 煞車
            self.backpack.printStack()  # 啟動道具
            self.item_Brake = True
            self.backpack.pop()