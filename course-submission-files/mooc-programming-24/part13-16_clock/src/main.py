# WRITE YOUR SOLUTION HERE:
import pygame
from datetime import datetime
from math import pi, sin, cos

width, height = 640, 480
display = pygame.display.set_mode((width, height))

mid_x = width/2
mid_y = height/2

# Computes the total division of the full 2π radian rotation for the hour hand into 43200 seconds - 2π/43,200
radians_per_hoursec = (2 * pi) / (12 * 60 * 60)
# Computes the total division of the full 2π radian rotation for the minute hand into 3600 seconds - 2π/3,600
radians_per_minsec = (2 * pi) / (60 * 60)
# Computes the total division of the full 2π radian rotation for the second hand into 60 seconds - 2π/60
raidans_per_sec = (2 * pi)/ 60

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    now = datetime.now()
    hour = int(f"{now: %H}")
    min = int(f"{now: %M}")
    sec = int(f"{now: %S}")
    # Because the y-axis is reversed from typical (increases going top to bottom) and 0 radian starts from the 3 o'clock position, the radians need to move back (anti-clockwise) entirely by π/2 or 90 degrees.
    hour_rad = (((hour * 60 * 60) + (min * 60) + sec) * radians_per_hoursec) - pi/2
    min_rad = (((min * 60) + sec) * radians_per_minsec) - pi/2
    sec_rad = (sec * raidans_per_sec) - pi/2
    

    pygame.display.set_caption(f"{now:%H:%M:%S}")
    
    display.fill((0, 0, 0))
    
    # Center Point
    pygame.draw.circle(display, (255, 0, 0), (mid_x, mid_y), 10)
    # Clock Circle
    pygame.draw.circle(display, (255, 0, 0), (mid_x, mid_y), 200, width=5)
    
    # Hour Hand
    pygame.draw.line(display, (0, 0, 255), (mid_x, mid_y), (mid_x+cos(hour_rad)*140, mid_y+sin(hour_rad)*140), width=4)
    
    # Minute Hand
    pygame.draw.line(display, (0, 0, 255), (mid_x, mid_y), (mid_x+cos(min_rad)*180, mid_y+sin(min_rad)*180), width=2)
    
    # Second Hand
    pygame.draw.line(display, (0, 0, 255), (mid_x, mid_y), (mid_x+cos(sec_rad)*180, mid_y+sin(sec_rad)*180), width=1)
    
    pygame.display.flip()
 
    clock.tick(60)    