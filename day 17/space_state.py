from search import *
import copy



directions = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}

def create_matrix(rows):
    mapp = []
    for row in rows:
        tmp = []
        for e in row:
            tmp.append(int(e))
        mapp.append(tmp)

    return mapp



class lava_heat(Problem):
    """
    state: ( )
       }

      """
    def __init__(self, initial, max_steps):
        """ Define goal state and initialize a problem """
        """  state: ((position)) """


        f = open("input", "r")
        l = [  n.replace("\n","" ) for n in f.readlines()  ]

        
        self.initial = initial
        
        self.max_steps = max_steps -1
        self.grid = create_matrix(l)

        self.goal = (len(self.grid)-1,len(self.grid)-1)
        Problem.__init__(self, self.initial, self.goal)

    def actions(self, state):
        possible_actions = []

        for di in directions:
            if di == state[1] and state[2] == self.max_steps:
                #print(state)
                pass
            else:
                tmp = tuple( t + d for t,d in zip(state[0], directions[di]))
                if 0 <= tmp[0] < len(self.grid) and 0 <= tmp[1] < len(self.grid[0]):
                    possible_actions.append(di)


        return possible_actions




    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """
        newstate = [0,0,0]

        #print("state ",state)

        if action == "U":
            newstate[0] = tuple(t + d for t,d in zip(state[0],directions[action]))

        if action == "D":
            newstate[0] = tuple(t + d for t,d in zip(state[0],directions[action]))

        if action == "R":
            newstate[0] = tuple(t + d for t,d in zip(state[0],directions[action]))

        if action == "L":
            newstate[0] = tuple(t + d for t,d in zip(state[0],directions[action]))

        if state[2] < self.max_steps and action == state[1]:
            newstate[2] = state[2]+1
        else:
            newstate[2] = 0

        newstate[1] = action

        return tuple(newstate)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        if self.goal == state[0]:
          print("goal", state)
          return True
        return False

    def path_cost(self, c, state1, action, state2):
        p = state2[0]
        cost = c + self.grid[p[1]][p[1]]
        return cost


    def astar_cost(self,node):
        
        tot = 0
        for n in node.path():
            p = n.state[0]
            tot += self.grid[p[0]][p[1]]
        print(tot)
        return tot + self.h(node)

    def h(self, node):
        return manhattan_distance(node.state[0],self.goal)
    



debug = False
p = lava_heat(((0,0),"D",0),3)

if debug:
    state = ((0,2),0,2)
    possible = p.actions(state)
    for a in possible:
        print(a)
        print(p.result(state,a))
else:
    #s3 = astar_search(p, display=True)
    #print("len ", s3.path_cost, "\nsolution", s3.solution(),"\n")

    s3 = astar_search(p,p.astar_cost)
    print("len ", s3.path_cost, "\nsolution", s3.solution(),"\n")