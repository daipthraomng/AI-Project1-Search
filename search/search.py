# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # lay ra trang thai ban dau cua agent va kiem tra goal state
    start_State = problem.getStartState()
    if problem.isGoalState(start_State):
        return []
    # luu cac state da di qua
    visited = []
    # tao stack luu state 
    st = util.Stack()
    # push trang thai ban dau va 
    # duong di den trang thai do hien tai la rong
    st.push((start_State, []))
    # khi stack con thi duyet
    while not st.isEmpty():
        # lay ra State CUOI CUNG 
        (current_State, path) = st.pop()
        if current_State not in visited:
            # cho state vao visited 
            visited.append(current_State)
            # kiem tra goal state
            if problem.isGoalState(current_State):
                return path
            # push cac state lien ke duong di den state do
            for successor in problem.getSuccessors(current_State):
                next_state = successor[0]
                path_to_next_state = path + [successor[1]]
                st.push((next_state, path_to_next_state))
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start_State = problem.getStartState()
    if problem.isGoalState(start_State):
        return []
    # luu cac state da di qua
    visited = []
    # tao stack luu state 
    q = util.Queue()
    # push trang thai ban dau va 
    # duong di den trang thai do hien tai la rong
    q.push((start_State, []))
    # khi stack con thi duyet
    while not q.isEmpty():
        # lay ra State CUOI CUNG 
        (current_State, path) = q.pop()
        if current_State not in visited:
            # cho state vao visited 
            visited.append(current_State)
            # kiem tra goal state
            if problem.isGoalState(current_State):
                return path
            # push cac state lien ke duong di den state do
            for successor in problem.getSuccessors(current_State):
                next_state = successor[0]
                path_to_next_state = path + [successor[1]]
                q.push((next_state, path_to_next_state))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start_State = problem.getStartState()
    if problem.isGoalState(start_State):
        return []
    # luu cac state da di qua
    visited = []
    # tao hang doi uu tien luu state
    pq = util.PriorityQueue()
    # truyen ten 
    # duong di
    # gia tri den duong di  
    # gia tri uu tien
    # ham push sap xep phan tu trong priority queue vao dung vi tri
    pq.push((start_State, [], 0), 0)
    while not pq.isEmpty():
        (current_State, path, cost) = pq.pop()
        if problem.isGoalState(current_State):
            return path
        if current_State not in visited:
            # push ...
            visited.append(current_State)
            for successor in problem.getSuccessors(current_State):
                # truyen vao ham push 2 tham so
                # mot la object state
                # hai la tham so priority duoc cap nhat theo cost
                next_state = successor[0]
                path_to_next_state = path + [successor[1]]
                cost_to_nextState = cost + successor[2]
                priority = cost + successor[2]
                pq.push((next_state, path_to_next_state, cost_to_nextState), priority)

    
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # tuong tu uniformCostSearch, chi khac priority duoc cap nhat bang cost + heuristic o phan push vao priority queue
    start_State = problem.getStartState()
    if problem.isGoalState(start_State):
        return []
    # luu cac state da di qua
    visited = []
    # tao hang doi uu tien luu state
    pq = util.PriorityQueue()
    pq.push((start_State, [], 0), 0)
    while not pq.isEmpty():
        (current_State, path, cost) = pq.pop()
        if problem.isGoalState(current_State):
            return path
        if current_State not in visited:
            visited.append(current_State)
            for successor in problem.getSuccessors(current_State):
                next_state = successor[0]
                path_to_next_state = path + [successor[1]]
                cost_to_nextState = cost + successor[2]
                priority = cost_to_nextState + heuristic(successor[0], problem)
                pq.push((next_state, path_to_next_state, cost_to_nextState), priority)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
