import re
from helpers import AdjNode
from singly_linked_lists import LinkedList


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        for i in range(vertices):
            self.graph.append(LinkedList())

    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.graph[source].insert_node_at_head(destination)

    def print_graph(self):
        for i in range(self.vertices):
            temp = self.graph[i].head
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next


def bfs_helper(g, source, visited):
    result = ''
    visited[source] = True
    queue = [source]
    while queue:
        s = queue.pop(0)
        result += str(s)
        adjacent = g.graph[s].head
        while adjacent:
            if visited[adjacent.data] is False:
                queue.append(adjacent.data)
                visited[adjacent.data] = True
            adjacent = adjacent.next
    return result, visited

# BFS slower than DFS


def bfs_traversal(g, source):
    visited = [False] * g.vertices
    result, visited = bfs_helper(g, source, visited)
    # if source did not start prior to an unvisited vertice,
    # revisit vertices starting from that one and all other unvisited vertices found
    for i in range(g.vertices):
        if visited[i] is False:
            res, visited = bfs_helper(g, i, visited)
            result += res
    return result


def dfs_helper(g, source, visited):
    result = ''
    visited[source] = True
    stack = [source]
    while stack:
        node = stack.pop()
        result += str(node)
        adjacent = g.graph[node].head
        while adjacent:
            if visited[adjacent.data] is False:
                stack.append(adjacent.data)
                visited[adjacent.data] = True
            adjacent = adjacent.next
    return result, visited


def dfs_traversal(g, source):
    visited = [False] * g.vertices
    result, visited = dfs_helper(g, source, visited)
    # if source did not start prior to an unvisited vertice,
    # revisit vertices starting from that one and all other unvisited vertices found
    for i in range(g.vertices):
        if visited[i] is False:
            res, visited = dfs_helper(g, i, visited)
            result += res
    return result

# Detect Cycle in a Directed Graph


def detect_cycle(g):
    visited = [False] * g.vertices
    if detect_cycle_rec(g, 0, visited, -1):
        return True
    return False

# DFS


def detect_cycle_rec(g, curr, visited, parent):
    visited[curr] = True
    adjacent = g.graph[curr].head
    while adjacent:
        if visited[adjacent.data] is False:
            if detect_cycle_rec(g, adjacent.data, visited, curr):
                return True
        # If adjacent vertice is visited and not the parent node of the current node
        elif adjacent.data is not parent:
            return True
        adjacent = adjacent.next
    return False


# Check if graph is a tree for undirected graph
# Conditions: 1. No cycles  2. Is Connected
def is_tree(g):
    visited = [False] * g.vertices
    if check_cycle(g, 0, visited, -1):
        return False
    for i in range(len(visited)):
        if visited[i] is False:
            return False
    return True


def check_cycle(g, curr, visited, parent):
    visited[curr] = True
    adjacent = g.graph[curr].head
    while adjacent:
        if visited[adjacent.data] is False:
            if check_cycle(g, adjacent.data, visited, curr):
                return True
        # If adjacent vertice is visited and not the parent node of the current node
        elif adjacent.data is not parent:
            return True
        adjacent = adjacent.next
    return False

# DFS O(V + E)


def find_mother_vertex(g):
    visited = [False] * g.vertices
    mother_vertex = 0
    for i in range(g.vertices):
        if visited[i] is False:
            find_mother_vertex_helper(g, i, visited)
            mother_vertex = i
    visited = [False] * g.vertices
    find_mother_vertex_helper(g, mother_vertex, visited)
    if any(i is False for i in visited):
        return -1
    return mother_vertex


def find_mother_vertex_helper(g, source, visited):
    visited[source] = True
    adjacent = g.graph[source].head
    while adjacent:
        if visited[adjacent.data] is False:
            find_mother_vertex_helper(g, adjacent.data, visited)
        adjacent = adjacent.next


# DFS

def check_path(g, source, destination):
    visited = [False] * g.vertices
    check_path_rec(g, source, destination, visited)
    if visited[destination] is False:
        return False
    return True


def check_path_rec(g, source, destination, visited):
    visited[source] = True
    adjacent = g.graph[source].head
    while adjacent:
        if visited[adjacent.data] is False:
            check_path_rec(g, adjacent.data, destination, visited)
        adjacent = adjacent.next

# BFS


def find_min_path(g, source, destination):
    visited = [False] * g.vertices
    visited[source] = True
    queue = [source]
    distance = [0] * g.vertices
    while queue:
        node = queue.pop(0)
        adjacent = g.graph[node].head
        while adjacent:
            if visited[adjacent.data] is False or adjacent.data == destination:
                queue.append(adjacent.data)
                visited[adjacent.data] = True
                distance[adjacent.data] = distance[node] + 1
                if adjacent.data == destination:
                    return distance[destination]
            adjacent = adjacent.next
    return None


if __name__ == "__main__":
    # g = Graph(4)

    # g.add_edge(0, 1)
    # g.add_edge(0, 2)
    # g.add_edge(1, 3)
    # g.add_edge(2, 3)

    # g.add_edge(0, 1)
    # g.add_edge(1, 2)
    # g.add_edge(3, 0)
    # g.add_edge(3, 1)

    g = Graph(7)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 5)
    g.add_edge(2, 5)
    g.add_edge(5, 6)
    g.add_edge(3, 6)

    print(g.print_graph())
    # print(bfs_traversal(g, 0))
    # print(dfs_traversal(g, 1))
    print(find_min_path(g, 1, 5))
