import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Snake")
icon = pygame.image.load("images.png")
pygame.display.set_icon(icon)

black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
snakenumlistx = []
snakenumlisty = []

for i in range(100, 700):
    if i%20 == 0:
        snakenumlistx.append(i)
for i in range(100, 500):
    if i%20 == 0:
        snakenumlisty.append(i)

snake_x = random.choice(snakenumlistx)
print(snake_x)
snake_y = random.choice(snakenumlisty)
print(snake_y)
food_x = random.choice(snakenumlistx)
print(food_x)
food_y = random.choice(snakenumlisty)
print(food_y)

running = True

while running:
    pygame.time.delay(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill(green)
        pygame.draw.rect(screen,blue,[snake_x,snake_y,20,20])
        pygame.draw.rect(screen,red,[food_x,food_y,20,20])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                snake_x -= 20
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                snake_x += 20
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                snake_y += 20
            if event.key == pygame.K_UP or event.key == ord('w'):
                snake_y -= 20
    if snake_x == food_x:
        if snake_y == food_y:
            print('here')
            pygame.draw.rect(screen,green,[food_x, food_y, 20,20])

            pygame.display.update()



    if snake_x == 0 or snake_x == 800:
        print('game over')
        running = False
    if snake_y == 0 or snake_y == 600:
        print('game over')
        running = False
    pygame.display.update()
