import pygame
from random import randint

# ----- Constants ------
# Screen Size
tile_width = 25
tile_height = 25
rows = 30
columns = 40
width = tile_width * columns
height = tile_height * rows

# Color
black = (0, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
red = (255, 0, 0)
teal = (0,139,139)
blue = (0, 0, 255)



maze = ['+-+-+-+-+-+-+-+-+-+-+',
        '|   |     |         |',
        '+ +-+ +-+ + +-+ +-+ +',
        '|   |   | |   | | | |',
        '+-+ + +-+ +-+ + + + +',
        '|   | | |   | | | | |',
        '+ +-+ + +-+ + + + + +',
        '|     | |   | | |   |',
        '+ +-+-+ + +-+-+ + +-+',
        '| |   |   |     |   |',
        '+ +-+ +-+-+ +-+-+-+-+',
        '|   | |     |       |',
        '+-+ + + + + + +-+-+ +',
        '|   |   | | |     | |',
        '+ +-+-+-+ +-+-+-+ + +',
        '|       |         | |',
        '+-+-+-+ +-+-+-+-+-+ +',
        '|   |   |       |   |',
        '+ + + +-+ +-+-+ + + +',
        '| |       |       | |',
        '+-+-+-+-+-+-+-+-+-+-+']

maze2 = ['+-+-+-+-+-+-+-+-+-+-+',
         '|     |             |',
         '+ +-+-+ +-+-+ +-+-+ +',
         '| |     | |   |     |',
         '+ + +-+-+ + +-+-+-+-+',
         '| |   |   | |       |',
         '+ +-+ +-+ + + +-+-+ +',
         '|   |   | |   |     |',    
         '+ + +-+ + +-+-+ +-+-+',
         '| | | | |     |   | |',
         '+ + + + +-+-+ +-+-+ +',
         '| |   |     |       |',
         '+ +-+-+-+-+ + +-+ + +',
         '|           |   | | |',
         '+ +-+-+-+-+-+-+-+ +-+',   
         '|               |   |',
         '+-+-+-+-+-+-+-+ + + +',
         '| |     |     | | | |',
         '+ + + +-+ +-+ + +-+ +',
         '|   |       |       |',
         '+-+-+-+-+-+-+-+-+-+-+']

# ----- Game Class ------
class RobotRescueMission:
    def __init__(self):
        
        # Pygame initialization
        pygame.init()
        
        # Set Screen size
        self.screen = pygame.display.set_mode((width - tile_width*3, height))
        self.game_font = pygame.font.SysFont("Arial", 24)
        self.clock = pygame.time.Clock()
        
        pygame.display.set_caption("Robot Rescue Mission")
        
        self.load_images()
        
        self.node(maze2)
        
        self.robot_x, self.robot_y = 1 * (tile_width + 11), 1 * (tile_height + 11)
        
        self.main_loop()
    
    def load_images(self):
        self.images = {'robot': (300,300), 'coin': self.coin_spawn(), 'monster': (0, 0), 'door': (0,0)}
        for name, pos in self.images.items():
            load = pygame.image.load(name + '.png')
            self.images[name] = [pygame.transform.scale(load, (tile_width+11, tile_height+11)), pos]
        return self.images

    def coin_spawn(self):
        return (randint(0,600), randint(0,600))
    
    def maze_render(self, maze):
        # Draw maze walls
        for row, line in enumerate(maze):
            for col, char in enumerate(line):
                x, y = (col) * (tile_width + 11), (row) * (tile_height + 11)
                if char == " ":
                    pygame.draw.rect(self.screen, white, (x, y, (tile_width+11), (tile_height+11)), width=0)
                else:
                    pygame.draw.rect(self.screen, teal, ((x, y), ((tile_width+11), (tile_height+11))), width=0)
    
    def move(self, dx, dy):
        # Calculate new position
        new_x, new_y = self.robot_x + dx, self.robot_y + dy
        
        # Check if the new position is within the white space nodes
        if (new_x, new_y) in self.nodes:
            self.robot_x, self.robot_y = new_x, new_y
    
    def move_monsters(self):
        pass
    
    def robot_immunity(self):
        pass
    
    def main_loop(self):
        while True:
            self.check_events()
            self.render()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move(-tile_width-11, 0)
                if event.key == pygame.K_RIGHT:
                    self.move(tile_width+11, 0)
                if event.key == pygame.K_UP:
                    self.move(0, -tile_height-11)
                if event.key == pygame.K_DOWN:
                    self.move(0, +tile_height+11)
                if event.key == pygame.K_F2:
                    self.new_game()
                if event.key == pygame.K_ESCAPE:
                    exit()                

            if event.type == pygame.QUIT:
                exit()       
    
    def render(self):
        self.screen.fill(white)
        
        self.maze_render(maze2)
        
        # Draw Robot
        for image in self.images:
            if image == 'robot':
                self.screen.blit(self.images['robot'][0], (self.robot_x, self.robot_y))
            else:    
                self.screen.blit(self.images[image][0],self.images[image][1])

        pygame.display.flip()
        
    
    def level_completed(self):
        pass
    
if __name__ == "__main__":
    RobotRescueMission()