import pygame
import sys

DEBUG = len(sys.argv) > 1
if DEBUG:
    print("Debug mode ON")


class Cell:
    def __init__(self):
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.vacant = False   # False = wall, True = open passage
        self.visited = False  # Prevents revisiting during search
        self.on_path = False  # Marked True when part of the found path

    def copy_from(self, other: "Cell"):
        """Copy attributes from another Cell instance."""
        self.north = other.north
        self.south = other.south
        self.east = other.east
        self.west = other.west
        self.vacant = other.vacant
        self.visited = other.visited
        self.on_path = other.on_path


# --- How to use ---
# Left click cells to carve open passages (build your maze).
# Right click a cell to search for a path from there to the east wall.
# The found path will be highlighted in red.

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Creation")
clock = pygame.time.Clock()

GREEN  = (0, 255, 0)
YELLOW = (255, 255, 100)
RED    = (255, 0, 0)

MAP_WIDTH  = SCREEN_WIDTH
MAP_HEIGHT = SCREEN_HEIGHT
CELL_DIM   = 60

x_cell_count = MAP_WIDTH  // CELL_DIM
y_cell_count  = MAP_HEIGHT // CELL_DIM

# --- Build the 2D grid of cells ---
maze: list[list[Cell]] = []
for i in range(x_cell_count):
    maze.append([])
    for j in range(y_cell_count):
        maze[i].append(Cell())

# --- Link each cell to its neighbours (N/S/E/W) ---
# Cells on the boundary simply get None on that side.
col = 0
while col < x_cell_count:
    row = 0
    while row < y_cell_count:
        current_cell = maze[col][row]

        if col < x_cell_count - 1: current_cell.east  = maze[col + 1][row]
        if col > 0:                current_cell.west  = maze[col - 1][row]
        if row > 0:                current_cell.north = maze[col][row - 1]
        if row < y_cell_count - 1: current_cell.south = maze[col][row + 1]

        row += 1
    col += 1

# --- Print neighbour links for every cell (debug / verification) ---
c = 0
while c < x_cell_count:
    r = 0
    while r < y_cell_count:
        current_cell = maze[c][r]

        n = 1 if current_cell.north else 0
        s = 1 if current_cell.south else 0
        e = 1 if current_cell.east  else 0
        w = 1 if current_cell.west  else 0

        print(f"Cell x: {c}, y:{r}, north:{n}, south:{s}, east:{e}, west:{w}")
        r += 1

    print("---------- End of Column ----------")
    c += 1


def search(cell_x, cell_y):
    """
    Recursively search for a path from (cell_x, cell_y) to the east wall.
    Returns the path as a list of [x, y] positions, or None if no path exists.
    """
    current_cell = maze[cell_x][cell_y]

    # Skip walls and already-visited cells to avoid infinite loops
    if not current_cell.vacant or current_cell.visited:
        return None

    current_cell.visited = True

    
    if cell_x == (MAP_WIDTH // CELL_DIM) - 1:
        if DEBUG:
            print("End of one path x:", cell_x, "y:", cell_y)
        return [[cell_x, cell_y]]

    north_path = south_path = east_path = west_path = None

    if DEBUG:
        print("Searching. In cell x:", cell_x, "y:", cell_y)

    # Try each direction; stop as soon as one succeeds
    if current_cell.north:
        north_path = search(cell_x, cell_y - 1)

    if north_path is None and current_cell.south:
        south_path = search(cell_x, cell_y + 1)

    if north_path is None and south_path is None and current_cell.east:
        east_path = search(cell_x + 1, cell_y)

    if north_path is None and south_path is None and east_path is None and current_cell.west:
        west_path = search(cell_x - 1, cell_y)

    # Use whichever direction returned a valid path
    path = north_path or south_path or east_path or west_path

    if path is not None:
        if DEBUG:
            print("Added x:", cell_x, "y:", cell_y)
        return [[cell_x, cell_y]] + path
    else:
        if DEBUG:
            print("Dead end x:", cell_x, "y:", cell_y)
        return None


def walk(path):
    """Mark every cell along the found path so it renders in red."""
    if path is None:
        return
    for cell_x, cell_y in path:
        maze[cell_x][cell_y].on_path = True


def reset_search_state():
    """Clear visited and on_path flags before each new search or edit."""
    for c in range(x_cell_count):
        for r in range(y_cell_count):
            maze[c][r].visited = False
            maze[c][r].on_path = False


# --- Main loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        elif event.type == pygame.MOUSEBUTTONDOWN:
            col = event.pos[0] // CELL_DIM
            row = event.pos[1] // CELL_DIM

            if event.button == 1:  # Left click: toggle wall/open
                maze[col][row].vacant = not maze[col][row].vacant
                reset_search_state()  # Redraw path from scratch after any edit

            if event.button == 3:  # Right click: find path from this cell
                reset_search_state()
                path = search(col, row)
                walk(path)

    # --- Render ---
    screen.fill((0, 0, 0))
    for col in range(x_cell_count):
        for row in range(y_cell_count):
            cell = maze[col][row]
            color = YELLOW if cell.vacant else GREEN
            if cell.on_path:
                color = RED
            pygame.draw.rect(screen, color, (col * CELL_DIM, row * CELL_DIM, CELL_DIM - 1, CELL_DIM - 1))

    pygame.display.flip()
    clock.tick(60)