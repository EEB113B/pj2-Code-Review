# =========================== Question 1 ===========================
    def move(self):
        head_x = self.snake.rear.x #原本頭的x
        head_y = self.snake.rear.y #原本頭的y
        if self.dir == 'right':
            head_x = head_x + self.g #將頭的x增加(代表往右)
        if self.dir == 'left':
            head_x = head_x - self.g #將頭的x減少(代表往左)
        if self.dir == 'up':
            head_y = head_y - self.g #將頭的y減少(代表往上)
        if self.dir == 'down':
            head_y = head_y + self.g #將頭的y增加(代表往下)
        self.snake.enQueue(head_x,head_y) #以新的x,y新增一個節點
        self.snake.deQueue() #把尾巴刪掉
# =========================== Question 2 ===========================
    def add_tail(self):
        front_x = self.snake.front.x 
        front_y = self.snake.front.y #63、64行為原本尾巴的x,y
        front_next_x = self.snake.front.next.x 
        front_next_y = self.snake.front.next.y #65、66行為原本尾巴.next的x,y
        x = front_x
        y = front_y
        if front_x > front_next_x: #如果尾巴在尾巴.next的右邊，代表新的節點要加在尾巴右邊
            x = front_x + self.g
        if front_x < front_next_x: #如果尾巴在尾巴.next的左邊，代表新的節點要加在尾巴左邊
            x = front_x - self.g
        if front_y > front_next_y: #如果尾巴在尾巴.next的下面，代表新的節點要加在尾巴下面
            y = front_y + self.g
        if front_y < front_next_y: #如果尾巴在尾巴.next的上面，代表新的節點要加在尾巴上面
            y = front_y - self.g
            
        new = Node(x,y) #新增節點
        self.snake.front.pre = new #把尾巴.pre指向新節點
        new.next = self.snake.front #把新節點的next指向尾巴
        self.snake.front = new #把尾巴指向新節點(新的尾巴)
# =========================== Question 3 ===========================
    def eat_body(self):
        cur = self.snake.rear.pre #先把頭.pre丟給cur
        while cur != None: 
            if self.snake.rear.x == cur.x and self.snake.rear.y == cur.y: #當頭與身體的x,y相同
                self.play_effect("eat_body")
                self.snake.front = cur.next #因為與頭重疊的節點要刪除，所以該節點.next會變成新的尾巴
                break
            cur = cur.pre #上面if如果不成立才會跑這裡，代表該節點的身體沒有與頭重疊，所以換下一個節點的身體繼續檢查
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]: #如果頭與方塊的x,y相同
                self.play_effect("eat_item")
                self.backpack.push(self.item_list[random.randrange(0, 4, 1)]) #隨機選擇index:0~3，push self.item_list裡的東西進backpack
                self.itemBoxPos = None 

# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top.item #把backpack.top的東西傳給self.item
        if self.item == "BlackHole":
            self.item_BlackHole = True #使用BlackHole
        if self.item == "Brake":
            self.item_Brake = True    #使用Brake
        if self.item == "FruitBasket":
            self.item_FruitBasket = True #使用FruitBasket
        if self.item == "Gamble":
            self.item_Gamble = True #使用Gamble
        self.backpack.pop() #使用完該道具，所以刪除