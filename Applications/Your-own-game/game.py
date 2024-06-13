import pygame
import random
from collections import deque

# ----- Constants ------
# Screen Size
tile_width = 25
tile_height = 25
rows = 30
columns = 40
width = tile_width * columns
height = tile_height * rows

# Color
white = (255, 255, 255)
teal = (0, 139, 139)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)

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

# ----- Map/Maze Class ------
class Map:
    def __init__(self, maze):
        self.path_nodes = {}
        for row, line in enumerate(maze):
            for col, char in enumerate(line):
                if char == " ":
                    x, y = col * (tile_width + 11), row * (tile_height + 11)
                    self.path_nodes[(x, y)] = True
    
    def paths(self):
        # return valid path dict
        return self.path_nodes
    
    def path_render(self, screen):
        # Renders maze walls & path
        for row, line in enumerate(maze):
            for col, char in enumerate(line):
                x, y = col * (tile_width + 11), row * (tile_height + 11)
                if char == " ":
                    pygame.draw.rect(screen, white, (x, y, tile_width + 11, tile_height + 11))
                else:
                    pygame.draw.rect(screen, teal, (x, y, tile_width + 11, tile_height + 11))        

# ----- Node Class ------
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# ----- Robot Class ------
class Robot:
    def __init__(self, path, screen):
        self.path = list(path.keys())
        self.robot_x, self.robot_y = self.path[0] # Starting position is the starting tile of the maze
        self.target_x, self.target_y = self.robot_x, self.robot_y
        self.direction = None   
        self.screen = screen  
        self.immunity = 10 
        self.score = 0 
        self.coins_collected = 0
        self.immunity_activated = False
        self.goals_visited = 0
        
    def render(self, screen):
        crop = pygame.Surface((tile_width+11, tile_height+10))
        crop.fill(white)
        robot = pygame.image.load('robot.png').convert_alpha()
        if self.immunity_activated:
            robot.fill((0, 0, 255, 128), special_flags=pygame.BLEND_RGBA_MULT)
        crop.blit(robot, (-7,0))
        screen.blit(crop, (self.robot_x, self.robot_y)) 
    
    def robot_move(self):
        if self.direction:
            dx, dy = self.direction
            if self.robot_x == self.target_x and self.robot_y == self.target_y:
                # Calculate new target position
                new_x, new_y = self.robot_x + dx, self.robot_y + dy
                
                if (new_x, new_y) in self.path:
                    self.target_x, self.target_y = new_x, new_y

        if self.robot_x < self.target_x:
            self.robot_x += 2
        elif self.robot_x > self.target_x:
            self.robot_x -= 2
        
        if self.robot_y < self.target_y:
            self.robot_y += 2
        elif self.robot_y > self.target_y:
            self.robot_y -= 2
    
    def collect_coin(self, coin):
        if abs(self.robot_x - coin.x) < tile_width and abs(self.robot_y - coin.y) < tile_height:
            return True
        return False
    
    def activate_immunity(self):
        if self.immunity > 0:
            self.immunity_activated = True
            self.immunity -= 0.05
        else:
            self.immunity_activated = False
            
    def deactivate_immunity(self):
        self.immunity_activated = False
        
    def add_immunity(self, amount):
        self.immunity += amount
        
    def add_score(self, points):
        self.score += points
    
    def get_stats(self):
        return self.immunity, self.score, self.coins_collected, self.goals_visited

