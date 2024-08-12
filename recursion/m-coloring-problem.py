"""
Problem Statement: Given an undirected graph and a number m, determine if the graph can be colored
with at most m colors such that no two adjacent vertices of the graph are colored with the same color.

Examples:

Example 1:
Input:
N = 4
M = 3
E = 5
Edges[] = {
  (0, 1),
  (1, 2),
  (2, 3),
  (3, 0),
  (0, 2)
}

Output: 1

Explanation: It is possible to colour the given graph using 3 colours.

Example 2:

Input:
N = 3
M = 2
E = 3
Edges[] = {
  (0, 1),
  (1, 2),
  (0, 2)
}

Output: 0


Explanation: It is not possible to color.
Solution
Disclaimer: Don't jump directly to the solution, try it out yourself first.

Solution 1: Backtracking

Approach:

Basically starting from vertex 0 color one by one the different vertices.

Base condition:

If I have colored all the N nodes return true.

Recursion:

Trying every color from 1 to m with the help of a for a loop.

Is safe function returns true if it is possible to color it with that color i.e none of the adjacent
nodes have the same color.

In case this is an algorithm and follows a certain intuition, please mention it.

Color it with color i then call the recursive function for the next node if it returns true we will return true.

And If it is false then take off the color.

Now if we have tried out every color from 1 to m and it was not possible to color it with any of the m colors
then return false.

Time Complexity: O( N^M) (n raised to m)
Space Complexity: O(N)


"""


def isSafe(node, color, graph, n, col):
    for k in range(n):
        if k != node and graph[k][node] == 1 and color[k] == col:
            return False
    return True


def solve(node, color, m, N, graph):
    if node == N:
        return True

    for i in range(1, m + 1):
        if isSafe(node, color, graph, N, i):
            color[node] = i
            if solve(node + 1, color, m, N, graph):
                return True
            color[node] = 0

    return False


# Function to determine if graph can be coloured with at most M colours such
# that no two adjacent vertices of graph are coloured with same colour.


def graphColoring(graph, m, N):
    color = [0] * N
    if solve(0, color, m, N, graph):
        return True
    return False


if __name__ == '__main__':
    N = 4
    m = 3

    graph = [[0 for i in range(101)] for j in range(101)]

    # Edges are (0, 1), (1, 2), (2, 3), (3, 0), (0, 2)
    graph[0][1] = 1
    graph[1][0] = 1
    graph[1][2] = 1
    graph[2][1] = 1
    graph[2][3] = 1
    graph[3][2] = 1
    graph[3][0] = 1
    graph[0][3] = 1
    graph[0][2] = 1
    graph[2][0] = 1

    print(1 if graphColoring(graph, m, N) else 0)
