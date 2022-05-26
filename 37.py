# =========================== Question 1 ===========================
    def move(self):
        next_x = self.snake.rear.x      #設新蛇頭座標x
        next_y = self.snake.rear.y      #設新蛇頭座標y
        if self.dir == 'down':
            next_y += 30                #方向向下新蛇頭座標y加30px
            self.snake.enQueue(next_x, next_y)
            self.snake.deQueue()        #刪除蛇尾保持長度
        if self.dir == 'up':
            next_y -=30                 #方向向上新蛇頭座標y減30px
            self.snake.enQueue(next_x, next_y)
            self.snake.deQueue()
        if self.dir == 'right':
            next_x += 30                #方向向右新蛇頭座標x加30px
            self.snake.enQueue(next_x, next_y)
            self.snake.deQueue()
        if self.dir == 'left':
            next_x -=30                 #方向向左新蛇頭座標x減30px
            self.snake.enQueue(next_x, next_y)
            self.snake.deQueue()
            
# =========================== Question 2 ===========================
    def add_tail(self):
        front_x = self.snake.front.x        #取蛇尾座標x
        front_y = self.snake.front.y        #取蛇尾座標y
        if self.snake.front.next.y == front_y:      #判別蛇尾及蛇身倒數第一個位置是否平行
            if self.snake.front.next.x > front_x:   #再判斷當下是向左走還向右走
                front_x -= 30                       #向右走就向左加蛇尾
            else:
                front_x += 30                       #向左走就向右加蛇尾
        if self.snake.front.next.y > front_y:       #判別蛇尾及蛇身倒數第一個位置是否垂直，再判斷當下是向下走還向上走
            front_y -= 30                           #向下走就往上加蛇尾
        if self.snake.front.next.y < front_y:
            front_y += 30                           #向下走就往下加蛇尾
        new_front = Node(front_x, front_y)          #最後再將算完的新的蛇尾x,y利用Node新增一個節點到蛇尾
        new_front.next = self.snake.front
        self.snake.front.pre = new_front
        self.snake.front = new_front
        pass
# =========================== Question 3 ===========================
    def eat_body(self):
        snake_body = self.snake.rear.pre        #蛇身取蛇頭後第一個座標
        while True:
            if snake_body == None:              #若取到None表示已到蛇尾
                    break
            if snake_body.x == self.snake.rear.x and snake_body.y == self.snake.rear.y:     #假設蛇頭的x及y與蛇身的x和y一樣，判定蛇頭碰到蛇身
                new_front = snake_body.next     #將當下取到的座標的前一個座標設為新的蛇尾
                snake_body.pre = None           #斷開當下座標到蛇尾的連結
                snake_body.next = None
                self.snake.front = new_front    #設定新蛇尾
                self.snake.front.pre = None
                self.play_effect("eat_body")
                break
            else:
                snake_body = snake_body.pre     #若非，則繼續判定下個蛇身座標

# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]:   #假如蛇頭xy座標與道具xy座標都相同
                index = random.randrange(0, 3)      #index = 0 ~ 2
                item = self.item_list[index]       
                self.backpack.push(item)         #將道具填到背包中
                self.play_effect("eat_item")
                self.itemBoxPos = None          #將itemBoxPos設為None方便下一格填充

# =========================== Question 5 ===========================
    def use_item(self):
        if self.backpack.top.item == "BlackHole":   #利用item屬性判定此使用的是否為此道具
            self.item = "BlackHole"                 #使用self.item儲存道具做使用
            self.item_BlackHole = True              #將道具參數改為True供下方程式判斷
        if self.backpack.top.item == "Brake":
            self.item = "Brake"
            self.item_Brake = True
        if self.backpack.top.item == "FruitBasket":
            self.item = "FruitBasket"
            self.item_FruitBasket= True
        if self.backpack.top.item == "Gamble":
            self.item = "Gamble"
            self.item_Gamble = True
        self.backpack.pop()                        #使用後刪除top的道具