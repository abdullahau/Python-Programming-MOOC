import pygame
import random
# Complete your game here
 
# my game is a game where a robot collects falling coins and avoids falling monsters. 
# The game keeps track of the amount of coins the robot has collected.
# if the robot touches a monster, the monster steals a coin from the robot 
# - so in case of theft, the coin count goes down by one coin.
 
# One feature I could've implemented is the new game feature
 
 
# initialize game
 
pygame.init()
 
width = 640
height = 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rich The Robot")
pink_background = (255,192,203)
 
coin_img = pygame.image.load('coin.png')
monster_img = pygame.image.load('monster.png')
robot_img = pygame.image.load('robot.png')
 
clock = pygame.time.Clock()
 
#-----------------------------------------------
# class RobotRich which handles the robot 
 
class RobotRich():
    def __init__(self):
        self.image = robot_img
        self.x = width / 2
        self.y = height - robot_img.get_height()
        self.speed = 1
        self.to_left = False
        self.to_right = False
 
    # def move() moves the robot, also checks events
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.to_left = True
                if event.key == pygame.K_RIGHT:
                    self.to_right = True
                if event.key == pygame.K_ESCAPE:
                    exit()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.to_right = False
            
            if event.type == pygame.QUIT:
                exit()
 
    
        if self.x < 640 - self.speed - self.image.get_width() and self.to_right:
            self.x += self.speed
        if self.x > self.speed and self.to_left:
            self.x -= self.speed
 
#-----------------------------------------------------------------
# class coin, which handles the coin objects
 
class Coin():
    def __init__(self):
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.x = random.randint(0, width - self.rect.width)
        self.y = random.randint(-80, -30)
        self.speed = random.randint(1,3)
    
    def respawn(self):
        self.x = random.randint(0, width - self.rect.width)
        self.y = random.randint(-80, -30)
        self.speed = random.randint(1, 4)
    
    def move(self):
        self.y += self.speed
        if self.y > height:
            self.respawn()
 
    def check_collisions(self, robot: RobotRich, coin_counter):
        if (robot.x < self.x < robot.x + robot_img.get_width() or robot.x < self.x + self.rect.width < robot.x + robot_img.get_width()) and \
            (robot.y < self.y < robot.y + robot_img.get_height() or robot.y < self.y + self.rect.height < robot.y + robot_img.get_height()):
            coin_counter += 1
            self.respawn()
        return self, coin_counter
        
 
#---------------------------------------------------------
# class Monster which handles the monster objects
 
class Monster():
    def __init__(self):
        self.image = monster_img
        self.rect = self.image.get_rect()
        self.x = random.randint(0, width - self.rect.width)
        self.y = random.randint(-80, -30)
        self.speed = random.randint(1, 3)
 
    def respawn(self):
        self.x = random.randint(0, width - self.rect.width)
        self.y = random.randint(-80, -30)
        self.speed = random.randint(1, 4)
    
    def move(self):
        self.y += self.speed
        if self.y > height:
            self.respawn()
 
    def check_collisions(self, robot: RobotRich, coin_counter):
        if (robot.x < self.x < robot.x + robot_img.get_width() or robot.x < self.x + self.rect.width < robot.x + robot_img.get_width()) and \
            (robot.y < self.y < robot.y + robot_img.get_height() or robot.y < self.y + self.rect.height < robot.y + robot_img.get_height()):
            if coin_counter > 0:
                coin_counter -= 1
            self.respawn()
        return self, coin_counter
    
#----------------------------------------------------------------
# running the game
 
# creating the attributes of the game
def new_game():
 
    coin_counter = 0
    all_objects = []
    monsters = []
    font = pygame.font.SysFont('chalkduster', 20)
 
    rich_the_robot = RobotRich()
 
    coins = [Coin(), Coin(), Coin(), Coin()]
    monsters = [Monster(), Monster(), Monster()]
 
    for c in coins:
        all_objects.append(c)
 
    for m in monsters:
        all_objects.append(m)
 
    victory_coins = []
    i = 0
    while i < 150:
        victory_coins.append(Coin())
        i += 1
    
    return coin_counter, all_objects, coins, monsters, font, rich_the_robot, victory_coins
 
 
# the main loop
 
def main():
 
    coin_counter, all_objects, coins, monsters, font, rich_the_robot, victory_coins = new_game()
 
    while True:
        
        # the game itself
        if coin_counter < 10:
            for i in all_objects:
                i.move()
                rich_the_robot.move()
                i, coin_counter = i.check_collisions(rich_the_robot, coin_counter)
                window.fill(pink_background)
            for i in all_objects:
                window.blit(i.image, (i.x, i.y))
            window.blit(rich_the_robot.image, (rich_the_robot.x, rich_the_robot.y))
            game_text = font.render("Get Rich rich by collecting 10 coins!", True, (255,20,147))
            counter_text = font.render("Coins collected: " + str(coin_counter), True, (255,20,147))
            thief_text = font.render("Beware of the thief monsters...", True, (255,20,147))
            window.blit(game_text, (25, 10))
            window.blit(counter_text, (25, 40))
            window.blit(thief_text, (25, 70))
        
        # after winning
        if coin_counter >= 10:
            window.fill(pink_background)
            for c in victory_coins:
                c.move()
                window.blit(c.image, (c.x, c.y))
            rich_the_robot.move()
            window.blit(rich_the_robot.image, (rich_the_robot.x, rich_the_robot.y))
            winning_text = font.render("YAY, YOU GOT RICH!!", True, (255,20,147))
            window.blit(winning_text, (width / 3, height / 2))
                
 
        pygame.display.flip()
        clock.tick(60)
        
main()