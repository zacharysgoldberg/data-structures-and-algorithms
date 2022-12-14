from helpers import AdjNode, Node
from singly_linked_lists import LinkedList
from collections import deque


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices
        self.array = [LinkedList() for _ in range(self.vertices)]

    def add_edge_lst(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.array[source].insert_node_at_head(destination)

    def add_edge(self, source, destination):
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

    def print_graph_lst(self):
        for i in range(self.vertices):
            temp = self.array[i].head
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next

    def print_graph(self):
        for i in range(self.vertices):
            temp = self.graph[i]
            while temp:
                print(temp.vertex, end=" -> ")
                temp = temp.next


def bfs_helper(g, source, visited):
    result = ''
    visited[source] = True
    queue = [source]
    while queue:
        s = queue.pop(0)
        result += str(s)
        adjacent = g.array[s].head
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

# DFS for LinkedLists


def dfs_helper(g, source, visited):
    result = []
    visited[source] = True
    stack = [source]
    while stack:
        node = stack.pop()
        result.append(node)
        adjacent = g.array[node].head
        while adjacent:
            if visited[adjacent.data] is False:
                stack.append(adjacent.data)
                visited[adjacent.data] = True
            adjacent = adjacent.next
    return result


def dfs_traversal(g, source):
    visited = [False] * g.vertices
    result = dfs_helper(g, source, visited)
    # if source did not start prior to an unvisited vertice,
    # revisit vertices starting from that one and all other unvisited vertices found
    for i in range(g.vertices):
        if visited[i] is False:
            res, visited = dfs_helper(g, i, visited)
            result += res
    return result

# DFS Recursive


def dfs_rec(g, source, visited):
    visited[source] = True
    adjacent = g.graph[source]
    while adjacent:
        if visited[adjacent.vertex] is False:
            print(adjacent.vertex, end=" ")
            dfs_rec(g, adjacent.vertex, visited)
        adjacent = adjacent.next

# Node Graph iterative DFS


def dfs(g, source, visited):
    result = []
    visited[source] = True
    stack = [source]
    while stack:
        node = stack.pop()
        result.append(node)
        adjacent = g.graph[node]
        while adjacent:
            if visited[adjacent.vertex] is False:
                stack.append(adjacent.vertex)
                visited[adjacent.vertex] = True
            adjacent = adjacent.next
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
    adjacent = g.array[curr].head
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
    adjacent = g.array[curr].head
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
    adjacent = g.array[source].head
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
    adjacent = g.array[source].head
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
        adjacent = g.array[node].head
        while adjacent:
            if visited[adjacent.data] is False or adjacent.data == destination:
                queue.append(adjacent.data)
                visited[adjacent.data] = True
                distance[adjacent.data] = distance[node] + 1
                if adjacent.data == destination:
                    return distance[destination]
            adjacent = adjacent.next
    return None


def number_of_nodes(g, level):
    visited = [0] * g.vertices
    queue = deque([0])
    visited[0] = 1
    while queue:
        node = queue.popleft()
        adjacent = g.graph[node].head
        while adjacent:
            if visited[adjacent.data] == 0:
                queue.append(adjacent.data)
                # while visiting each node, the level of that node is set with an increment in the level of its parent node
                # This is how the level of each node is determined
                visited[adjacent.data] = visited[node] + 1
            adjacent = adjacent.next
    count = 0
    for i in range(g.vertices):
        if visited[i] == level:
            count += 1
    return count


def transpose(g):
    new_graph = Graph(g.vertices)  # Creating a new graph
    for source in range(g.vertices):
        while g.graph[source]:
            destination = g.graph[source].vertex
            # swap destination and source (transpose)
            new_graph.add_edge(destination, source)
            g.graph[source] = g.graph[source].next

    return new_graph


# DFS


def find_all_paths(g, source, destination):
    visited = [False] * g.vertices
    all_paths = []
    find_all_paths_rec(g, source, destination, visited, [], all_paths)
    return all_paths


def find_all_paths_rec(g, source, destination, visited, path, all_paths):
    visited[source] = True
    path.append(source)
    adjacent = g.graph[source]
    if source == destination:
        all_paths.append(list(path))
    else:
        while adjacent:
            if visited[adjacent.vertex] is False:
                find_all_paths_rec(g, adjacent.vertex,
                                   destination, visited, path, all_paths)
            adjacent = adjacent.next
    # Remove current vertex from path and mark it as unvisited
    path.pop()
    visited[source] = False


def is_strongly_connected(g):
    visited = [False] * g.vertices
    # Return False if all vertices are not visited in DFS
    dfs_rec(g, 0, visited)
    if any(not i for i in visited):
        return False
    # Do same for transposed graph
    new_g = transpose(g)
    visited = [False] * new_g.vertices
    dfs_rec(new_g, 0, visited)
    if any(not i for i in visited):
        return False

    return True


def connected_components(g):
    visited = [False] * g.vertices
    connected_components = []
    for v in range(len(visited)):
        if visited[v] is False:
            result = dfs(g, v, visited)
            print(result)
            connected_components.append(list(result))
    return connected_components

# Clone Directed Graph


def clone(root):
    nodes = {}
    return clone_rec(root, nodes)


def clone_rec(root, nodes):
    if root is None:
        return None

    node = Node(root.data)
    nodes.update({root: node})
    for neighbor in root.neighbors:
        n = nodes.get(neighbor)
        if n is None:
            node.neighbors.append(clone_rec(neighbor, nodes))
        else:
            node.neighbors.append(n)
    return node


# Tasks Scheduling
    """ 1. Initialize a hashmap of node to parent count.
        2. Go through the nodes, count how many parents each node has (a parent node means another node pointing to the current).
        3. Push the nodes with 0 parents into the queue.
        4. Pop each node from the queue, subtract 1 from the parent count of each node it points to.
        5. If a node's parent count drops to 0, then push it into the queue.
        6. repeat until the queue is empty. If the queue is not empty, then there must be a cycle.
    """


def is_scheduling_possible(tasks, prerequisites):
    sorted_order = []
    queue = deque()
    node_count = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for prereq in prerequisites:
        parent, child = prereq
        graph[parent].append(child)
        node_count[child] += 1

    for node in node_count:
        if node_count[node] == 0:
            queue.append(node)

    while queue:
        vertex = queue.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            node_count[child] -= 1
            if node_count[child] == 0:
                queue.append(child)
    # [Find Order]
    # print(sorted_order)
    if len(sorted_order) == tasks:
        return True
    return False


# All Tasks Scheduling Orders


def print_orders(tasks, prerequisites):
    sorted_order = []
    queue = deque()
    node_count = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for prereq in prerequisites:
        parent, child = prereq
        graph[parent].append(child)
        node_count[child] += 1

    for node in node_count:
        if node_count[node] == 0:
            queue.append(node)

    all_topological_orders(sorted_order, node_count, graph, queue)


def all_topological_orders(sorted_order, node_count, graph, queue):
    if queue:
        for vertex in queue:
            sorted_order.append(vertex)
            queue_for_next_call = deque(queue)
            queue_for_next_call.remove(vertex)
            for child in graph[vertex]:
                node_count[child] -= 1
                if node_count[child] == 0:
                    queue_for_next_call.append(child)

            all_topological_orders(
                sorted_order, node_count, graph, queue_for_next_call)

            sorted_order.remove(vertex)
            for child in graph[vertex]:
                node_count[child] += 1
    if len(sorted_order) == len(node_count):
        print(sorted_order)


# Alien Dictionary


def find_order(words):
    if len(words) == 0:
        return ""

    in_degree = {}
    graph = {}
    for word in words:
        for char in word:
            in_degree[char] = 0
            graph[char] = []

    for i in range(len(words) - 1):
        char1, char2 = words[i], words[i + 1]
        for j in range(min(len(char1), len(char2))):
            parent, child = char1[j], char2[j]
            if parent != child:  # if the two characters are different put the child into it's parent's list
                graph[parent].append(child)
                in_degree[child] += 1
                break  # only the first different character between the two words will help us find the order

    sources = deque()
    for char in in_degree:
        if in_degree[char] == 0:
            sources.append(char)

    sorted_order = []
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
    # Check for cyclic dependency
    if len(sorted_order) != len(in_degree):
        return ""

    return "".join(sorted_order)


if __name__ == "__main__":
    # g = Graph(5)

    # g.add_edge_lst(0, 1)
    # g.add_edge_lst(0, 2)
    # g.add_edge_lst(1, 3)
    # g.add_edge_lst(2, 3)

    # g.add_edge(0, 1)
    # g.add_edge(0, 2)
    # g.add_edge(1, 3)
    # g.add_edge(1, 4)

    g = Graph(7)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 5)
    g.add_edge(2, 5)
    g.add_edge(5, 6)
    g.add_edge(3, 6)

    # g.add_edge(0, 1)
    # g.add_edge(1, 2)
    # g.add_edge(2, 3)
    # g.add_edge(3, 0)
    # g.add_edge(4, 5)
    # g.add_edge(5, 6)

    # g = Graph(5)
    # g.add_edge(0, 1)
    # g.add_edge(1, 2)
    # g.add_edge(2, 3)
    # g.add_edge(2, 4)
    # g.add_edge(3, 0)
    # g.add_edge(4, 2)

    # print(g.print_graph_lst())
    # print(g.print_graph())
    # print(connected_components(g))
    # print(bfs_traversal(g, 0))
    # print(dfs_traversal(g, 1))
    # print(is_strongly_connected(g))
    print(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]]))
    print_orders(
        6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
