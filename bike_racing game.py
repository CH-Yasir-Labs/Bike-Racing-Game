#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     15/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Bike Racing Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Game variables
bike_width, bike_height = 40, 70
player_x = WIDTH // 2 - bike_width // 2
player_y = HEIGHT - 150
player_speed = 6

# AI bikes
num_ai_bikes = 3
ai_bikes = [{
    "x": random.randint(130, WIDTH - 130 - bike_width),
    "y": random.randint(-400, -100),
    "speed": random.randint(3, 6)
} for _ in range(num_ai_bikes)]

road_y = 0
road_speed = 5
score = 0
running = True
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Main game loop
while running:
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 120:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 120 - bike_width:
        player_x += player_speed

    # Move road effect
    road_y += road_speed
    if road_y > HEIGHT:
        road_y = 0

    # Draw road and lane markers
    pygame.draw.rect(screen, BLACK, (100, 0, WIDTH - 200, HEIGHT))
    for i in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, YELLOW, (WIDTH // 2 - 5, i + road_y, 10, 30))

    # Move AI bikes
    for bike in ai_bikes:
        bike["y"] += bike["speed"]
        if bike["y"] > HEIGHT:
            bike["y"] = random.randint(-400, -100)
            bike["x"] = random.randint(130, WIDTH - 130 - bike_width)
            bike["speed"] = random.randint(3, 6)
            score += 1

    # Draw AI bikes
    for bike in ai_bikes:
        pygame.draw.rect(screen, RED, (bike["x"], bike["y"], bike_width, bike_height))
        pygame.draw.circle(screen, BLACK, (bike["x"] + 10, bike["y"] + 60), 10)
        pygame.draw.circle(screen, BLACK, (bike["x"] + 30, bike["y"] + 60), 10)

    # Draw player's bike
    pygame.draw.rect(screen, BLUE, (player_x, player_y, bike_width, bike_height))
    pygame.draw.circle(screen, GREEN, (player_x + 10, player_y + 60), 10)
    pygame.draw.circle(screen, GREEN, (player_x + 30, player_y + 60), 10)

    # Display Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))

    # Collision detection
    for bike in ai_bikes:
        if player_x < bike["x"] + bike_width and player_x + bike_width > bike["x"] and \
                player_y < bike["y"] + bike_height and player_y + bike_height > bike["y"]:
            print("🚨 Crash! Game Over!")
            running = False

    # Update display
    pygame.display.update()
    clock.tick(30)

pygame.quit()
