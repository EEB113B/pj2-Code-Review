# =========================== Question 1 ===========================
    def move(self):
        if self.dir == "up": #如果偵測到up，在蛇頭(rear)上面加一節
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y - self.g)
            self.snake.deQueue()#在蛇尾(front)拿掉一節
        if self.dir == "down":#如果偵測到down，在蛇頭(rear)下面面加一節
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y + self.g)
            self.snake.deQueue()#在蛇尾(front)拿掉一節
        if self.dir == "left":#如果偵測到left，在蛇頭(rear)左邊面加一節
            self.snake.enQueue(self.snake.rear.x - self.g, self.snake.rear.y)
            self.snake.deQueue()#在蛇尾(front)拿掉一節
        if self.dir == "right":#如果偵測到right，在蛇頭(rear)右邊面加一節
            self.snake.enQueue(self.snake.rear.x + self.g, self.snake.rear.y)
            self.snake.deQueue()#在蛇尾(front)拿掉一節
# =========================== Question 2 ===========================
    def add_tail(self):
        self.snake.reverse()    #因為反轉了 所以enQueue位子與原本相反!(原本加self.g變成減self.g)
        if self.dir == "up":#如果吃到食物時方向向上，就在蛇尾(注意:因為反轉了，此時是rear)加一節
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y+self.g)
        elif self.dir == "down": #$由上面解釋以此類推...
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y-self.g)
        elif self.dir == "left":
            self.snake.enQueue(self.snake.rear.x+self.g, self.snake.rear.y)
        elif self.dir == "right":
            self.snake.enQueue(self.snake.rear.x-self.g, self.snake.rear.y)
        self.snake.reverse()#反轉回來 
# =========================== Question 3 ===========================
    def eat_body(self):
        test=self.snake.rear.pre    #test為蛇頭的第二節(會慢慢往下找)
        while test :
            if(self.snake.rear.x == test.x and self.snake.rear.y == test.y):#如果蛇頭跟test位子一樣，就把後面的刪掉
                test=test.next  #先把test移到重複位子節點的前一個
                self.play_effect("eat_body")    #播放音效
                while(self.snake.front != test): #刪除後面的節點
                    self.snake.deQueue()
            else:
                test = test.pre #往下找
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if(self.itemBoxPos[0] == self.snake.rear.x and self.itemBoxPos[1] == self.snake.rear.y):#若蛇頭與道具位子一樣(代表吃到道具)
                item_len=len(self.item_list)
                num=random.randrange(item_len)% item_len    #從0~list的長度-1中隨機取一個數字num
                self.backpack.push(self.item_list[num])     #把list中第num個的值push進背包
                self.play_effect("eat_item")    #播放音效
                self.itemBoxPos = None #重設成None
   
# =========================== Question 5 ===========================
    def use_item(self):
        # "BlackHole", "Brake", "FruitBasket", "Gamble"
        self.item = self.backpack.top.item  #把背包堆疊頂端(最新拿到)的道具儲存在self.item裡面
        if self.item == "BlackHole":        #如果self.item是黑洞，就啟用相對應道具
            self.item_BlackHole = True      
        if self.item == "Brake":            #以此類推...
            self.item_Brake = True
        if self.item == "FruitBasket":
            self.item_FruitBasket = True
        if self.item == "Gamble":
            self.item_Gamble = True
        self.backpack.pop()         #刪除堆疊頂端的道具