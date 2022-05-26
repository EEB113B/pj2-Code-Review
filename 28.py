# =========================== Question 1 ===========================
    def move(self):
        if self.dir =="down":   #判斷向下方向
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y+self.g)  #加入新節點
            self.snake.deQueue()                                            #刪掉尾巴
        if self.dir == "up":    #判斷向上方向
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y-self.g)  #加入新節點
            self.snake.deQueue()                                            #刪掉尾巴
        if self.dir =="left":   #判斷向左方向
            self.snake.enQueue(self.snake.rear.x-self.g,self.snake.rear.y)  #加入新節點
            self.snake.deQueue()                                            #刪掉尾巴
        if self.dir == "right": #判斷向右方向
            self.snake.enQueue(self.snake.rear.x+self.g,self.snake.rear.y)  #加入新節點
            self.snake.deQueue()                                            #刪掉尾巴
# =========================== Question 2 ===========================
    def add_tail(self):
        tail=self.snake.front       #tail等於尾巴節點
        new=Node(tail.x,tail.y)     #建立新節點在尾巴命名new
        self.snake.front.pre=new    #尾巴的前一個是new
        new.next=self.snake.front   #new的下一個是尾巴
        self.snake.front=new        #尾巴用new取代
# =========================== Question 3 ===========================
    def eat_body(self):
        tmp=self.snake.rear.pre     #tmp是第一個蛇身
        while tmp!=None:            #tmp不是空的
            if tmp.x==self.snake.rear.x and tmp.y==self.snake.rear.y:   #蛇頭碰到蛇身
                self.snake.front=tmp.next       #tmp的下一個變成尾巴
                self.snake.front.pre=None       #tmp的前一個改成空的
                self.play_effect("eat_body")    #撥放音效
                break
            tmp=tmp.pre                         
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x==self.itemBoxPos[0] and self.snake.rear.y==self.itemBoxPos[1]:   #蛇頭的x等於itemBoxPox這個list的第0項  
                item=self.item_list[random.randrange(len(self.item_list))]                        #蛇頭的y等於itemBoxPox這個list的第1項
                self.backpack.push(item)        #item push進backpack            #item等於在道具列表(self.item_list)內隨機選擇一個道具
                self.itemBoxPos=None            #改道具方塊改成沒有顯現

# =========================== Question 5 ===========================
    def use_item(self):
        self.item=self.backpack.top.item        #用『self.item』儲存堆疊頂端的道具名稱
        if self.item=="BlackHole":              #啟用相對應道具"BlackHole"
            self.item_BlackHole=True            #把該道具的參數調成True
        elif self.item=="Brake":                #啟用相對應道具"Brake"
            self.item_Brake=True
        elif self.item=="FruitBasket":          #啟用相對應道具"FruitBasket"
            self.item_FruitBasket=True
        elif self.item=="Gamble":               #啟用相對應道具"Gamble"
            self.item_Gamble=True
        self.backpack.pop()                     #刪除背包堆疊頂端的道具