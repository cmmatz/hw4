#Catch the apples 
#Based on Whack-a-mole game using pygame by Kimberly Todd

from pygame import *
from pygame.sprite import *
from random import *
import os

DELAY = 1000;            #Seed a timer to move sprite

bgcolor = (255,255,255) 
#Color taken from background of sprite

class Snake(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load("snake.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = (300, 400)
        self.dx = self.dy = 0

    def move(self, direction):
        currentX = self.rect.centerx
        currentY = self.rect.centery

        newx = currentX
        newy = currentY
        if direction == "right":
            newx += 10
            self.dx = 10
        if direction == "left":
            newx -= 10
            self.dx = -10
        if direction == "up":
            newy -= 10
            self.dy = -10
        if direction == "down":
            newy += 10
            self.dy = 10

        self.rect.center = (newx,newy)
    def update(self):
        x, y = self.rect.center
        self.rect.center = x + self.dx, y + self.dy

class Apple(Sprite):
    def __init__(self, x_pos):
        #print("dd")
        Sprite.__init__(self)
        self.image = image.load("apple.gif").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, 0)

        self.velocity = randint(1, 3)

    def update(self):
        #print("ddd")
        x, y = self.rect.center

        if y > 480:
            x, y = randint(0, 640), 0
            self.velocity = randint(2, 4)
        else:
            x, y = x, y + self.velocity

        self.rect.center = x, y


    # Did snake hit the target (apple)?
    def hit(self, target):
        return self.rect.colliderect(target)

    #The apples will move randomly as the snake eats it 
    def move(self):
        # y_vel = 1
        # self.y += y_vel
        # if self.y > Y_MAX:
        #     self.kill
        randX = randint(0, 640)
        randY = randint(0, 480)
        self.rect.center = (randX,randY)


#main
init()

screen = display.set_mode((640, 480))
bg = pygame.image.load("tree.bmp")
bgRect = bg.get_rect()

display.set_caption('Eat-apples')

# hide the mouse cursor so we only see shovel
# mouse.set_visible(False)

f = font.Font(None, 25)

# create the snake and apple using the constructors
x_pos = randint(0, 640)
snake = Snake()
apple = Apple(x_pos)
apple.move()
# creates a group of sprites so all can be updated at once
sprites = RenderPlain(snake, apple)
sprites.update()

hits = 0
time.set_timer(USEREVENT + 1, DELAY)

# loop until user quits
while True:
    screen.blit(bg, bgRect)
    apple.update()
    e = event.poll()
    if e.type == QUIT:
        quit()
        break
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_LEFT:
            snake.move("left")
        if e.key == pygame.K_RIGHT:
            snake.move("right")
        if e.key == pygame.K_UP:
            snake.move("up")
        if e.key == pygame.K_DOWN:
            snake.move("down")
    if e.type == pygame.KEYUP:
        if e.key == pygame.K_LEFT:
            snake.move("left")
        if e.key == pygame.K_RIGHT:
            snake.move("right")
        if e.key == pygame.K_UP:
            snake.move("up")
        if e.key == pygame.K_DOWN:
            snake.move("down")
    
    #Boarder dimmensions
    #When you lift your hand from the key, the snake should stop moving
    

    # elif e.type == MOUSEBUTTONDOWN:
        if apple.hit(snake):
            mixer.Sound("appleCrunch.wav").play()
            apple.move()
            hits += 1
                
                # display.update()
            # reset timer
            
    # elif e.type == USEREVENT + 1: # TIME has passed
        # gold.move()

    # refill background color so that we can paint sprites in new locations
    #screen.fill(bgcolor)
    t = f.render("Apples count = " + str(hits), False, (0,0,0))
    screen.blit(t, (320, 0))        # draw text to screen.  Can you move it?
    if hits == 15:
        screen.fill((0, 0, 0))
        t = f.render("You Won!!!!", False, (255,255,255))
        screen.blit(t, (310, 240))
    else:
        sprites.draw(screen)
    # update and redraw sprites
    sprites.update()
    # sprites.draw(screen)
    display.update()
