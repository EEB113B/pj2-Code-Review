# =========================== Question 1 ===========================
    def move(self):

        head_x = self.snake.rear.x             #定義蛇頭的x座標
        head_y = self.snake.rear.y             #定義蛇頭的y座標
        if self.dir == "right":                #如果鍵盤方向向右
            head_x += self.g                   #蛇頭的x座標右移一個單位
            
        if self.dir == "left":                 #如果鍵盤方向向左
            head_x -= self.g                   #蛇頭的x座標左移一個單位
            
        if self.dir == "up":                   #如果鍵盤方向向上
            head_y -= self.g                   #蛇頭的y座標上移一個單位
            
        if self.dir == "down":                 #如果鍵盤方向向下
            head_y += self.g                   #蛇頭的y座標下移一個單位
        
        self.snake.enQueue(head_x,head_y)      #在最後端(rear)加入新節點
        self.snake.deQueue()                   #刪除最前端(front)的節點
# =========================== Question 2 ===========================
    def add_tail(self):

        back_x = self.snake.front.x             #蛇尾的x座標
        back_y = self.snake.front.y             #蛇尾的y座標
        back_x_next = self.snake.front.next.x   #指向蛇尾的下一個x座標位置
        back_y_next = self.snake.front.next.y   #指向蛇尾的下一個y座標位置
        newback_x = back_x + self.g             #新蛇尾的x座標加一個單位(向右延伸)
        newback_y = back_y + self.g             #新蛇尾的y座標加一個單位(向下延伸)
        newback_x1 = back_x - self.g            #新蛇尾的x座標減一個單位(向左延伸)
        newback_y1 = back_y - self.g            #新蛇尾的y座標減一個單位(向上延伸)
        if back_y < back_y_next:                #蛇尾的下一個截點再下面，所以要往上長一個截點
            new = Node(back_x,newback_y1)       #新截點創立
            new.next = self.snake.front         #新節點指向原本的蛇尾
            self.snake.front.pre = new          #原本蛇尾的pre節點指向新節點
            self.snake.front = new
        elif back_y > back_y_next:              #蛇尾的下一個截點再上面，所以要往下長一個截點
            new = Node(back_x,newback_y)        #新截點創立
            new.next = self.snake.front         #新節點指向原本的蛇尾
            self.snake.front.pre = new          #原本蛇尾的pre節點指向新節點
            self.snake.front = new
        elif back_x < back_x_next:              #蛇尾的下一個截點再右邊，所以要往左長一個截點
            new = Node(newback_x1,back_y)       #新截點創立
            new.next = self.snake.front         #新節點指向原本的蛇尾
            self.snake.front.pre = new          #原本蛇尾的pre節點指向新節點
            self.snake.front = new
        elif back_x > back_x_next:              #蛇尾的下一個截點再左邊，所以要往右長一個截點
            new = Node(newback_x,back_y)        #新截點創立
            new.next = self.snake.front         #新節點指向原本的蛇尾
            self.snake.front.pre = new          #原本蛇尾的pre節點指向新節點
            self.snake.front = new
# =========================== Question 3 ===========================
    def eat_body(self):
        head_x = self.snake.rear.x                   #蛇頭的x座標
        head_y = self.snake.rear.y                   #蛇頭的y座標
        tmp = self.snake.rear.pre                    #蛇佇列倒數第2個節點
        while tmp:                                   #從柱列尾端一路往前找
            tmp.x                                    #蛇佇列的x座標
            tmp.y                                    #蛇佇列的y座標
            if tmp.x == head_x and tmp.y ==head_y:   #表示貪吃蛇的頭吃到身體了
                
                self.snake.front = tmp.next
                self.play_effect("eat_body")
                tmp = None                           #刪除從佇列蛇的起始到貪吃蛇頭吃到的位置的節點
            else:
                tmp = tmp.pre                        #繼續往前面節點尋找
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            head_x = self.snake.rear.x                                         #貪吃蛇頭的x座標
            head_y = self.snake.rear.y                                         #貪吃蛇頭的y座標
            if head_x == self.itemBoxPos[0] and head_y == self.itemBoxPos[1]:  #如果吃到道具方塊
                new_item = random.choice(self.item_list)                       #隨機產生一項道具
                self.backpack.push(new_item)                                   #進行堆疊
                self.itemBoxPos = None                                         # 再把道具方塊座標重設成None
                self.play_effect("eat_item")
# =========================== Question 5 ===========================
    def use_item(self):
# ==================================================================
        self.item = self.backpack.top.item     #找堆疊頂端的道具名稱
        if self.item == "BlackHole":
            self.item_BlackHole = True         #使用道具
            self.backpack.pop()                #清掉堆疊
        if self.item == "Gamble":
            self.item_Gamble = True            #使用道具
            self.backpack.pop()                #清掉堆疊
        if self.item ==  "Brake":
            self.item_Brake = True             #使用道具
            self.backpack.pop()                #清掉堆疊
        if self.item == "FruitBasket":
            self.item_FruitBasket = True       #使用道具
            self.backpack.pop()                #清掉堆疊