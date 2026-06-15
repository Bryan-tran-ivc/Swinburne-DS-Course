import pygame
import sys

DEBUG = len(sys.argv) > 1
if DEBUG:
    print("Debug mode ON")

class Cell:
    def __init__(self):
        # Set pointers to None
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        # record whether this cell is vacant
        # default is not vacant i.e is a wall.
        self.vacant = False
        # this stops cycles - set when you travel through a cell
        self.visited = False
        self.on_path = False

    def copy_from(self, other: "Cell"):
        """Copy attributes from another Cell instance."""
        self.north = other.north
        self.south = other.south
        self.east = other.east
        self.west = other.west
        self.vacant = other.vacant
        self.visited = other.visited
        self.on_path = other.on_path


# Instructions:
# Left click on cells to create a maze with at least one path moving from
# left to right.  The right click on a cell for the program to find a path
# through the maze. When a path is found it will be displayed in red.

# Initialize Pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Creation")
clock = pygame.time.Clock()

# Setup Colours
GREEN = (0, 255, 0)
YELLOW = (255, 255, 100)
RED = (255, 0, 0)
# Maze Parameters
MAP_WIDTH = SCREEN_WIDTH
MAP_HEIGHT = SCREEN_HEIGHT
CELL_DIM = 60

x_cell_count = MAP_WIDTH // CELL_DIM
y_cell_count = MAP_HEIGHT // CELL_DIM
# Create Maze Grid (dimensions: columns x rows) and populate Cells
#maze = [[Cell() for _ in range(y_cell_count)] for _ in range(x_cell_count)]
maze : list[list[Cell]] = []

for i in range(x_cell_count):
    maze.append([])

    for j in range(y_cell_count):
        maze[i].append(Cell())

# Task: Neighbour Links
# now set up the neighbour links
# You need to do this using a while loop with another
# nested while loop inside.

col = 0 
while col < x_cell_count:
    row = 0 
    while row < y_cell_count:
        current_cell = maze[col][row]

        if col < x_cell_count - 1 :
            current_cell.east = maze[col+1][row]
        if col > 0 : 
            current_cell.west = maze[col - 1][row] 
        if row > 0: 
            current_cell.north = maze[col][row - 1]
        if row < y_cell_count - 1: 
            current_cell.south = maze[col][row + 1] 
        row += 1
    col += 1

# Task: Print Maze
# Now create a function to print out the maze and display the neighbour links
c = 0 
while c < x_cell_count:
    r = 0 
    while r < y_cell_count:
        current_cell = maze[c][r]

        if current_cell.north != None: 
            n = 1 
        else: n = 0 
        if current_cell.south != None: 
            s = 1 
        else: s = 0 
        if current_cell.east != None: 
            e = 1 
        else: e = 0 
        if current_cell.west != None: 
            w = 1 
        else: w = 0 
        print(f"Cell x: {c}, y:{r}, north:{n}, south:{s}, east:{e}, west:{w}")

        r += 1
    print("---------- End of Column ----------")
    c += 1

    

# start a recursive search for paths from the selected cell
# it searches till it hits the East 'wall' then stops
# it does not necessarily find the shortest path

# Completing this function is NOT NECESSARY for the Maze Creation task
# complete the following for the Maze Search task - after
# # we cover Recusion in the lectures.
# But you DO need to complete it later for the Maze Search task
def search(cell_x, cell_y):

    dead_end = False
    path_found = False

    # Base case: reached the east wall (exit)
    if cell_x == (MAP_WIDTH // CELL_DIM) - 1:
        if DEBUG:  # debug
            print("End of one path x:", cell_x, "y:", cell_y)

        return [[cell_x, cell_y]]  # We are at the east wall - exit

    else:
        north_path = None
        west_path = None
        east_path = None
        south_path = None

        if DEBUG:  # debug
            print("Searching. In cell x:", cell_x, "y:", cell_y)

        # INSERT MISSING CODE HERE!!
        # You need to have 4 'if' tests to check each surrounding cell.
        # Make use of the attributes for cells such as vacant, visited
        # and on_path.
        # Cells on the outer boundaries will always have None on the
        # boundary side
        # Check North

        # Pick one of the possible paths that is not None (if any):
        path = None
        if north_path is not None:
            path = north_path
        elif south_path is not None:
            path = south_path
        elif east_path is not None:
            path = east_path
        elif west_path is not None:
            path = west_path

        # A path was found:
        if path is not None:
            if DEBUG:  # debug
                print("Added x:", cell_x, "y:", cell_y)

            return [[cell_x, cell_y]] + path

        else:
            if DEBUG:  # debug
                print("Dead end x:", cell_x, "y:", cell_y)

            return None  # dead end
        
def walk(path):
    """Mark the cells on the given path."""
    if path is None:
        return

    for position in path:
        cell_x, cell_y = position
        cell = maze[cell_x][cell_y]
        cell.on_path = True

# Pygame main loop - For now this just handles quitting the window
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        # Check for mouse click event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:   # Left click toggles cell vacancy
                # Get the position of the click
                mouse_pos = event.pos # event.pos is a tuple (x, y)
                # Determine which cell was clicked
                col = mouse_pos[0] // CELL_DIM
                row = mouse_pos[1] // CELL_DIM
                # Toggle the cell's vacant status
                cell = maze[col][row]
                cell.vacant = not cell.vacant
            if event.button == 3:   # Right click starts search
                # Get the position of the click
                mouse_pos = event.pos # event.pos is a tuple (x, y)
                # Determine which cell was clicked
                col = mouse_pos[0] // CELL_DIM
                row = mouse_pos[1] // CELL_DIM
                # search using the cell given
                path = search(col, row)
                walk(path)

    # Draw the cells onto the screen
    screen.fill((0, 0, 0))  # Clear screen with black
    for col in range(x_cell_count):
        for row in range(y_cell_count):
            cell = maze[col][row]
            color = YELLOW if cell.vacant else GREEN
            if cell.on_path:
                color = RED
            pygame.draw.rect(screen, color, (col * CELL_DIM, row * CELL_DIM, CELL_DIM - 1, CELL_DIM - 1))
    
    pygame.display.flip() # Update the full display Surface to the screen
    clock.tick(60)         # wait until next frame (at 60 FPS)
