# =========================== Question 1 ===========================
    def move(self):
        n=self.snake.len()                      #計算現今蛇長
        tmp=self.snake.front                    #將tmp指向蛇尾

        if  self.dir == "right":                #當輸入為右 ，進入
            for i in range(n-1):                #從蛇尾開始，將下一節蛇體的x座標及y座標複製到現在的位子
                tmp.x=tmp.next.x
                tmp.y=tmp.next.y
                tmp=tmp.next                    #tmp指派到下一節蛇體
            self.snake.rear.x += self.g         #蛇頭的x座標+30px

        if  self.dir == "left":                 #當輸入為左 ，進入
            for i in range(n-1):                #從蛇尾開始，將下一節蛇體的x座標及y座標複製到現在的位子
                tmp.x=tmp.next.x
                tmp.y=tmp.next.y
                tmp=tmp.next                    #tmp指派到下一節蛇體
            self.snake.rear.x -= self.g         #蛇頭的x座標-30px

        if  self.dir == "up":                   #當輸入為上 ，進入
            for i in range(n-1):                #從蛇尾開始，將下一節蛇體的x座標及y座標複製到現在的位子
                tmp.x=tmp.next.x
                tmp.y=tmp.next.y
                tmp=tmp.next                    #tmp指派到下一節蛇體
            self.snake.rear.y -= self.g         #蛇頭的y座標-30px

        if  self.dir == "down":                 #當輸入為下 ，進入
            for i in range(n-1):                #從蛇尾開始，將下一節蛇體的x座標及y座標複製到現在的位子
                tmp.x=tmp.next.x       
                tmp.y=tmp.next.y
                tmp=tmp.next                    #tmp指派到下一節蛇體
            self.snake.rear.y +=self.g          #蛇頭的y座標+30px
# =========================== Question 2 ===========================
    def add_tail(self):
        new = Node((2*(self.snake.front.x)-(self.snake.front.next.x)), (2*(self.snake.front.y)-(self.snake.front.next.y))) #利用九宮格算出對應座標x與y，並建立有此X與Y座標的new節點
        new.next = self.snake.front             #將new節點的next指向原先的蛇尾
        self.snake.front.pre = new              #將原蛇尾的pre由None，指向new這個節點
        self.snake.front = new                  #將尾節點指向new完成尾巴增長
# =========================== Question 3 ===========================
    def eat_body(self):
        cur=self.snake.front                    #將cur指向尾節點
        while True:
            if cur.x==self.snake.rear.x and cur.y==self.snake.rear.y and cur.next!=None:       #如果cur的x與y座標皆相等於蛇頭與cur節點的next不等於None，進入        
                self.snake.front=cur            #將尾節點，變成cur節點
                self.snake.front.pre=None       #將現在的尾節點的pre指向None
                self.play_effect("eat_body")    #撥放音樂
                break                           #跳出迴圈
            if cur.next==None:                  #cur.next若等於None，進入
                break                           #跳出迴圈
            cur=cur.next                        #cur往下一個節點走

        if self.snake.rear.x==self.snake.front.x and self.snake.rear.y==self.snake.front.y:    #如果尾節點等於頭節點
            self.snake.deQueue()                #刪除一個尾節點
            self.play_effect("eat_body")        #撥放音樂
# =========================== Question 4 ===========================
    def eat_item(self):

        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x==self.itemBoxPos[0] and self.snake.rear.y==self.itemBoxPos[1]: #如果頭節點的X與Y座標等於箱子的X與Y座標，進入
                self.play_effect("eat_item")    #撥放音樂 
                self.backpack.push(self.item_list[random.randrange(0,4)])      #將道具存放到背包(self.backpack)中
                self.itemBoxPos=None            #再把道具方塊座標(self.itemBoxPos)重設成None

# =========================== Question 5 ===========================
    def use_item(self):

        self.item=self.backpack.top.item    #利用self.item儲存堆疊頂端的道具名稱
        if self.item=="BlackHole":          #如果道具等於"BlackHole"
            self.item_BlackHole = True      #將self.item_BlackHole設為True
        if self.item=="Brake":              #如果道具等於"Brake"
            self.item_Brake = True      #將self.item_Brake設為True
        if self.item=="FruitBasket":        #如果道具等於"FruitBasket"
            self.item_FruitBasket = True      #將self.item_FruitBasket設為True
        if self.item=="Gamble":             #如果道具等於"Gamble"
            self.item_Gamble = True      #將self.item_Gamble設為True
        self.backpack.pop()             #刪除堆疊頂端的道具