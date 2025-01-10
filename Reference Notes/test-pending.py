import pygame

pygame.init()
width, height = 640, 480

window = pygame.display.set_mode((width, height))

robot = pygame.image.load("Images\\Pygame\\robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

class Player:
    def __init__(self, keys: list, pos: tuple):
        self.player = pygame.image.load("Images\\Pygame\\robot.png")
        self.keys = keys
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.left_right_up_down = [False, False, False, False]
    
    def move(self, event_type, event_key) -> tuple:
        if event_type == pygame.KEYDOWN and event_key in self.keys:
            self.left_right_up_down[self.keys.index(event_key)] = True
            
            if self.left_right_up_down[0]:
                self.pos_x -= 2
            if self.left_right_up_down[1]:
                self.pos_x += 2
            if self.left_right_up_down[2]:
                self.pos_y -= 2
            if self.left_right_up_down[3]:
                self.pos_y += 2

            self.pos_x = max(self.pos_x, 0)
            self.pos_x = min(self.pos_x, width - robot_width)
            self.pos_y = max(self.pos_y, 0)
            self.pos_y = min(self.pos_y, height - robot_height)
        
        if event_type == pygame.KEYUP and event_key in self.keys:
            self.left_right_up_down[self.keys.index(event_key)] = False
                
player1_keys = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
player2_keys = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]

player1 = Player(player1_keys, (0 , 0))
player2 = Player(player2_keys, (width - robot_width, height - robot_height))

#clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key in player1_keys:
                player1.move(event.type, event.key)
            if event.key in player2_keys:
                player2.move(event.type, event.key)
         
    window.fill((0, 0, 0))
    
    window.blit(player1.player, (player1.pos_x, player1.pos_y))
    window.blit(player2.player, (player2.pos_x, player2.pos_y))
    
    pygame.display.flip()
    #clock.tick(60)