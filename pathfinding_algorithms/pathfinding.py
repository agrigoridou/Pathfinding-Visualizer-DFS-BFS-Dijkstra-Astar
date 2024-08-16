from pathfinding_algorithms.node import Node

class Pathfinding:
    @staticmethod
    def pathfind(maze, start, end, gui, coords, key):
        # Initialize start and end nodes
        start_node = Node(None, start)
        end_node = Node(None, end)
        open_list = []  # Nodes to be evaluated
        closed_list = []  # Nodes already evaluated
        open_list.append(start_node)  # Add start node to open list

        while len(open_list) > 0:
            # Get the current node based on the algorithm
            current_node, current_index = Pathfinding.get_current_node(open_list, key)
            open_list.pop(current_index)  # Remove current node from open list
            closed_list.append(current_node)  # Add current node to closed list

            if current_node == end_node:
                # Path found, reconstruct the path
                path = Pathfinding.reconstruct_path(current_node)
                coords.final_path = path
                return path  # Return the path

            # Generate children (neighboring nodes) of the current node
            children = Pathfinding.generate_children(current_node, maze)

            for child in children:
                if child in closed_list:
                    continue  # Skip already evaluated nodes
                Pathfinding.calculate_node_values(child, current_node, end_node, key)
                for open_node in open_list:
                    if child == open_node and child.g >= open_node.g:
                        break  # Skip if child is not better
                else:
                    open_list.append(child)  # Add child to open list

            # Update GUI with current state
            coords.open_list = open_list
            coords.closed_list = closed_list
            gui.main(True)  # Refresh GUI to show current state

        coords.final_path = []  # No path found
        return []  # Return empty path

    @staticmethod
    def get_current_node(open_list, key):
        # Determine which node to process based on the algorithm
        if key == "DFS":
            # Depth-First Search: Last node added (stack behavior)
            current_node = open_list[-1]
            current_index = len(open_list) - 1
        elif key == "BFS":
            # Breadth-First Search: First node added (queue behavior)
            current_node = open_list[0]
            current_index = 0
        elif key == "A*":
            # A*: Node with lowest f value (cost + heuristic)
            current_index, current_node = min(enumerate(open_list), key=lambda x: x[1].f)
        elif key == "Dijkstra":
            # Dijkstra: Node with lowest g value (cost)
            current_index, current_node = min(enumerate(open_list), key=lambda x: x[1].g)
        return current_node, current_index

    @staticmethod
    def reconstruct_path(current_node):
        # Reconstruct the path from end to start by following parent nodes
        path = []
        while current_node is not None:
            path.append(current_node.position)
            current_node = current_node.parent
        return path[::-1]  # Return reversed path

    @staticmethod
    def generate_children(current_node, maze):
        children = []
        # Possible moves: up, right, down, left
        for new_pos in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            node_pos = (int(current_node.position[0] + new_pos[0]), int(current_node.position[1] + new_pos[1]))
            print(f"Generated node position: {node_pos}")  # Debug message
            # Check if the new position is within maze bounds and is not a wall
            if (0 <= node_pos[0] < len(maze)) and (0 <= node_pos[1] < len(maze[0])) and maze[node_pos[0]][node_pos[1]] == 0:
                children.append(Node(current_node, node_pos))
        return children

    @staticmethod
    def calculate_node_values(child, current_node, end_node, key):
        # Calculate g, h, and f values based on the algorithm
        if key == "Dijkstra":
            child.g = current_node.g + 1  # g is the cost from the start node
        elif key == "A*":
            child.g = current_node.g + 1  # g is the cost from the start node
            # Calculate the heuristic (Euclidean distance) for A*
            child.h = (((abs(child.position[0] - end_node.position[0]) ** 2) + 
                        (abs(child.position[1] - end_node.position[1]) ** 2)) ** 0.5)
            child.f = child.g + child.h  # f is the total cost (g + h)
