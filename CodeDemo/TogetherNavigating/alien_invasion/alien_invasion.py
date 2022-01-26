#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/12 17:44

#武装飞行项目

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from  pygame.sprite import Group

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_heigt)
    )
    pygame.display.set_caption("Alien Invasion")

    #创建一个艘飞船
    ship = Ship(ai_settings,screen)
    #  创建一个用于存储子弹的编组
    bullets = Group()

    #设置背景色
    bg_color = (230,230,230)

    #  开始游戏的主循环
    while True:

        gf.chenk_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()


