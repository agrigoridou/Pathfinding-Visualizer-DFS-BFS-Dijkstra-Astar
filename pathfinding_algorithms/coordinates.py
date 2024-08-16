import random

class Coordinates:
    def __init__(self):
        self.remove_all()  # Initialize with empty values

    def remove_all(self):
        # Reset all attributes to their default values
        self.start = None
        self.end = None
        self.walls = []
        self.maze = []
        self.open_list = []
        self.closed_list = []
        self.final_path = []

    def remove_last(self):
        # Clear maze, open list, closed list, and final path
        self.maze = []
        self.open_list = []
        self.closed_list = []
        self.final_path = []

    def largest_distance(self):
        # Calculate the largest coordinate value in the walls list
        largest = 0
        for wall in self.walls:
            if wall[0] > largest:
                largest = wall[0]
            if wall[1] > largest:
                largest = wall[1]
        return largest + 1  # Add 1 to ensure the maze includes the largest coordinate

    def create_maze(self, gui):
        # Create a maze with walls placed based on the walls list
        largest_distance = self.largest_distance()
        largest = max(gui.grid_size, largest_distance)  # Ensure maze is large enough
        largest = int(largest)  # Convert to integer

        # Initialize maze with zeros
        self.maze = [[0 for x in range(largest)] for y in range(largest)]
        # Place walls in the maze
        for wall in self.walls:
            try:
                wall_x, wall_y = wall
                self.maze[wall_x][wall_y] = 1  # Set wall position to 1
            except:
                pass  # Ignore any errors (e.g., out-of-bounds)

    def generate_random_maze(self, gui):
        # Generate a random maze by randomly placing walls
        self.walls = []
        for i in range(gui.grid_size * gui.grid_size):
            if random.random() > 0.6:  # 40% chance of placing a wall
                wall = (random.randint(0, gui.grid_size - 1), random.randint(0, gui.grid_size - 1))
                if wall not in self.walls:
                    self.walls.append(wall)  # Add wall if it is not already present
