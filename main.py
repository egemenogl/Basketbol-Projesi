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

# Yardımcı Fonksiyonlar:



def convertPixelToMeter(n):
    return n / WIDTH * WIDTH_IN_METER




def _translatePos(t):
    return (t[0], HEIGHT - t[1])




def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5




def isMouseOverUI():
    
    testMouseX = pygame.mouse.get_pos()[0] < 230
    
    testMouseY = pygame.mouse.get_pos()[1] < 80
    
    return testMouseX and testMouseY

# Pota





class Hoop:
    
    def getHoopInColliderDimensions(self):
        
        return pygame.Rect(
            
            self.obj.centerx+5, self.obj.y-15, self.width / 6, self.height / 8)
    
    

    def getHoopMetalColliderDimensions(self):
        
        return pygame.Rect
            self.obj.x-5, self.obj.y+15, self.width / 12, self.height / 10)
    
    

    def __init__(self, Debug=False):
        
        _tp = _translatePos((HOOP_X, HOOP_Y))
        
        self.width = HOOP.get_width()
        
        self.height = HOOP.get_height()


        self.obj = pygame.Rect(_tp[0], _tp[1], self.width, self.height)
        
        self.hoopInCollider = self.getHoopInColliderDimensions()
        
        self.hoopMetalCollider = self.getHoopMetalColliderDimensions()
        self.Debug = Debug

    def collisionBoxes(self):
        return [self.hoopInCollider, self.hoopMetalCollider]

    def hoopInBox(self):
        return self.hoopInCollider

    def hoopMetalBox(self):
        return self.hoopMetalCollider

    def pos(self):
        return (self.obj.x, self.obj.y)

    def moveTo(self, x=None, y=None):
        if x:
            self.obj.x = x
            
            self.hoopInCollider = self.getHoopInColliderDimensions()
            
            self.hoopMetalCollider = self.getHoopMetalColliderDimensions()
        if y:
            self.obj.y = y
            
            self.hoopInCollider = self.getHoopInColliderDimensions()
            
            self.hoopMetalCollider = self.getHoopMetalColliderDimensions()
            
    def reset(self):
            _tp = _translatePos((HOOP_X, HOOP_Y))
            
            self.obj = pygame.Rect(_tp[0], _tp[1], self.width, self.height)
            
            self.hoopInCollider = self.getHoopInColliderDimensions()
            
            self.hoopMetalCollider = self.getHoopMetalColliderDimensions()

    def draw(self):
            SCREEN.blit(HOOP, self.pos())
            
            # Hata ayıklama için beyaz kare çiz
            if self.Debug:
                for c in self.collisionBoxes():
                    pygame.draw.rect(SCREEN, (255, 255, 255), c)
                    
                    
                    
     
     # Top:
     class Ball:
         def __init__(self):
              _tp = _translatePos((BALL_START_X, BALL_START_Y))
              self.vx = 0
              self.vy = 0
              self.isMoving = False
              self.obj = pygame.Rect(_tp[0], _tp[1], BALL_WIDTH, BALL_HEIGHT)
        
       

    def move(self, hoop: Hoop):
        
        self.obj.x += self.vx * PLAY_SPEED / FPS
        
        self.obj.y += self.vy * PLAY_SPEED / FPS
        
        self.vy += 9.8 * PLAY_SPEED / FPS

        self.checkCollision(hoop)

        if self.obj.x < 0 or self.obj.x > WIDTH - BALL_WIDTH:
            
            self.vx *= -.8
            
            self.obj.x = max(0, min(self.obj.x, WIDTH - BALL_WIDTH))

        if self.obj.y > HEIGHT:
            
            self.reset()

    def pos(self):
        return (self.obj.x, self.obj.y)

    def reset(self):
        _tp = _translatePos((BALL_START_X, BALL_START_Y))
        self.obj.x = _tp[0]
        self.obj.y = _tp[1]
        self.vx = 0
        self.vy = 0
        self.isMoving = False

    def startMoving(self, mouseX, mouseY):
        self.isMoving = True
        diffX = mouseX - self.obj.x
        diffY = mouseY - self.obj.y
        self.vx = diffX / MOUSE_DIST_D
        self. vy = diffY / MOUSE_DIST_D

    def draw(self):
        
        SCREEN.blit(BALL, self.pos())
        
        def checkBallMovingTowardsHoop(self, hoop: Hoop):
