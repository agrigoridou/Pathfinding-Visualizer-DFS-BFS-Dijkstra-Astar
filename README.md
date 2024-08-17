# Pathfinding-Visualizer(DFS-BFS-Dijkstra-A*)

A tool for visualizing pathfinding algorithms, allowing users to create mazes and watch their solution using popular algorithms such as DFS, BFS, Dijkstra, and A*.

<div align="center">
    <img src="https://github.com/user-attachments/assets/e777c7fb-d3ce-4861-a350-74cc0bfcc28d" alt="image"height="600" >
</div>

## Features
- **Algorithm Visualization:** See in real-time how DFS, BFS, Dijkstra, and A* algorithms search for a path through a maze.
- **Maze Creation:** Create custom mazes by placing walls, as well as start and end points.
- **Random Mazes:** Generate random mazes to test the algorithms.
- **Clearing:** Easily remove walls and reset the grid for a new search.

## Prerequisites
To run this project, you will need:

- Python 3.x
- Pygame

To install the required libraries, run the following command:

```bash
pip install pygame
```

## Installation Instructions
- Clone the repository or download the files.
- Ensure that you have installed the prerequisites.
- Run main.py to start the application.

## Usage Instructions
- **Starting:** Once the application starts, a grid will appear.
- **Placing Walls:** Use right-click to place walls and left-click to set the start or end point.
- **Running Algorithms:** Press the Enter key to select an algorithm and then press the corresponding buttons for DFS, BFS, Dijkstra, or A* to view their visualization.
- **Random Mazes:** Click the "Random Maze" button to generate a random maze.
- **Clearing:** Use the "Clear" button to remove all walls and reset the grid.

## Code Structure
- **main.py:** The entry point of the application.
- **gui.py:** Contains the Gui class that manages the graphical user interface and interactions.
- **pathfinding_algorithms:** Folder containing the code for the pathfinding algorithms and maze handling.
- **coordinates.py:** Contains the Coordinates class for managing the maze and the algorithms' paths.
- **pathfinding.py:** Contains the Pathfinding class with methods implementing the DFS, BFS, Dijkstra, and A* algorithms.




### Example Results

<div align="center">
  
### DFS
<img src="https://github.com/user-attachments/assets/ae5c62e8-1a36-46ae-b872-f641750dc91b" alt="DFS Example GIF">

### BFS
<img src="https://github.com/user-attachments/assets/b6bf6a32-db8e-4c0d-b2a3-865e4edca30a" alt="BFS Example GIF">

### Dijkstra
<img src="https://github.com/user-attachments/assets/c35ba312-ea29-474d-be7d-2e83f09ef858" alt="Dijkstra Example GIF">

### A*
<img src="https://github.com/user-attachments/assets/9bb4a534-c2b2-4576-9bd4-21d138f71638" alt="A* Example GIF">

</div>





