import pygame
from pygame.locals import *
import sys
import math
import colorsys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("")


#スタート画面
font = pygame.font.SysFont("hgｺﾞｼｯｸmhgpｺﾞｼｯｸmhgsｺﾞｼｯｸm", 40)
text = font.render("正ｎ角形を描画するプログラム", True, (255, 255, 255))
text_blank = font.render("|", True, (255, 255, 255))
count = 0
inputs = ""
returns = True

while returns:
    screen.fill((0, 0, 0))

    text_n = font.render("ｎ =  "+inputs, True, (255, 255,  255))

    screen.blit(text, (120, 150))
    screen.blit(text_n, (320, 300))

    if count <= 5:
        screen.blit(text_blank, (440+len(inputs)*20, 300))
    elif count == 10:
        count = 0


    pygame.display.update()
    pygame.time.wait(100)
    count += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_RETURN:
                returns = False
            else:
                inputs += pygame.key.name(event.key)

inputs = float(inputs)


#メイン画面
n = inputs
angle = 360/n
text = font.render("正"+str(inputs)+"角形", True, (255, 255, 255))

while True:
    screen.fill((0, 0, 0))
    screen.blit(text, (300, 20))

    i, color_h = 1, 0
    x, y = 0, 0
    x_first = math.cos(math.radians(angle))*200
    y_first = math.sin(math.radians(angle))*200
    x_before, y_before = x_first, y_first

    while int(x) != int(x_first) or int(y) != int(y_first):
        color = colorsys.hsv_to_rgb(color_h, 1, 1)
        r, g, b = color[0]*255, color[1]*255, color[2]*255
        x = math.cos(math.radians(angle*(i+1)))*200
        y = math.sin(math.radians(angle*(i+1)))*200
        pygame.draw.line(screen, (r, g, b), (400+x_before, 300-y_before), (400+x, 300-y), 2)
        x_before, y_before = x, y
        i += 1
        color_h += 0.025

    pygame.display.update()
    pygame.time.wait(200)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()