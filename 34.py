# =========================== Question 1 ===========================
    def move(self): 
        count = 0                                
        if self.dir == "right":                 
                x = self.snake.rear.x           
                y = self.snake.rear.y            
                x_next = x + self.g             
                self.snake.enQueue(x_next,y)    
                self.snake.deQueue()            
                count+=1                        

        if self.dir == "down":                     
            while count < 1:                    
                x = self.snake.rear.x           
                y = self.snake.rear.y              
                y_next = y + self.g             
                self.snake.enQueue(x,y_next)    
                self.snake.deQueue()            
                count+=1                        

        if self.dir == "up":                    
            while count < 1:
                x = self.snake.rear.x           
                y = self.snake.rear.y           
                y_next = y - self.g             
                self.snake.enQueue(x,y_next)    
                self.snake.deQueue()            
                count+=1                        

        if self.dir == "left":                  
            while count < 1:
                x = self.snake.rear.x           
                y = self.snake.rear.y           
                x_next = x - self.g             
                self.snake.enQueue(x_next,y)
                self.snake.deQueue()    
                count+=1                        
# =========================== Question 2 ===========================
    def add_tail(self): 
        x = self.snake.front.x                  
        y = self.snake.front.y                  
        new_tail = Node(x,y)                    
        new_tail.next = self.snake.front        
        self.snake.front.pre = new_tail         
        self.snake.front = new_tail             
# =========================== Question 3 ===========================
    def eat_body(self):
        count2 = self.snake.len()                       
        tmp = self.snake.rear.pre                      
        while tmp != None:                             
            head_x = self.snake.rear.x                 
            head_y = self.snake.rear.y                  
            body_x = tmp.x                              
            body_y = tmp.y                              
            if head_x != body_x or head_y != body_y:    
                tmp = tmp.pre                          
                count2 -= 1                             
            if head_x == body_x and head_y == body_y:   
                if count2 > 0:                         
                    self.snake.deQueue()                
                    count2-=1                          
                if count2 == 0:                         
                    self.play_effect("eat_body")       
                    break                              
# ==================================================================

# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None:                    
            head_x = self.snake.rear.x                 
            head_y = self.snake.rear.y                 
            if self.itemBoxPos[0] ==head_x and self.itemBoxPos[1] == head_y:    
                pick = random.randrange(0,4)           
                item = self.item_list[pick]             
                self.backpack.push(item)              
                self.itemBoxPos = None                 

# ==================================================================
# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top                 
        if self.item == "BlackHole":                  
            self.item_BlackHole = True  
        if self.item == "Brake":               
            self.item_Brake = True                     
        if self.item == "FruitBasket":                 
            self.item_FruitBasket = True              
        if self.item == "Gamble":                      
            self.item_Gamble = True                   
        self.backpack.pop()                             
# ==================================================================