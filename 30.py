# =========================== Question 1 ===========================
    def move(self):
        if direction == up:
            newHead = {'x': snake_coords[HEAD]['x'], 'y': snake_coords[HEAD]['y'] - 1}
        elif direction == down:
            newHead = {'x': snake_coords[HEAD]['x'], 'y': snake_coords[HEAD]['y'] + 1}
        elif direction == left:
            newHead = {'x': snake_coords[HEAD]['x'] - 1, 'y': snake_coords[HEAD]['y']}
        elif direction == right:
            newHead = {'x': snake_coords[HEAD]['x'] + 1, 'y': snake_coords[HEAD]['y']}

        snake_coords.insert(0, newHead)
# =========================== Question 2 ===========================
    def add_tail(self):
        self.body.append(self.last_body[-1])
# =========================== Question 3 ===========================
    def eat_body(self):
        # 1. 判斷是否有身體
        if self.body_list:
            head = self.body_list[0].copy()
        else:
            head = pygame.Rect(-CELL_SIZE, 0, CELL_SIZE, CELL_SIZE)

        # 2. 根據運動方向，調整 head 的位置
        if self.dir == pygame.K_RIGHT:
            head.x += CELL_SIZE
        elif self.dir == pygame.K_LEFT:
            head.x -= CELL_SIZE
        elif self.dir == pygame.K_UP:
            head.y -= CELL_SIZE
        elif self.dir == pygame.K_DOWN:
            head.y += CELL_SIZE

        # 3. 將蛇頭插入到身體列表第 0 項
        self.body_list.insert(0, head)
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話

# =========================== Question 5 ===========================
    def use_item(self):
        for event in pygame.event.get():  # 遍歷同一時刻發生的事件列表
                    if event.type == pygame.QUIT:  # 判斷退出事件
                        return
                    elif event.type == pygame.KEYDOWN:  # 判斷按鍵事件
                        if event.key == pygame.K_ESCAPE:
                            return
                        elif event.key == pygame.K_SPACE:
                            if self.is_game_over:
                                self.reset_game()
                            else:
                                self.is_pause = not self.is_pause