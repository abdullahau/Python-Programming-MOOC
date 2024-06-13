import pygame
from random import randint
 
class Coinport:
 
    def __init__(self):
        pygame.init()
 
        self.load_images()
        self.width = 640
        self.height = 480
        self.window = pygame.display.set_mode((self.width, self.height))
 
        self.game_font = pygame.font.SysFont("Arial", 24)
 
        pygame.display.set_caption("Coinport")
        
        
        self.door()
 
        self.clock = pygame.time.Clock()
 
        self.to_left = False
        self.to_right = False
        self.x = 0
        self.y = self.height - self.images["robot"].get_height()
 
        self.points = 0
 
        self.start = True
        self.end = False
 
        self.number = 10
 
        self.main_loop()
 
        
 
    def load_images(self):
        self.images = {}
        for name in ["coin", "door", "monster", "robot"]:
            self.images[name] = pygame.image.load(name +".png")
 
    def coin_monster_pos(self, number):
        self.position_coin = []
        self.position_monster = []
 
        self.number = number
 
        for i in range(self.number):
            self.position_coin.append([randint(0, self.width - self.images["coin"].get_width()), -randint(100, 1000)])
            self.position_monster.append([randint(0, self.width - self.images["monster"].get_width()), -randint(100, 1000)])
 
    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()
            if self.start:
                continue
            if self.end:
                continue
            self.fall()
            self.robot_move()
        
 
 
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.to_left = True
                if event.key == pygame.K_RIGHT:
                    self.to_right = True
 
                if event.key == pygame.K_SPACE:
                    self.x = self.d_x
                    self.y = self.y_x
 
                    self.door()
                
                if event.key == pygame.K_RETURN:
                    if self.end:
                        self.end = False
                        self.coin_monster_pos(self.number)
                        self.points = 0
 
                # Giving level by changing amount of monster and coin
                if event.key == pygame.K_1:
                    self.start = False
                    self.number = 10
                    self.coin_monster_pos(10)
 
                if event.key == pygame.K_2:
                    self.start = False
                    self.number = 20
                    self.coin_monster_pos(20)
 
                if event.key == pygame.K_3:
                    self.start = False
                    self.number = 30
                    self.coin_monster_pos(30)
 
                if event.key == pygame.K_ESCAPE:
                    exit()
                
 
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.to_right = False
 
            if event.type == pygame.QUIT:
                exit()
    
    def fall(self):
        for i in range(self.number):
            
            if self.position_coin[i][1] >= self.height:
                self.position_coin[i][0] = randint(0, self.width - self.images["coin"].get_width())
                self.position_coin[i][1] = -randint(100, 3000)
 
            if self.position_monster[i][1] >= self.height:
                self.position_monster[i][0] = randint(0, self.width - self.images["monster"].get_width())
                self.position_monster[i][1] = -randint(100, 3000)
 
            # Checking points i.e, robot contacts with coin
            
            if self.position_coin[i][1] + self.images["coin"].get_height() in range(self.y, self.y+self.images["robot"].get_height()):
                if self.position_coin[i][0] in range(self.x , self.x + self.images["robot"].get_width()) or (self.position_coin[i][0] + self.images["coin"].get_width()) in range(self.x , self.x + self.images["robot"].get_width()):
                    self.position_coin[i][0] = randint(0, self.width - self.images["coin"].get_width())
                    self.position_coin[i][1] = -randint(100, 3000)
 
                    self.points += 1
 
            # checking if robot touches monster
 
            if (self.position_monster[i][1] + self.images["monster"].get_height()) in range(self.y, self.y+self.images["robot"].get_height()):
                if self.position_monster[i][0] in range(self.x , self.x + self.images["robot"].get_width()) or (self.position_monster[i][0] + self.images["monster"].get_width()) in range(self.x , self.x + self.images["robot"].get_width()):
                    self.position_monster[i][0] = randint(0, self.width - self.images["monster"].get_width())
                    self.position_monster[i][1] = -randint(100, 3000)
 
                    self.end = True
 
            self.position_coin[i][1] += 3
            self.position_monster[i][1] += 3
 
 
 
    def robot_move(self):
        
        if self.to_left and self.x > 0:
            self.x -= 4
        if self.to_right and self.width - self.images["robot"].get_width() > self.x:
            self.x += 4
 
    def door(self):
        self.d_x = randint(0, self.width - self.images["robot"].get_width())
        self.y_x = self.height - self.images["robot"].get_height()
 
 
    def  draw_window(self):
        self.window.fill((235, 227, 213))
 
        if self.start:
            x_start = self.width/2
 
            s_font = pygame.font.SysFont("Arial bold", 24)
            start_text = s_font.render("Use LEFT, RIGHT arrow keys to move and SPACE for telport to door", True, (117, 106, 182))
            choose_level = s_font.render("choose Level: Press(1 for easy, 2 for normal, 3 for hard)", True, (85, 173, 155))
            pygame.draw.rect(self.window, "white", (50, 200, 540, 100))
            self.window.blit(start_text, (x_start - start_text.get_width()/2,220))
            self.window.blit(choose_level, (x_start - choose_level.get_width()/2,260))
 
 
        elif self.end:
            end_font = pygame.font.SysFont("Arial", 25)
            end_text = end_font.render(f"Game Over! Collected Coins: {self.points}", True, "Red")
            end_info = end_font.render(f"Press: Return for restart and Escape for exit", True, "black")
            pygame.draw.rect(self.window, "white", (50, 200, 540, 100))
            self.window.blit(end_text, (self.width/2-end_text.get_width()/2,220))
            self.window.blit(end_info, (self.width/2-end_info.get_width()/2,260))
 
        else:
            game_text = self.game_font.render(f"Coins: {self.points}", True, "red")
            self.window.blit(game_text, (510, 0))
 
            for i in range(self.number):
                self.window.blit(self.images["coin"], (self.position_coin[i][0], self.position_coin[i][1]))
                self.window.blit(self.images["monster"], (self.position_monster[i][0], self.position_monster[i][1]))
 
            
                
            self.window.blit(self.images["robot"], (self.x, self.y))
            self.window.blit(self.images["door"], (self.d_x, self.y_x))
 
        pygame.display.flip()
        self.clock.tick(60)
 
if __name__ == "__main__":
    Coinport()