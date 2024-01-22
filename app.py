import pygame
import time
import random

pygame.init()

# Colors
snake_color = (255, 255, 255)
text_color = (255, 255, 255)
food_color = (255, 0, 0)
background = (0, 0, 0)

# Window settings
window_width = 600
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Snake settings
snake_block = 10
snake_speed = 8

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def draw_snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(window, snake_color, [segment[0], segment[1], snake_block, snake_block])

def display_message(msg, color, y_displacement=0):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [window_width / 6, window_height / 3 + y_displacement])

def game_loop():
    game_over = False
    game_close = False

    x1, y1 = window_width / 2, window_height / 2
    x1_change, y1_change = 0, 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            window.fill(background)
            display_message("You Lost! Press C-Play Again or Q-Quit", text_color, y_displacement=50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not x1_change:
                    x1_change, y1_change = -snake_block, 0
                elif event.key == pygame.K_RIGHT and not x1_change:
                    x1_change, y1_change = snake_block, 0
                elif event.key == pygame.K_UP and not y1_change:
                    y1_change, x1_change = -snake_block, 0
                elif event.key == pygame.K_DOWN and not y1_change:
                    y1_change, x1_change = snake_block, 0

        x1 += x1_change
        y1 += y1_change

        if x1 < 0 or x1 >= window_width or y1 < 0 or y1 >= window_height:
            game_close = True

        window.fill(background)
        pygame.draw.rect(window, food_color, [foodx, foody, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
