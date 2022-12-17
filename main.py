import math
import pygame
import os
from math import atan, pi

DEBUG_MODE = False

PLAY_SPEED = 10
MOUSE_DIST_D = 5

WIDTH = 1200   # Width : 6.75m
WIDTH_IN_METER = 6.75
HEIGHT = 800
APP_NAME = "Eğik Atış"
FPS = 60
BALL_WIDTH = 50
BALL_HEIGHT = 50
BALL_START_X = 30
BALL_START_Y = 340
HOOP_X = 1100
HOOP_Y = 600

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(APP_NAME)

ballPath = os.path.join("image", "ball.png")
BALL_IMAGE = pygame.image.load(ballPath)
BALL = pygame.transform.scale(BALL_IMAGE, (BALL_WIDTH, BALL_HEIGHT))

hoopPath = os.path.join("image", "hoop.png")
HOOP_IMAGE = pygame.image.load(hoopPath)
HOOP = pygame.transform.scale(HOOP_IMAGE, (100, 100))

playerPath = os.path.join("image", "player.png")
PLAYER_IMAGE = pygame.image.load(playerPath)
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (100, 325))
courtBackgroundPath = os.path.join("image", "court-background.png")
COURT_BACKGROUND_IMAGE = pygame.image.load(courtBackgroundPath)




COURT_BACKGROUND = pygame.transform.scale(
    COURT_BACKGROUND_IMAGE, (WIDTH, HEIGHT/2))

pygame.display.set_icon(BALL_IMAGE)

pygame.font.init()

