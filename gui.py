import pygame
import os
from pathfinding_algorithms.coordinates import Coordinates
from pathfinding_algorithms.pathfinding import Pathfinding

class Gui():
    FPS = 60
    WIDTH = 800

    def __init__(self, coords):
        # Set grid size and box width
        self.grid_size = 20
        self.box_width = self.WIDTH / self.grid_size
        self.coords = coords
        self.placing_walls = False
        self.removing_walls = False
        self.ready_for_algorithm = False

        # Initialize the maze with all zeros
        self.coords.maze = [[0 for x in range(self.grid_size)] for y in range(self.grid_size)]

        pygame.init()
        # Set up the display window
        self.win = pygame.display.set_mode((self.WIDTH, self.WIDTH + 100))  # Extra space for buttons
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pathfinding Algorithms")

        # Load images for walls, robot, and end points
        image_folder = os.path.join(os.path.dirname(__file__), 'images')

        self.wall_img = pygame.image.load(os.path.join(image_folder, 'wall.png')).convert_alpha()
        self.wall_img = pygame.transform.scale(self.wall_img, (int(self.box_width), int(self.box_width)))

        self.robot_img = pygame.image.load(os.path.join(image_folder, 'robot.png')).convert_alpha()
        self.robot_img = pygame.transform.scale(self.robot_img, (int(self.box_width), int(self.box_width)))

        self.end_img = pygame.image.load(os.path.join(image_folder, 'end.png')).convert_alpha()
        self.end_img = pygame.transform.scale(self.end_img, (int(self.box_width), int(self.box_width)))

        # Define button areas for different actions
        self.buttons = {
            "DFS": pygame.Rect(10, 810, 100, 40),
            "BFS": pygame.Rect(120, 810, 100, 40),
            "Dijkstra": pygame.Rect(230, 810, 100, 40),
            "A*": pygame.Rect(340, 810, 100, 40),
            "Clear": pygame.Rect(450, 810, 100, 40),
            "Random Maze": pygame.Rect(560, 810, 120, 40),
        }

    def main(self, running=False):
        self.clock.tick(self.FPS)
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        # Handle wall placement and removal if not running an algorithm
        if not running:
            if self.placing_walls:
                self.place_wall()
            elif self.removing_walls:
                self.remove_wall()

        # Handle events and redraw the screen
        self.event_handle(running)
        self.redraw()
        pygame.display.update()

    def event_handle(self, running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mousedown(event, running)
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event)

    def handle_keydown(self, event):
        if event.key == pygame.K_RETURN:  # Press Enter to toggle algorithm mode
            self.ready_for_algorithm = not self.ready_for_algorithm
            print(f"Enter key pressed. ready_for_algorithm: {self.ready_for_algorithm}")
        
            if self.ready_for_algorithm:
                # Disable wall placement and removal in algorithm mode
                self.placing_walls = False
                self.removing_walls = False
                print("Switching to algorithm mode. Placing walls and removing walls are now disabled.")
            else:
                print("Exiting algorithm mode. You can now place or remove walls.")
    
        elif event.key == pygame.K_SPACE:  # Press Space to remove walls
            print("Space key pressed. Attempting to remove wall.")
            self.remove_wall()

    def handle_mousedown(self, event, running):
        if self.ready_for_algorithm:
            if event.button == 1:  # Left click to set start or end point
                if self.coords.start is None:
                    self.coords.start = (self.mouse_x // self.box_width, self.mouse_y // self.box_width)
                elif self.coords.end is None:
                    self.coords.end = (self.mouse_x // self.box_width, self.mouse_y // self.box_width)
            elif event.button == 3:  # Right click to place walls
                self.placing_walls = True
        else:
            if event.button == 1:  # Left click to set start or end point
                if self.coords.start is None:
                    self.coords.start = (self.mouse_x // self.box_width, self.mouse_y // self.box_width)
                elif self.coords.end is None:
                    self.coords.end = (self.mouse_x // self.box_width, self.mouse_y // self.box_width)
            elif event.button == 3:  # Right click to place walls
                self.placing_walls = True

        # Check if the click is on a button and execute corresponding action
        if event.type == pygame.MOUSEBUTTONDOWN:
            for name, rect in self.buttons.items():
                if rect.collidepoint(self.mouse_x, self.mouse_y):
                    self.button_action(name)
                    print(f"Button {name} clicked.")

    def button_action(self, name):
        print(f"Button {name} pressed")
        if name in {"DFS", "BFS", "Dijkstra", "A*"}:
            self.run_algorithm(name)
        elif name == "Clear":
            self.coords.remove_all()
        elif name == "Random Maze":
            self.coords.generate_random_maze(self)

    def run_algorithm(self, algorithm_name):
        if self.coords.start and self.coords.end:
            self.coords.create_maze(self)
            self.coords.final_path = Pathfinding.pathfind(
                self.coords.maze, self.coords.start, self.coords.end, self, self.coords, algorithm_name
            )

    def place_wall(self):
        try:
            x, y = int(self.mouse_x // self.box_width), int(self.mouse_y // self.box_width)
            if (x, y) != self.coords.start and (x, y) != self.coords.end and (x, y) not in self.coords.walls:
                self.coords.walls.append((x, y))
        except Exception as e:
            print(f"Error placing wall: {e}")

    def remove_wall(self):
        try:
            x, y = self.mouse_x // self.box_width, self.mouse_y // self.box_width
            if (x, y) in self.coords.walls:
                self.coords.walls.remove((x, y))
        except Exception as e:
            print(f"Error removing wall: {e}")

    def redraw(self):
        self.win.fill((255, 255, 255))

        # Draw walls
        for wall in self.coords.walls:
            self.win.blit(self.wall_img, (wall[0] * self.box_width, wall[1] * self.box_width))

        # Draw start and end points
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                if (x, y) == self.coords.start:
                    self.win.blit(self.robot_img, (x * self.box_width, y * self.box_width))
                elif (x, y) == self.coords.end:
                    self.win.blit(self.end_img, (x * self.box_width, y * self.box_width))
                else:
                    pygame.draw.rect(self.win, (200, 200, 200), (x * self.box_width, y * self.box_width, self.box_width, self.box_width), 1)

        # Draw open list nodes with transparency
        for node in self.coords.open_list:
            transparent_surface = pygame.Surface((self.box_width, self.box_width), pygame.SRCALPHA)
            transparent_surface.fill((0, 255, 255, 128))  # RGBA where A (Alpha) is set to 128 (50% transparency)
            self.win.blit(transparent_surface, (node.position[0] * self.box_width, node.position[1] * self.box_width))

        # Draw closed list nodes with transparency
        for node in self.coords.closed_list:
            transparent_surface = pygame.Surface((self.box_width, self.box_width), pygame.SRCALPHA)
            transparent_surface.fill((0, 0, 255, 128))  # RGBA where A (Alpha) is set to 128 (50% transparency)
            self.win.blit(transparent_surface, (node.position[0] * self.box_width, node.position[1] * self.box_width))

        # Draw final path with transparency
        final_path = self.coords.final_path if self.coords.final_path is not None else []
        for node in final_path:
            transparent_surface = pygame.Surface((self.box_width, self.box_width), pygame.SRCALPHA)
            transparent_surface.fill((255, 255, 0, 128))  # RGBA where A (Alpha) is set to 128 (50% transparency)
            self.win.blit(transparent_surface, (node[0] * self.box_width, node[1] * self.box_width))

        # Draw buttons
        for name, rect in self.buttons.items():
            pygame.draw.rect(self.win, (150, 150, 150), rect)
            font = pygame.font.SysFont(None, 24)
            text = font.render(name, True, (255, 255, 255))
            self.win.blit(text, (rect.x + 10, rect.y + 10))