# ----- Monster Class ------
class Monster:
    def __init__(self, path, screen, start_pos):
        self.path = path
        self.monster_x, self.monster_y = start_pos
        self.screen = screen
        self.target_x, self.target_y = self.monster_x, self.monster_y
        self.respawn_pos = start_pos
        self.running_away = False
        self.alive = True  # Track if the monster is alive
        
    def bfs(self, start, goal):
        queue = deque([start])
        came_from = {start: None}
        
        while queue:
            current = queue.popleft()
            if current == goal:
                break
                
            neighbors = [(current[0] + dx, current[1] + dy) for dx, dy in [(-tile_width-11, 0), (tile_width+11, 0), (0, -tile_height-11), (0, tile_height+11)]]
            for neighbor in neighbors:
                if neighbor in self.path and neighbor not in came_from:
                    queue.append(neighbor)
                    came_from[neighbor] = current
                    
        if goal not in came_from:
            return []
        
        path = []
        current = goal
        while current:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path
    
    def move_towards(self, target_pos):
        path = self.bfs((self.monster_x, self.monster_y), target_pos)
        if len(path) > 1:
            self.target_x, self.target_y = path[1]
        
        if self.monster_x < self.target_x:
            self.monster_x += 1
        elif self.monster_x > self.target_x:
            self.monster_x -= 1
        
        if self.monster_y < self.target_y:
            self.monster_y += 1
        elif self.monster_y > self.target_y:
            self.monster_y -= 1
            
    def run_away(self, target_pos):
        all_possible_nodes = list(self.path.keys())
        farthest_distance = 0
        best_position = (self.monster_x, self.monster_y)
        
        for node in all_possible_nodes:
            distance = abs(node[0] - target_pos[0]) + abs(node[1] - target_pos[1])
            if distance > farthest_distance:
                farthest_distance = distance
                best_position = node
        
        self.move_towards(best_position)
    
    def render(self):
        if self.alive:
            monster = pygame.image.load('monster.png').convert_alpha()
            monster = pygame.transform.scale_by(monster, 0.5)
            self.screen.blit(monster, (self.monster_x, self.monster_y)) 
        
    def respawn(self):
        self.monster_x, self.monster_y = self.respawn_pos
        self.alive = True

# ----- Coin Class ------
class Coin:
    def __init__(self, position):
        self.x, self.y = position
    
    def render(self, screen):
        coin = pygame.image.load('coin.png').convert_alpha()
        coin = pygame.transform.scale(coin, (tile_width + 11, tile_height + 11))
        screen.blit(coin, (self.x, self.y))

# ----- Goal Class ------
class Goal:
    def __init__(self, position):
        self.x, self.y = position
        self.active = True
    
    def render(self, screen):
        color = blue if self.active else green
        pygame.draw.rect(screen, color, (self.x, self.y, tile_width + 11, tile_height + 11))

