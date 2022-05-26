# =========================== Question 1 ===========================
    def move(self):
        head = self.snake.rear
        if self.dir == "right":
            self.snake.enQueue(head.x+self.g,head.y) #當按右鍵時，在蛇頭x+self.g座標的地方加新蛇頭，然後刪掉舊蛇尾，避免增加新節點
            self.snake.deQueue()            
        if self.dir == "left":
            self.snake.enQueue(head.x-self.g,head.y) #按左鍵時，在蛇頭x-self.g座標的地方加新蛇頭，然後刪掉舊蛇尾
            self.snake.deQueue()
        if self.dir == "up":
            self.snake.enQueue(head.x,head.y-self.g) #按上下鍵以此類推。
            self.snake.deQueue()
        if self.dir == "down":
            self.snake.enQueue(head.x,head.y+self.g)
            self.snake.deQueue()
# =========================== Question 2 ===========================
    def add_tail(self):
        newtail = Node(self.snake.front.x,self.snake.front.y) #產生一個新尾巴節點
        if self.snake.len()==0:    #當蛇長度為0時，蛇頭為新尾巴
            self.snake.rear = newtail
        else:
            newtail.next = self.snake.front #不為0時舊尾巴變成新尾巴前的節點，新尾巴變成舊尾巴後的節點並且連接。
            self.snake.front.pre = newtail 
            self.snake.front = newtail
# =========================== Question 3 ===========================
    def eat_body(self):
        cur = self.snake.front
        while cur.next!=self.snake.rear: #當尾巴前的身體不等於蛇頭時，假如蛇頭座標等於尾巴前身體的座標
            if self.snake.rear.x == cur.x and self.snake.rear.y == cur.y:  
                self.play_effect("eat_body")
                self.snake.front = cur #新尾巴變成觸碰後的下一個節點，觸碰節點以前為None
                cur.pre = None
            cur = cur.next
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None:
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y ==self.itemBoxPos[1]: #當觸碰方塊時
                item = self.item_list[random.randrange(0,4,1)] #隨機產生道具字串
                self.backpack.push(item) #將字串放進背包
                self.play_effect("eat_item") 
                self.itemBoxPos = None #將方塊座標重設為None # 若道具方塊有顯現的話

# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top.item #儲存堆疊頂端道具名稱
        if self.item == "BlackHole": #當使用道具時
            self.item_BlackHole = True #將預設為False的道具設為True
            self.backpack.pop()       #將道具從背包刪除
        if self.item == "FruitBasket":
            self.item_FruitBasket = True
            self.backpack.pop()
        if self.item == "Gamble":
            self.item_Gamble = True
            self.backpack.pop()
        if self.item == "Brake":
            self.item_Brake = True
            self.backpack.pop()