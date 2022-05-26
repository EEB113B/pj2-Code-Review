# =========================== Question 1 ===========================
    def move(self):
        
        if self.dir == "right": #當輸入為右
            self.snake.enQueue(self.snake.rear.x+self.g,self.snake.rear.y)  #在蛇頭前插入
            self.snake.deQueue()    #刪除蛇尾
            
        if self.dir == "left":  #當輸入為左
            self.snake.enQueue(self.snake.rear.x-self.g,self.snake.rear.y)  #在蛇頭前插入
            self.snake.deQueue()    #刪除蛇尾
            
        if self.dir == "up":    #當輸入為上
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y-self.g)  #在蛇頭前插入
            self.snake.deQueue()    #刪除蛇尾
            
        if self.dir == "down":  #當輸入為下
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y+self.g)  #在蛇頭前插入
            self.snake.deQueue()    #刪除蛇尾
       
# =========================== Question 2 ===========================
    def add_tail(self):
        
        if self.snake.front.x+self.g == self.snake.front.next.x:        #身體向右移動時
            new = Node(self.snake.front.x-self.g,self.snake.front.y)    #新增蛇尾位置為上一幀的蛇尾
            new.next = self.snake.front                                 #將新蛇尾與舊蛇尾連接
            self.snake.front.pre = new
            self.snake.front = new
            
        if self.snake.front.x-self.g == self.snake.front.next.x:        #身體向左移動時
            new = Node(self.snake.front.x+self.g,self.snake.front.y)    #新增蛇尾位置為上一幀的蛇尾
            new.next = self.snake.front                                 #將新蛇尾與舊蛇尾連接
            self.snake.front.pre = new
            self.snake.front = new
            
        if self.snake.front.y+self.g == self.snake.front.next.y:        #身體向下移動時
            new = Node(self.snake.front.x,self.snake.front.y-self.g)    #新增蛇尾位置為上一幀的蛇尾
            new.next = self.snake.front                                 #將新蛇尾與舊蛇尾連接
            self.snake.front.pre = new
            self.snake.front = new
            
        if self.snake.front.y-self.g == self.snake.front.next.y:        #身體向上移動時
            new = Node(self.snake.front.x,self.snake.front.y+self.g)    #新增蛇尾位置為上一幀的蛇尾
            new.next = self.snake.front                                 #將新蛇尾與舊蛇尾連接
            self.snake.front.pre = new
            self.snake.front = new
            
# =========================== Question 3 ===========================
    def eat_body(self):
        
        tmp = self.snake.rear.pre
        while tmp != None:                                                      #跑過一次身體除了頭部的各節點
            if (self.snake.rear.x == tmp.x) & (self.snake.rear.y == tmp.y):     #檢查頭的位置與身體是否重疊
                self.snake.front = tmp.next                                     #如果重疊，就斷掉接觸到的身體的節點
                self.snake.front.pre = None 
                self.play_effect("eat_body")
                break
            tmp = tmp.pre
            
# =========================== Question 4 ===========================
    def eat_item(self):
        
        if self.itemBoxPos != None:                                                                         #若道具方塊有顯現的話
              if (self.snake.rear.x == self.itemBoxPos[0]) & (self.snake.rear.y == self.itemBoxPos[1]):     #檢查道具箱位置是否與蛇頭重疊
                site = random.randrange(0,4)                                                                #item_list index從0到3
                item = self.item_list[site]                                                                 #從item_list中隨機提取一個
                self.backpack.push(item)                                                                    #將抽到的item放到道具欄頂端
                self.itemBoxPos = None                                                                      #將(self.itemBoxPos的座標重置為None
                self.play_effect("eat_item")

# =========================== Question 5 ===========================
    def use_item(self):
        
        self.item = self.backpack.top.item      #讀取背包頂端的道具
        
        if self.item == "BlackHole":            #對應到相對的道具名稱並啟動
            self.item_BlackHole = True
            
        if self.item ==  "Gamble":
            self.item_Gamble = True
            
        if self.item == "Brake":
            self.item_Brake = True
            
        if self.item == "FruitBasket":
            self.item_FruitBasket = True
            
        self.backpack.pop()                     #刪除已用過的道具