# =========================== Question 1 ===========================
    def move(self):

        if self.dir == "right":                                                     # 如果方向向右
            self.snake.enQueue(self.snake.rear.x + self.g,self.snake.rear.y)        # 將頭(rear)的x座標增加self.g，y不動
            self.snake.deQueue()                                                    # 把屁屁(front)節點刪掉
        if self.dir == "left":                                                      # 如果方向向左
            self.snake.enQueue(self.snake.rear.x - self.g,self.snake.rear.y)        # 將頭(rear)的x座標減少self.g，y不動
            self.snake.deQueue()                                                    # 把屁屁(front)節點刪掉
        if self.dir == "up":                                                        # 如果方向向上
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y - self.g)        # 將頭(rear)的y座標減少self.g，x不動
            self.snake.deQueue()                                                    # 把屁屁(front)節點刪掉
        if self.dir == "down":                                                      # 如果方向向下
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y + self.g)        # 將頭(rear)的y座標增加self.g，x不動
            self.snake.deQueue()                                                    # 把屁屁(front)節點刪掉
# =========================== Question 2 ===========================
    def add_tail(self):

        tail2 = Node(self.snake.front.x,self.snake.front.y)                       # 設一個新的節點叫 tail2 
        if self.snake.len()== 0:                                                  # 如果 self.snake 長度為 0 
            self.snake.rear = tail2                                               # 把 tail2 放到 self.snake.rear 裡
            self.snake.front = tail2                                              # 把 tail2 放到 self.snake.front 裡
        else:                                                                     # 否則
            tail2.next = self.snake.front                                         # 把 self.snake.front 放到 tail2.next 裡
            self.snake.front.pre = tail2                                          # 把 tail2 放到 self.snake.front.pre 裡
            self.snake.front = tail2                                              # 再把 tail2 放到 self.snake.front 裡
# =========================== Question 3 ===========================
    def eat_body(self):

        temp = self.snake.rear.pre                                                                          # 設一個 temp 變數來暫存，以便等等檢查是否重疊
        while temp != None:                                                                                 # 如果 temp 有資料，就把除了頭部以外的節點跑一次
            if (self.snake.rear.x == temp.x) & (self.snake.rear.y == temp.y):                               # 檢查頭(rear)的位置與身體是否重疊
                self.snake.front = temp.next                                                                
                self.snake.front.pre = None                                                                 # 重疊了，斷掉接觸到的身體的節點
                self.play_effect("eat_body")                                                                # 撥放音效
                break                                                                                       # 離開迴圈
            temp = temp.pre                                                                                 # temp 繼續往下走
# =========================== Question 4 ===========================
    def eat_item(self):

        if self.itemBoxPos != None:                                                                         # 若道具庫有道具
            if (self.snake.rear.x == self.itemBoxPos[0]) & (self.snake.rear.y == self.itemBoxPos[1]):       # 判斷道具箱位置是否與蛇頭重疊
                location = random.randrange(0,3)                                                            # 隨機給定道具出現的位置
                item = self.item_list[location]                                                             # 將剛剛隨機創出來的位置放進 item 變數裡
                self.backpack.push(item)                                                                    # 再把抽到的道具(在item裡)移至頂端
                self.itemBoxPos = None                                                                      # 最後 self.itemBoxPos 的座標設為None
# =========================== Question 5 ===========================
    def use_item(self):

        self.item = self.backpack.top.item                                                                  # 讀取出背包頂端的道具並且放置到 self.item 變數裡
        if self.item == "BlackHole":                                                                        # 如果為 BlackHole 道具
            self.item_BlackHole = True                                                                      # self.item_BlackHole 設為 True
                                                                                                            
        if self.item ==  "Gamble":                                                                          # 如果為 Gamble 道具
            self.item_Gamble = True                                                                         # self.item_Gamble 設為 True

        if self.item == "Brake":                                                                            # 如果為 Brake 道具
            self.item_Brake = True                                                                          # self.item_Brake 設為 True

        if self.item == "FruitBasket":                                                                      # 如果為 FruitBasket 道具
            self.item_FruitBasket = True                                                                    # self.item_FruitBasket 設為 True

        self.backpack.pop()                                                                                 # 當道具已使用完畢即刪除道具