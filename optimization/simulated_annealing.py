import random
import math
'''
General simulated annealing algorithm
initial_state is the starting solution
- randomized appropriately through the domain space
initial_temp is the starting temperature
- best if matches closely with the general range of the function space
final_temp is the ending temperature
alpha is the step size of the temperature as it goes from initial_temp to final_temp
get_cost(x) is the cost function with which to evaluate state x
get_neighbors(x) gets the neighbors of state x
'''
def simulated_annealing(initial_state, initial_temp, final_temp, alpha, get_cost, get_neighbors):
    current_temp = initial_temp
    solution = initial_state

    best_iterate = None
    best_iterate_cost = None

    while current_temp > final_temp:
        neighbor = random.choice(get_neighbors(solution))

        curr_cost = get_cost(solution)

        if best_iterate_cost is None or curr_cost < best_iterate_cost:
            best_iterate_cost = curr_cost
            best_iterate = solution
            print("best iterate cost: ", best_iterate_cost)

        print("curr_cost: ", curr_cost)
        cost_diff = curr_cost - get_cost(neighbor)
        if cost_diff > 0:
            solution = neighbor
        else:
            if random.uniform(0, 1) < math.exp(cost_diff/current_temp):
                solution = neighbor

        current_temp -= alpha
    print(best_iterate)
    return best_iterate

if __name__ == "__main__":
    '''
    Sample code for running simulated annealing on the sample cost and neighbors function
    The start_state and parameters are fixed here for testing, but should be fine tuned in final code
    Note that this isn't really tuned very well
    '''
    start_state = [0, 1]
    initial_temp = 0.4
    final_temp = .0001
    alpha = 0.0001
    '''
    Example cost and get neighbors function which was used to test the simulated annealing approach
    Currently cost is a non-convex function many local minimas
    '''
    def cost_func(state):
        return -(math.sin(state[0])**2+math.cos(state[1])**2)/(5+state[0]**2+state[1]**2)

    '''
    Sample get neighbors function which gets a few nearby points to the current state
    '''
    def neighbors_func(state):
        delta = 0.01
        return [(round(state[0]+delta, 4), round(state[1], 4)),
        (round(state[0]-delta, 4), round(state[1], 4)),
        (round(state[0], 4), round(state[1]+delta, 4)),
        (round(state[0], 4), round(state[1]-delta, 4)),
        (round(state[0]+delta, 4), round(state[1]+delta, 4)),
        (round(state[0]-delta, 4), round(state[1]-delta, 4)),
        (round(state[0]-delta, 4), round(state[1]+delta, 4)),
        (round(state[0]+delta, 4), round(state[1]-delta, 4))]
    simulated_annealing(start_state, initial_temp, final_temp, alpha, cost_func, neighbors_func)
