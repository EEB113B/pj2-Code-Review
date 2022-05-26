# =========================== Question 1 ===========================
    def move(self):
        head_x = self.snake.rear.x
        head_y = self.snake.rear.y
        if self.dir == 'up':       #向上移動
            head_y -= self.g
            self.snake.enQueue(head_x, head_y)
            self.snake.deQueue()
        
        if self.dir == 'down':     #向下移動
            head_y += self.g
            self.snake.enQueue(head_x, head_y)
            self.snake.deQueue()

        if self.dir == 'left':     #向左移動
            head_x -= self.g
            self.snake.enQueue(head_x, head_y)
            self.snake.deQueue()
        
        if self.dir == 'right':    #向右移動
            head_x += self.g
            self.snake.enQueue(head_x, head_y)
            self.snake.deQueue()
# =========================== Question 2 ===========================
    def add_tail(self):
        tail_x = self.snake.front.x  
        tail_y = self.snake.front.y   #尾端座標
        tail_new = Node(tail_x, tail_y)   
        tail_new.next = self.snake.front  
        self.snake.front.pre = tail_new   #增長
        self.snake.front = tail_new       #front往後一個
# =========================== Question 3 ===========================
    def eat_body(self):
        head_x = self.snake.rear.x
        head_y = self.snake.rear.y
        body = self.snake.rear.pre
        while body:
            if head_x == body.x and head_y == body.y:   #判斷有沒有重疊
                body.next.pre = None            #斷開
                self.snake.front = body.next
                self.play_effect("eat_body")            #撥放音效
            bodt = body = body.pre
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]:   #頭和Box重疊即觸發
                p = random.randrange(0,4)     #四種隨機一個
                item_new = self.item_list[p]
                self.backpack.push(item_new)  #得到的加進去
                self.play_effect("eat_item")
                self.itemBoxPos = None

# =========================== Question 5 ===========================
    def use_item(self):
        use = self.backpack.top.item
        if use == 'BlackHole':    #使用黑洞
            self.item = 'BlackHole'    #呼叫黑洞
            self.item_BlackHole = True
            self.backpack.pop()      #用完丟掉

        elif use == 'Brake':      #使用煞車
            self.item_Brake = True
            self.backpack.pop()   #用完丟掉

        elif use == 'FruitBasket':  #使用水果籃
            self.item_FruitBasket = True
            self.backpack.pop()   #用完丟掉

        elif use == 'Gamble':    #使用賭博
            self.item_Gamble = True
            self.backpack.pop()   #用完丟掉

        self.backpack.top = None