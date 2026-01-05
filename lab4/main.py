def get_possible_states(state):

    new_states = []

    for row in range(8):

        curr_column = state[row]

        if curr_column > 0:
            temp_list = list(state)
            temp_list[row] = curr_column - 1
            new_states.append(tuple(temp_list))

        if curr_column < 7:
            temp_list = list(state)
            temp_list[row] = curr_column + 1
            new_states.append(tuple(temp_list))

    return new_states



def h_function(state):

    final_state = [3, 2, 0, 1, 7, 6, 4, 5]

    heur = 0

    for i in range(8):
        difference = abs(state[i] - final_state[i])
        heur += difference

    return heur




def a_star(start, end):
    
    open_set = {start}
    closed_set = set()
    g = {start: 0}
    parents = {start: None}

    while len(open_set) > 0:
        current_state = min(open_set, key=lambda x: g[x] + h_function(x))

        if current_state == end:
            break
        
        open_set.remove(current_state)
        closed_set.add(current_state)

        print(current_state)

        set_new_states = get_possible_states(current_state)

        for neighbor in set_new_states:

            if neighbor in closed_set:
                continue

            neighbor_price = g[current_state] + 1

            if neighbor not in open_set or neighbor_price < g.get(neighbor, float('inf')):

                parents[neighbor] = current_state
                g[neighbor] = neighbor_price
                open_set.add(neighbor)

    path = []
    curr = current_state

    while curr is not None:
        path.append(curr)
        curr = parents[curr]
    
    path.reverse()

    print("Zavrseno")
    print(current_state)
    return path



a_star((3, 2, 3, 3, 7, 6, 2, 1), (3, 2, 0, 1, 7, 6, 4, 5))