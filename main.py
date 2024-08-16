import pygame
from gui import Gui
from pathfinding_algorithms.coordinates import Coordinates

def main():
    # Initialize the Coordinates object to manage the maze and pathfinding data
    coords = Coordinates()
    
    # Initialize the GUI with the Coordinates object for visualization and interaction
    gui = Gui(coords)

    # Main loop to keep the application running
    while True:
        gui.main()  # Call the main method of the GUI to handle events and update the display

# Entry point of the script
if __name__ == "__main__":
    main()  # Execute the main function if this script is run directly
