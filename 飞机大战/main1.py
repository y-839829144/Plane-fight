import pygame
from pygame.locals import *
from sys import exit
from plane import Myplane,Enemyplane
from bullet import Bullet
from pygame.sprite import collide_mask

pygame.init()
# 创建一个窗口
w = 480
h = 600
screen = pygame.display.set_mode((w,h))

# 加载资源文件
bg = pygame.image.load('res/images/background.png')
bg_rect = bg.get_rect()
again_btn = pygame.image.load('res/images/again.png')
again_btn_rect = again_btn.get_rect()
again_btn_rect.centerx = bg_rect.centerx
again_btn_rect.y =300
gameover_btn = pygame.image.load('res/images/gameover.png')
gameover_btn_rect = gameover_btn.get_rect()
gameover_btn_rect.centerx = bg_rect.centerx
gameover_btn_rect.y=400

# 全局变量声明
run_flag = True
score = 0
life = 3

def mygame():

    # 初始化标记变量
    clock = pygame.time.Clock()
    counter = 0
    global score
    score = 0
    global life
    life = 3
    
    # 创建精灵实体
    plane = Myplane(w,h)
    bullet_group = pygame.sprite.Group(Bullet(plane.rect))
    enemy_group = pygame.sprite.Group(*[Enemyplane(w,h) for x in range(10)])
    
    while True:
        # 事件检测
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        
        # 绘制背景
        screen.blit(bg,bg_rect)
       


        # 飞机
        plane.update(screen)
        # 子弹
        bullet_group.update(screen)
        # 每循环12次创建一个子弹
        if counter%12 ==0:
            bullet_group.add(Bullet(plane.rect))
        # 敌机
        enemy_group.update(screen)

        # 碰撞检测 （敌机与子弹）
        collide_dict = pygame.sprite.groupcollide(bullet_group,enemy_group,True,False,collide_mask)
        tmp = []
        for i  in collide_dict.values():
            tmp += i
        # 更改敌机状态 
        for i in tmp:
            i.active_flag = False    
        # 计算分数
        score += len(tmp) *100
        print(score)

        if plane.active_flag:
            collide_list = pygame.sprite.spritecollide(plane,enemy_group,False,collide_mask)
            for i in collide_list:
                i.active_flag = False
            life -= len(collide_list)
            if collide_list:
                 plane.active_flag = False
        
        # 完成：
        # 1 飞机与敌机碰撞
        # 2 退出游戏界面 ，实现重新开始游戏
        # 3 完善游戏界面，显示分数和生命值

        
        # 刷新页面
        pygame.display.flip()
        # 计数器+1
        counter +=1 
        # 判断生命值，是否要结束游戏 life = 0
        if life <= 0:
            global run_flag
            run_flag = False
            break
        # 设置帧率    
        clock.tick(30)





def gameover():
   
    screen.blit(bg,bg_rect)
    screen.blit(again_btn,again_btn_rect)
    screen.blit(gameover_btn,gameover_btn_rect)
    pygame.display.flip()

    while True:
        # 事件检测
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONUP:
                # 判断鼠标弹起位置 是否在 暂停键图片区域
                if again_btn_rect.collidepoint(event.pos):
                    global run_flag
                    run_flag = True
                    break
                if gameover_btn_rect.collidepoint(event.pos):
                    exit()
        if run_flag:
            break



if __name__ == '__main__' :
    while True:
        if run_flag:
            mygame()
        else:
            gameover()





