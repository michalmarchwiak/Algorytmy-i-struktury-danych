from zadanie1 import Graph
from queue import Queue

def generate_successors(state):
    successors = []
    x, y = state
    max_x, max_y = 3, 4

    successors.append((max_x, y))
    successors.append((x, max_y))
    successors.append((0, y))
    successors.append((x, 0))

    pour = min(x, max_y - y)
    successors.append((x - pour, y + pour))


    pour = min(y, max_x - x)
    successors.append((x + pour, y - pour))

    return list(set(successors))


def solve_water_jug_problem():
    start_state = (0, 0)
    goal_states = {(2, 0), (0, 2)}

    graph = Graph()

    visited_states = set()
    queue = Queue()
    queue.enqueue(start_state)

    while not queue.is_empty():
        current_state = queue.dequeue()
        if current_state in visited_states:
            continue

        visited_states.add(current_state)
        graph.add_vertex(current_state)
        print(f"Current state: {current_state}")

        for successor in generate_successors(current_state):
            graph.add_vertex(successor)
            graph.add_edge(current_state, successor, 1)

            if successor not in visited_states:
                queue.enqueue(successor)

    start_vertex = graph.get_vertex(start_state)
    visited = graph.bfs(start_vertex)




    for vertex_id in visited:
        if eval(vertex_id) in goal_states:
            path = []
            current_vertex = graph.get_vertex(eval(vertex_id))
            while current_vertex:
                path.append(eval(current_vertex.get_id()))
                current_vertex = current_vertex.get_predecessor()

            return path[::-1]
    return None

solution = solve_water_jug_problem()
if solution:
    print("Rozwiązanie (kolejne stany):")
    for step in solution:
        print(step)


