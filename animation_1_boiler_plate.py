# imports for pygame
import pygame, sys
from pygame.locals import *
import random

# canvas variables
width = 900 # adjust for width of canvas
height = 900 # adjust for height of canvas

# frame rate
fps = 60

# colors
background_color = (0, 0, 0)

# initializing pygame, setting up the surface (canvas)
pygame.init()
canvas = pygame.display.set_mode((width, height))
pygame.display.set_caption("It's gonna get glitchy") # add a caption for your canvas

# import assets
sprite_sheet = pygame.image.load("The Glitch.png").convert_alpha() # add the path/name of your sprite sheet file
background_scene = pygame.image.load("sunset animation.png").convert_alpha()
total_background_images = 5

# get details about individual sprites
total_sprites = 35 # code the number of sprite images your sprite sheet has
sprite_sheet_width = sprite_sheet.get_rect().width
sprite_sheet_height = sprite_sheet.get_rect().height
sprite_sheet_background_width = background_scene.get_rect().width
sprite_sheet_background_height = background_scene.get_rect().height

# adjust sprite size
sprite_scale_factor = 5
sprite_sheet_width = sprite_sheet_width * sprite_scale_factor
sprite_sheet_height = sprite_sheet_height * sprite_scale_factor
sprite_sheet = pygame.transform.scale(sprite_sheet, (sprite_sheet_width, sprite_sheet_height))
sprite_sheet_width = sprite_sheet.get_rect().width
sprite_sheet_height = sprite_sheet.get_rect().height
sprite_width = sprite_sheet_width // total_sprites
sprite_height = sprite_sheet_height

background_scale_factor = 3
sprite_sheet_background_width = sprite_sheet_background_width * background_scale_factor
sprite_sheet_background_height = sprite_sheet_background_height * background_scale_factor
background_scene = pygame.transform.scale(background_scene, (sprite_sheet_background_width, sprite_sheet_background_height))
sprite_sheet_background_width = background_scene.get_rect().width
sprite_sheet_background_height = background_scene.get_rect().height
background_width = sprite_sheet_background_width // 5
background_height = sprite_sheet_background_height

# define initial x and y position of sprite
sprite_x_pos = 0
sprite_y_pos = 0
sprite_x_delta = 10
sprite_y_delta = 10

# load sprite sheet into list
sprite_list = []
for i in range(total_sprites):
    rect = pygame.Rect(i * sprite_width, 0, sprite_width, sprite_height)
    image = sprite_sheet.subsurface(rect)
    sprite_list.append(image)

# load background scene sprite sheet into list
background_list = []
for i in range(total_background_images):
    rect = pygame.Rect(i * background_width, 0, background_width, background_height)
    image = background_scene.subsurface(rect)
    background_list.append(image)

# sprite picker function for animation
sprite_index = 0
counter = 0
def spritePicker():
    global sprite_index
    if counter % 5 == 0: # adjust the number to the right of the "%" symbol to increase/decrease animation speed
        if sprite_index == total_sprites - 1:
            sprite_index = 0
        else:
            sprite_index += 1

# sprite picker for background
background_index = 0
def backgroundPicker():
    global background_index
    global counter
    if counter % 20 == 0:
        if background_index == total_background_images - 1:
            background_index = 0
        else:
            background_index += 1


# clock to set FPS
clock = pygame.time.Clock()

# variable to control state of entire game
running = True

# main game loop
while running:
    # paint the canvas with background color
    # background_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    # canvas.fill(background_color)

    # poll for events
    for event in pygame.event.get():
        # if 'X' is clicked on the canvas
        if event.type == QUIT:
            running = False

    # get all keys that are currently pressed    
    keys = pygame.key.get_pressed()

    # check to see if any of the keys are w, a, s, or d
    # and perform an action
    if keys[pygame.K_w]:
        sprite_y_pos -= sprite_y_delta
    if keys[pygame.K_s]:
        sprite_y_pos += sprite_y_delta
    if keys[pygame.K_a]:
        sprite_x_pos -= sprite_x_delta
    if keys[pygame.K_d]:
        sprite_x_pos += sprite_x_delta

    canvas.blit(background_list[background_index], (0, 0))
    backgroundPicker()
    canvas.blit(sprite_list[sprite_index], (sprite_x_pos, sprite_y_pos))
    spritePicker()
    pygame.display.update()
    counter += 1
    clock.tick(fps)

# close pygame down
pygame.quit()
sys.exit()