# ----- Main Game Class ------
class RobotRescueMission:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Robot Rescue Mission")
        self.maze = Map(maze)
        self.path = self.maze.paths()
        
        # Robot Initialization
        self.robot = Robot(self.path, self.screen)
        
        # Monster Initialization
        self.monsters = [
            Monster(self.path, self.screen, (684, 684)),  # Bottom-left corner
            Monster(self.path, self.screen, (36, 684)), # Bottom-right corner
            Monster(self.path, self.screen, (684, 36))  # Top-left corner
        ]
        
        # Coin Initialization
        self.coins = []
        for _ in range(5):
            coin_pos = random.choice(list(self.path.keys()))
            self.coins.append(Coin(coin_pos))
        
        # Goal Initialization
        self.goals = [Goal((684, 684)), Goal((36, 684)), Goal((684, 36))]
        
        self.main_loop()
    
    def main_loop(self):
        while True:
            self.check_events()
            self.robot.robot_move()
            for monster in self.monsters:
                if self.robot.immunity_activated and monster.alive:
                    monster.run_away((self.robot.robot_x, self.robot.robot_y))
                elif monster.alive:
                    monster.move_towards((self.robot.robot_x, self.robot.robot_y))
                if self.check_collision(monster):
                    if self.robot.immunity_activated and monster.alive:
                        self.robot.add_score(50)
                        monster.alive = False  # Mark the monster as dead
                    elif monster.alive:
                        print("Game Over!")
                        pygame.quit()
                        exit()
            
            for coin in self.coins:
                if self.robot.collect_coin(coin):
                    self.robot.add_immunity(10)
                    self.robot.add_score(10)
                    self.robot.coins_collected += 1
                    self.coins.remove(coin)
            
            for goal in self.goals:
                if goal.active and self.check_goal_reached(goal):
                    goal.active = False
                    self.robot.add_score(100)
                    self.robot.goals_visited += 1
                    for monster in self.monsters:
                        if not monster.alive:
                            pygame.time.set_timer(pygame.USEREVENT, 5000, True)  # Set a timer for 5 seconds

            if self.robot.goals_visited == len(self.goals):
                print("You Win!")
                pygame.quit()
                exit()
            
            self.render()
            self.clock.tick(60)

    def check_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.robot.direction = (-tile_width - 11, 0)
        elif keys[pygame.K_RIGHT]:
            self.robot.direction = (tile_width + 11, 0)
        elif keys[pygame.K_UP]:
            self.robot.direction = (0, -tile_height - 11)
        elif keys[pygame.K_DOWN]:
            self.robot.direction = (0, tile_height + 11)
        else:
            self.robot.direction = None
        
        if keys[pygame.K_SPACE]:
            self.robot.activate_immunity()
        else:
            self.robot.deactivate_immunity()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.USEREVENT:
                for monster in self.monsters:
                    if not monster.alive:
                        monster.respawn()

    def check_collision(self, monster):
        return abs(self.robot.robot_x - monster.monster_x) < tile_width and abs(self.robot.robot_y - monster.monster_y) < tile_height
    
    def check_goal_reached(self, goal):
        return abs(self.robot.robot_x - goal.x) < tile_width and abs(self.robot.robot_y - goal.y) < tile_height
    
    def render(self):
        self.screen.fill(white)
        self.maze.path_render(self.screen)
        self.robot.render(self.screen)
        for monster in self.monsters:
            monster.render()
        for coin in self.coins:
            coin.render(self.screen)
        for goal in self.goals:
            goal.render(self.screen)
        
        self.render_stats()
        pygame.display.flip()
    
    def render_stats(self):
        font = pygame.font.SysFont('consolas', 25)
        immunity, score, coins_collected, goals_visited = self.robot.get_stats()
        
        immunity_text = font.render(f"Total Immunity", True, teal)
        immunity_display = font.render(f"{int(immunity)}s", True, red)
        
        self.screen.blit(immunity_text, (width-immunity_text.get_width()-10, 10))
        self.screen.blit(immunity_display, (width-immunity_display.get_width()-10, 50))
        
        
        score_text = font.render(f"Total Score", True, teal)
        score_display = font.render(f"{score}", True, red) 
        self.screen.blit(score_text, (width-score_text.get_width()-10, 110))
        self.screen.blit(score_display, (width-score_display.get_width()-10, 150))
        
        
        coins_text = font.render(f"Coins Collected", True, teal)
        coins_display = font.render(f"{coins_collected}", True, red)
        self.screen.blit(coins_text, (width-coins_text.get_width()-10, 210))
        self.screen.blit(coins_display, (width-coins_display.get_width()-10, 250))
         
        goals_text = font.render(f"Goals Visited", True, teal)
        goals_display = font.render(f"{goals_visited}/{len(self.goals)}", True, red)
        self.screen.blit(goals_text, (width-goals_text.get_width()-10, 310))
        self.screen.blit(goals_display, (width-goals_display.get_width()-10, 350))
        
        instruction_font = pygame.font.SysFont('arial', 25)
        fontItalic = instruction_font
        fontItalic.set_italic(True)
        instruction = fontItalic.render("Instructions", True, black)
        instructions_text1 = fontItalic.render("Move: ← ↑ → ↓", True, black)
        instructions_text2 = fontItalic.render("Immunity: Spacebar", True, black)
        self.screen.blit(instruction, (width-instruction.get_width()-10, 600))
        self.screen.blit(instructions_text1, (width-instructions_text1.get_width()-10, 630))
        self.screen.blit(instructions_text2, (width-instructions_text2.get_width()-10, 660))

if __name__ == "__main__":  
    RobotRescueMission()