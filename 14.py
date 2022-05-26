# =========================== Question 1 ===========================
    def move(self):
        n = self.snake.rear                     #將n設為蛇頭的位置
        if(self.dir=="up"):                     #如果按下up
            self.snake.enQueue(n.x, n.y-self.g) #將蛇頭上方的位置添加一個節點
            self.snake.deQueue()                #將蛇尾刪除

        if(self.dir=="down"):                   #如果按下down
            self.snake.enQueue(n.x, n.y+self.g) #將蛇頭下方的位置添加一個節點
            self.snake.deQueue()                #將蛇尾刪除

        if(self.dir=="right"):                  #如果按下right
            self.snake.enQueue(n.x+self.g, n.y) #將蛇頭右方的位置添加一個節點
            self.snake.deQueue()                #將蛇尾刪除
                
        if(self.dir=="left"):                   #如果按下left
            self.snake.enQueue(n.x-self.g, n.y) #將蛇頭左方的位置添加一個節點
            self.snake.deQueue()                #將蛇尾刪除   
# =========================== Question 2 ===========================
    def add_tail(self):
        x = self.snake.front.x      #將x設為蛇尾的x位置
        y = self.snake.front.y      #將y設為蛇尾的y位置
        new = Node(x,y)             #將new設為一個新節點
        new.next = self.snake.front #將new的next設為原本蛇尾
        self.snake.front.pre = new  #將原本蛇尾的pre設為new
        self.snake.front = new      #將new設為新的蛇尾
# =========================== Question 3 ===========================
    def eat_body(self):
        test = self.snake.rear.pre  #設一個test為蛇頭的前面一個節點
        while(test):
            if(test.x==self.snake.rear.x and test.y==self.snake.rear.y):#當test的位置等於蛇頭的位置時
                self.play_effect("eat_body") 
                self.snake.front = test.next    #將蛇尾改成test的下一個節點
                test.next.pre = None            #將test與test.next斷開連結
                break                           #跳出迴圈
            test = test.pre 
        

# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]:#如果蛇頭的位置是道具方塊的位置
                self.play_effect("eat_item")
                r = random.randrange(len(self.item_list))#隨機選擇一個道具
                self.backpack.push(self.item_list[r])    #push到背包裡
                self.itemBoxPos = None                   #將道具方塊刪除
# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top.item  #將self.item設為堆疊頂端的道具名稱
        if self.item == "Brake":            #如果self.item是剎車
            self.item_Brake = True          #開啟剎車
        if self.item == "BlackHole":        #如果self.item是黑洞
            self.item_BlackHole = True      #開啟黑洞
        if self.item == "Gamble":           #如果self.item是賭博
            self.item_Gamble = True         #開啟賭博
        if self.item == "FruitBasket":      #如果self.item是水果籃
            self.item_FruitBasket = True    #開啟水果籃
        self.backpack.pop()                 #刪除背包頂端的道具