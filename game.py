import pygame

# 初始化游戏
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 加载背景音乐
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.play(-1)

# 设置游戏标题
pygame.display.set_caption("飞机大战")

# 绘制玩家飞机
player_img = pygame.image.load("player.png")
player_rect = player_img.get_rect()
player_rect.centerx = 240
player_rect.bottom = 680

# 绘制敌机
enemy_img = pygame.image.load("enemy.png")
enemy_rect = enemy_img.get_rect()
enemy_rect.centerx = 240
enemy_rect.top = 0

# 绘制子弹
bullet_img = pygame.image.load("bullet.png")
bullet_rect = bullet_img.get_rect()
bullet_rect.centerx = player_rect.centerx
bullet_rect.top = player_rect.top

# 更新元素位置
player_rect.centerx += player_speed
enemy_rect.top += enemy_speed
bullet_rect.top -= bullet_speed

# 将元素绘制到游戏窗口中
screen.blit(player_img, player_rect)
screen.blit(enemy_img, enemy_rect)
screen.blit(bullet_img, bullet_rect)

# 游戏循环
running = True
while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 键盘操作
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.centerx -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.centerx += player_speed
    if keys[pygame.K_SPACE]:
        # 发射子弹
        shoot_bullet()

    # 碰撞检测
    if bullet_rect.colliderect(enemy_rect):
        # 子弹击中敌机
        score += 10

    # 更新元素位置
    enemy_rect.top += enemy_speed
    bullet_rect.top -= bullet_speed

    # 游戏结束判断
    if enemy_rect.colliderect(player_rect):
        running = False

    # 更新游戏窗口
    screen.blit(player_img, player_rect)
    screen.blit(enemy_img, enemy_rect)
    screen.blit(bullet_img, bullet_rect)

    # 更新分数显示
    show_score(score)

    # 更新屏幕显示
    pygame.display.update()

# 游戏结束
pygame.quit()