return not self.vx * (self.obj.centerx - WIDTH) + self.vy * (self.obj.centery - hoop.obj.centery) > 0        

    def bounceRelative(self, x, y, hoop: Hoop):
        # Check if the ball is moving towards the hoop
        if not self.checkBallMovingTowardsHoop(hoop):
            return
        
        
            speedNow = (self.vx**2 + self.vy**2)**0.5
        bounceAngle = math.atan2(self.obj.centery - y, self.obj.centerx - x)
        
        self.vx = -speedNow * math.cos(bounceAngle) * 0.9
        
        self.vy = -speedNow * math.sin(bounceAngle) * 0.9

    def checkCollision(self, hoop: Hoop):
        
        hib = hoop.hoopInBox()
        hmb = hoop.hoopMetalBox()
        
        if self.obj.colliderect(hib):
            self.vx = 0
        elif self.obj.colliderect(hmb):
            self.bounceRelative( hmb.centery, hoop)


# Kaydıraçlar:


class Slider:

    def __init__(self, name, startingValue, xmin, xmax, ymin, ymax):
        self.value = startingValue
        self.name = name
        self.xbound = (xmin, xmax)
        self.ybound = (ymin, ymax)
        self.width = xmax - xmin
        self.height = ymax - ymin

    def update(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        
        if self.xbound[0] < mouseX < self.xbound[1] and self.ybound[0] + self.height / 2 - 5 < mouseY < self.ybound[1]:
            self.value = mouseX

    def draw(self, suffix="", getValFunc=None):
        
      
    # Çerçeve
    
    
        pygame.draw.rect(SCREEN, (125, 125, 125)
                         (self.xbound[0], self.ybound[0], self.width, self.height))
        
        pygame.draw.circle(SCREEN, (125, 125, 125),
                           (self.xbound[0], self.ybound[0]  ), self.height / 2)
        pygame.draw.circle(SCREEN, (125, 125, 125),
                           (self.x, self.ybound[0] + self.height / 2), self.height / 2)
        
        
        
        
        # Yuvarlak
        pygame.draw.circle(SCREEN, (125, 0, 0), (
            self.xbound[0] + self.value - 5, self.ybound[0] + self.height / 2), 10)
        
        
        
       
        # Yazı
        df = pygame.font.get_default_font()
        font = pygame.font.SysFont(df, 20)
        if getValFunc != None:
            text = font.render(
                f"{self.name}: {getValFunc(self.value)}{suffix}", True, (0, 0, 0))
        else:
            text = font.render(
                f"{self.name}: {self.value}{suffix}", True, (0, 0, 0))
        SCREEN.blit(text, (self.xbound[1] + 10,
                    (self.ybound[1]+self.ybound[0])/2 - text.get_height() / 2))

    def getValue(self, func=None):
        if func != None:
            return func(self.value)
        return self.value
    
    
    
    
    
# Oyun:



class Game:
    def __init__(self, Debug=False):
        self.isRunning = True
        self.clock = pygame.time.Clock()
        self.deltaTime = 0
        self.ball = Ball()
        
        self.hoop = Hoop(Debug=Debug)
        
        self.hoopSlider = Slider("Pota", 150, 15, 215, 14, 26)
        self.speedSlider = Slider("Hız", 115, 15, 215, 50, 62)
        
        self.LastTrajectory = None
        self.LastClickPos = None

        
    def tickClock(self):
        return self.clock.tick(FPS)
    
    
def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not isMouseOverUI():
                    self.LastTrajectory = mouseDownShootBall(self.ball)
                    self.LastClickPos = pygame.mouse.get_pos()
                    
                    
                    
                    
 def playSpeedConversion(self, x):
        return (x-15)/10   
    
    
    
def hoopHeightConversion(self, x):
        minHoop = self.hoopSlider.xbound[0]
        maxHoop = self.hoopSlider.xbound[1]
        return HEIGHT - 100 - ((x - minHoop) / (maxHoop - minHoop) * (HEIGHT - 100))
                    
                    
                    
