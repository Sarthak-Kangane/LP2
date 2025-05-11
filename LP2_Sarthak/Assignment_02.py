import heapq

# 1. Helpers

def manhattan(state, goal):
    """Sum of Manhattan distances of each tile from its goal position."""
    dist = 0
    for i, tile in enumerate(state):
        if tile == 0: continue
        goal_i = goal.index(tile)
        dist += abs(i//3 - goal_i//3) + abs(i%3 - goal_i%3)
    return dist

def neighbors(state):
    """Generate all states by sliding the blank (0) up/down/left/right."""
    zero = state.index(0)
    x, y = divmod(zero, 3)
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            nz = nx*3 + ny
            new = list(state)
            new[zero], new[nz] = new[nz], new[zero]
            yield tuple(new)

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

# 2. A* Search

def a_star(start, goal):
    open_heap = []
    heapq.heappush(open_heap, (manhattan(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}
    
    while open_heap:
        f, g, current = heapq.heappop(open_heap)
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for nb in neighbors(current):
            tentative_g = g + 1
            if tentative_g < g_score.get(nb, float('inf')):
                g_score[nb] = tentative_g
                f_nb = tentative_g + manhattan(nb, goal)
                heapq.heappush(open_heap, (f_nb, tentative_g, nb))
                came_from[nb] = current

    return None  # no solution

# 3. Example Usage

if __name__ == "__main__":
    start = (1,2,3,
             0,4,6,
             7,5,8)
    goal  = (1,2,3,
             4,5,6,
             7,8,0)

    path = a_star(start, goal)
    if path:
        print(f"Solved in {len(path)-1} moves:")
        for state in path:
            for i in range(0,9,3):
                print(state[i:i+3])
            print()
    else:
        print("No solution found.")
