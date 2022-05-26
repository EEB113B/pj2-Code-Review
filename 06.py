# =========================== Question 1 ===========================
    def move(self): 
        head_x = self.snake.rear.x
        head_y = self.snake.rear.y
        #分別討論各個方向的x, y值變動
        if self.dir == "up": 
            head_y -= self.g
            self.snake.enQueue(head_x, head_y)
            self.snake.deQueue()
        if self.dir == "down":
            head_y += self.g
            self.snake.enQueue(head_x, head_y)
            self.snake.deQueue()
        if self.dir == "left":
            head_x -= self.g
            self.snake.enQueue(head_x, head_y)
            self.snake.deQueue()
        if self.dir == "right":
            head_x += self.g
            self.snake.enQueue(head_x, head_y)
            self.snake.deQueue()
# =========================== Question 2 ===========================
    def add_tail(self): 
        tail_x = self.snake.front.x
        tail_y = self.snake.front.y
        tail_new = Node(tail_x, tail_y)
        #將新增的尾巴設為新的front
        tail_new.next = self.snake.front
        self.snake.front.pre = tail_new
        self.snake.front = tail_new
# =========================== Question 3 ===========================
    def eat_body(self): 
        head_x = self.snake.rear.x
        head_y = self.snake.rear.y
        body = self.snake.rear.pre
        while body:
            #判斷蛇頭座標是否與身體座標重疊
            if head_x == body.x and head_y == body.y:
                #斷開重疊座標與身體的連接
                body.next.pre = None
                self.snake.front = body.next
                self.play_effect("eat_body")
            body = body.pre
# =========================== Question 4 ===========================
    def eat_item(self):
        #判斷有沒有出現盒子
        if self.itemBoxPos != None:
            #判斷蛇頭座標與盒子座標是否重疊
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]:
                #從道具列表中隨機選出一個道具
                p = random.randrange(0,4)
                item_new = self.item_list[p]
                #新增到背包
                self.backpack.push(item_new)
                self.play_effect("eat_item")
                #刪除盒子
                self.itemBoxPos = None
# =========================== Question 5 ===========================
    def use_item(self): 
        use = self.backpack.top.item

        #判斷是哪一種道具
        #回傳為true之後把該道具從背包移除
        if use == 'BlackHole':
            self.item = 'BlackHole'
            self.item_BlackHole = True
            self.backpack.pop()
        elif use == 'Brake':
            self.item = 'Brake'
            self.item_Brake = True
            self.backpack.pop()
        elif use == 'FruitBasket':
            self.item = 'FruitBasket'
            self.item_FruitBasket = True
            self.backpack.pop()
        elif use == 'Gamble':
            self.item = 'Gamble'
            self.item_Gamble = True
            self.backpack.pop()