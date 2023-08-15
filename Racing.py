import pygame
import random
import os
from pygame.locals import *

crong = 500
ccao = 700
nen = pygame.display.set_mode((crong, ccao))

trang = (255,255,255)
den = (0,0,0)
xanh_la = (0, 200, 0)
cam = (255, 103, 0)
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 24)
icon = pygame.image.load('E:\\Racing\\sport-car.png')
pygame.display.set_caption('Racin-Bois')
pygame.display.set_icon(icon)



road = pygame.image.load('E:\\Racing\\road.png')
road = pygame.transform.scale(road, (500,ccao))
tries = pygame.image.load('E:\\Racing\\tree.png')
tree = pygame.transform.scale(tries, (50,50))
car = pygame.image.load('E:\\Racing\\car.png')
main_car = pygame.transform.rotate(car, 180)
e_car = pygame.image.load('E:\\Racing\\car-top-view.png')
obj_car = pygame.transform.rotate(e_car, 180)
def trees(x, y):
    nen.blit(tree, (x,y))
def m_road(x, y):
    nen.blit(road, (x, y))
class char:
    def __init__(self,x,y):

        self.car = nen.blit(main_car, (x,y))
class enemies_car:
    def __init__(self, x, y):
        self.mask = pygame.mask.from_surface(obj_car)
        self.bad_car = nen.blit(obj_car,(x, y-100))

def main():

    max_num_of_enemies = 4
    x = crong/2 - main_car.get_width() / 2
    y = ccao - 100
    vel_y = 2

    road_x = crong/2 - road.get_width()/2
    road_y = ccao - road.get_height()
    tree_x1 = []
    ran_tree_x1 = []
    ran_tree_x2 = []
    tree_x2 = []
    tree_y = []
    ran_tree_y = []
    max_trees = 4
    tree_vel = []

    enemies = []
    enemy_x =[]
    enemy_y = []
    enemy_ran_x = []
    enemy_ran_y = []
    enemy_vel_y = []
    enemy_vel_x = []

    max_num_of_enemies = 5
    spd = 4

    level = 1
    MAX_HP = 5
    progress = 0
    success = 5

    fps = 60
    def thong_so():
        # draw text
        hp = font.render(f"Hp: {MAX_HP}", 1, (255, 0, 0))
        lv = font.render(f"Level: {level}", 1, (255, 0, 0))
        diem_con_lai = font.render(f"con lai: {success-progress}",1, (255,0,0))
        nen.blit(hp, (10, 10))
        nen.blit(lv, (crong - 100, 10))
        nen.blit(diem_con_lai,(10,50))
    # trees sprite
    for i in range(max_trees):
        tree_x1.append(0)
        tree_x2.append(0)
        tree_vel.append(spd/1.8)
        tree_y.append(random.randrange(0, ccao))
        ran_tree_x1.append(random.randrange(0,road_x+20))
        ran_tree_x2.append(random.randrange(road_x + 430, crong))

    for i in range(max_num_of_enemies):
        enemies.append(obj_car)
        enemy_ran_x.append(random.randrange(road_x + 50 ,road_x +400))
        enemy_x.append(0)
        enemy_y.append(random.randrange(-1000,0))
        enemy_vel_x.append(0)
        enemy_vel_y.append(random.randrange(spd,spd*2))
    win = False
    lost = False
        # loooppppppp
    while True:

        keys = pygame.key.get_pressed()
        nen.fill(xanh_la)



        m_road(road_x, road_y)
        m_road(road_x, road_y - road.get_height() * 2 + 100)
        m_road(road_x, road_y-road.get_height() + 50)

        if road_y >=ccao - 30:
            m_road(road_x, road_y)
            road_y = ccao - road.get_height() + 20
        road_y += spd/1.8
        char_car = char(x,y)

        # treessssssss
        for i in range(max_trees):
            trees(tree_x1[i],tree_y[i])
            trees(tree_x2[i],tree_y[i])
            tree_x1[i] = ran_tree_x1[i]
            tree_x2[i] = ran_tree_x2[i]

            if tree_y[i] >= ccao:
                tree_x1[i] = random.randrange(0,road_x+20)
                tree_x2[i] = random.randrange(road_x + 440, crong)
                tree_y[i] = -80
            tree_y[i] += tree_vel[i]

        # black carsssssssss
        for i in range(max_num_of_enemies):

            enemy_car = enemies_car(enemy_x[i],enemy_y[i])
            enemy_x[i] = enemy_ran_x[i]

            enemy_y[i] += enemy_vel_y[i]
            if enemy_x[i] + 30 >= x and enemy_x[i] <= x + 30 and enemy_y[i] - 30 >= y and enemy_y[i] <= y+150:
                MAX_HP -= 1
                enemy_vel_y[i] = random.randrange(spd, round(spd * 1.5))
                enemy_ran_x[i] = random.randrange(road_x + 50, road_x + 400)
                enemy_y[i] = 0

            if enemy_y[i] - 100 >= ccao:
                enemy_vel_y[i] = random.randrange(spd,round(spd*1.5))
                enemy_ran_x[i] = random.randrange(road_x + 50 ,road_x +400)
                enemy_y[i] = 0
                progress +=1
                if progress >= success:
                    win = True
                    level += 1
                    spd += round(spd/3)
                    success += success
                    progress = 0
                    for i in range(max_trees):
                        tree_vel[i] = spd/1.8
                    for i in range(max_num_of_enemies):
                        enemy_vel_y[i] = random.randrange(spd, round(spd * 1.5))
                        enemy_ran_x[i] = random.randrange(road_x + 40, road_x + 400)
                        enemy_y[i] =  random.randrange(-1000, 0)

        thong_so()
        if MAX_HP == 0:
            lost = True
        if keys[pygame.K_s] and y + main_car.get_height() < ccao:
            y += spd/1.5
        if keys[pygame.K_a] and x >= road_x + 40:
            x -= spd
        if keys[pygame.K_d] and x<= road_x + 400:
            x += spd
        if keys[pygame.K_w] and y > 0:
            y -= spd
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        while win:

            MAX_HP = 5
            nen.fill(cam)
            win_title = font.render("You win!!", 1, den)
            level_title = font.render(f"Cap Hien Tai La: {level}", 1 , den)
            nen.blit(win_title, (crong/2 - win_title.get_width()/2, ccao/2))
            nen.blit(level_title,(crong/2 - level_title.get_width()/2, ccao/2 + 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN or keys[pygame.K_SPACE]:
                    win = False

        while lost:

            nen.fill(trang)
            win_title = font.render("U lost", 1, den)
            level_title = font.render(f"lv hien tai: {level}", 1 , den)
            nen.blit(win_title, (crong/2 - win_title.get_width()/2, ccao/2))
            nen.blit(level_title,(crong/2 - level_title.get_width()/2, ccao/2 + 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    main()

main()