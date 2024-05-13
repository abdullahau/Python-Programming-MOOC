
# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window_x = 640
window_y = 480
window = pygame.display.set_mode((window_x, window_y))

robot = pygame.image.load('robot.png')

window.fill((0, 0, 0))

width = robot.get_width()
height = robot.get_height()

window.blit(robot, (0, 0))
window.blit(robot, (window_x - width, 0))
window.blit(robot, (0, window_y - height))
window.blit(robot, (window_x - width, window_y - height))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()