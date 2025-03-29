from zadanie1 import Graph
from queue import Queue

def is_valid_state(missionaries, cannibals):
    return (
        (0 <= missionaries <= 3) and
        (0 <= cannibals <= 3) and
        (missionaries == 0 or missionaries >= cannibals)
    )


def generate_successors(state):
    successors = []
    missionaries, cannibals, boat_side = state

    if boat_side == 'L':
        delta = -1
    else:
        delta = 1

    possible_moves = [
        (1, 0),
        (0, 1),
        (1, 1),
        (2, 0),
        (0, 2),
    ]

    for move in possible_moves:
        m_move, c_move = move
        new_state = (
            missionaries + delta * m_move,
            cannibals + delta * c_move,
            'R' if boat_side == 'L' else 'L'
        )
        if is_valid_state(new_state[0], new_state[1]) and is_valid_state(
            3 - new_state[0], 3 - new_state[1]
        ):
            successors.append(new_state)

    return successors


def solve_missionaries_and_cannibals():
    start_state = (3, 3, 'L')
    goal_state = (0, 0, 'R')

    graph = Graph()

    queue = Queue()
    queue.enqueue(start_state)
    graph.add_vertex(start_state)
    visited = {start_state: None}

    while not queue.is_empty():
        current_state = queue.dequeue()

        if current_state == goal_state:
            path = []
            while current_state is not None:
                path.append(current_state)
                current_state = visited[current_state]
            return path[::-1]

        for successor in generate_successors(current_state):
            if successor not in visited:
                graph.add_vertex(successor)
                graph.add_edge(current_state, successor, 1)
                queue.enqueue(successor)
                visited[successor] = current_state

    return None

solution = solve_missionaries_and_cannibals()
if solution:
    print("Rozwiązanie (kolejne stany):")
    for step in solution:
        print(step)
else:
    print("Nie znaleziono rozwiązania.")