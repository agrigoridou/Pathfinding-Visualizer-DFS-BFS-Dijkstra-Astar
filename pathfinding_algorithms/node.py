class Node:
    def __init__(self, parent, position):
        self.parent = parent  # Parent node in the pathfinding tree
        self.position = (int(position[0]), int(position[1]))  # Position of the node in the maze, converted to integers
        self.h = 0  # Heuristic cost (used in A* algorithm)
        self.f = 0  # Total cost (g + h) used in pathfinding algorithms

    def __eq__(self, other):
        # Nodes are considered equal if they have the same position
        return self.position == other.position
