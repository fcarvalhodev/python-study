#This program is an exercise from chapter 6 of the book "Python Crash Course"
#by Eric Matthes. The exercise is to implement a breadth-first search algorithm
#to find a mango seller in a graph.
#The graph is represented as a dictionary of nodes, where each node is a dictionary of its neighbors.
#The algorithm iterates over the nodes and finds the lowest cost node that has not been processed yet.
#It then updates the costs of the neighbors of this node.
#The O complexity of this algorithm is O(n^2) because it iterates over the nodes and the neighbors of each node.

from collections import deque
def initialize_graph(graph, name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    return search_queue, searched

def person_is_seller(person):
    return person[-1] == 'm'

def add_person_to_search_queue(search_queue, person, graph, searched):
    if person not in searched:
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        else:
            search_queue += graph[person]
            searched.append(person)
    return False

def breadth_first_search(graph, name):
    search_queue, searched = initialize_graph(graph, name)
    while search_queue:
        person = search_queue.popleft()
        if add_person_to_search_queue(search_queue, person, graph, searched):
            return True
    return False

def main():
    graph = {
        "you": ["alice", "bob", "claire"],
        "bob": ["anuj", "peggy"],
        "alice": ["peggy"],
        "claire": ["thom", "jonny"],
        "anuj": [],
        "peggy": [],
        "thom": [],
        "jonny": []
    }
    name = "you"
    result = breadth_first_search(graph, name)
    if not result:
        print("No mango seller found.")

if __name__ == "__main__":
    main()
