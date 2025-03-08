initial_state = [
      [1, 0, 2],
      [4, 6, 3],
      [7, 5, 8]
  ]


goal_state = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 0]
  ]

def find_empty_tile(state):
    """Find the position of the empty tile (0) in the puzzle."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def possible_moves(state):
    """Generate all possible moves from the current state."""
    new_states = []
    x, y = find_empty_tile(state)

    # Define the possible directions
    directions = {
        "up": (x - 1, y),
        "down": (x + 1, y),
        "left": (x, y - 1),
        "right": (x, y + 1),
    }

    # Check if each move is within bounds
    for move, (new_x, new_y) in directions.items():
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            # Create a new state by copying the current state
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            new_states.append(new_state)

    return new_states

def dfs_search(initial_state, goal_state):
    stack = [initial_state]
    visited = [initial_state]
    nodes_explored = 0

    if initial_state == goal_state:
        return True, visited, nodes_explored

    while stack:
        current_state = stack.pop()  # Récupère le dernier élément de la pile
        nodes_explored += 1

        if current_state == goal_state:
            return True, visited, nodes_explored

        for new_state in possible_moves(current_state):
            if new_state not in visited:
                stack.append(new_state)  # Ajoute le nouvel état à la pile
                visited.append(new_state)  # Marque comme visité

    return False, visited, nodes_explored



result, visited_nodes, explored_nodes = dfs_search(initial_state, goal_state)
print(f"Goal Found: {result}")
print(f"Visited Nodes: {len(visited_nodes)}")
print(f"Nodes Explored: {explored_nodes}")

print(dfs_search(initial_state, goal_state))
