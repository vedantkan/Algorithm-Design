#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import time

def printPath(parent, j): # used to print the shortest path when called
    if parent[j] == -1:
        print(j, end=" ")
        return
    printPath(parent, parent[j])
    print(j, end=" ")

class Node_Distance : # used for node distance

    def __init__(self, name, dist) :
        self.name = name
        self.dist = dist

class Graph :   # used to create functions for graph on taking input

    def __init__(self, node_count) :
        self.adjlist = {}
        self.node_count = node_count
        
    
    def Add_Into_Adjlist(self, src, node_dist) :     # create and add values into an adjacency list
        if src not in self.adjlist :
            self.adjlist[src] = []
        self.adjlist[src].append(node_dist)

    def Dijkstras_Shortest_Path(self, source) :  # dijkstra's algorithm to calculate the shortest path
        
        distance = [999999999999] * self.node_count
        distance[source] = 0
        parent = [-1 for _ in range(self.node_count)]
        dict_node_length = {source: 0}

        while dict_node_length :
            source_node = min(dict_node_length, key = lambda k: dict_node_length[k])
            del dict_node_length[source_node]

            for node_dist in self.adjlist[source_node] :
                adjnode = node_dist.name
                length_to_adjnode = node_dist.dist

                if distance[adjnode] > distance[source_node] + length_to_adjnode :
                    distance[adjnode] = distance[source_node] + length_to_adjnode
                    dict_node_length[adjnode] = distance[adjnode]
                    parent[adjnode] = source_node

        if (source == 197 or source == 65 or source == 187):
            for i in range(self.node_count):
                if (source == 197 and i == 27):
                    print("\n\nTest Case: 1\nFrom Node: " + str(source) + " \nTo Node: " + str(i) + " \nDistance: " + str(distance[i]) + " feet \nShortest Path:")
                    printPath(parent, i)
                if (source == 65 and i == 280):
                    print("\n\nTest Case: 2\nFrom Node: " + str(source) + " \nTo Node: " + str(i) + " \nDistance: " + str(distance[i]) + " feet \nShortest Path:")
                    printPath(parent, i)
                if (source == 187 and i == 68):
                    print("\n\nTest Case: 3\nFrom Node: "+str(source)+" \nTo Node: "+str(i)+" \nDistance: "  + str(distance[i]) + " feet \nShortest Path:")
                    printPath(parent, i)

# read the input files, create a list and call the dijkstra function to compute the shortest path
def main() :
    with open('./Project2_Input_Files/Project2_Input_File4.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                lastVertex = int(row[0])
        v = lastVertex + 1

    g = Graph(v)    
    with open('./Project2_Input_Files/Project2_Input_File4.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        graph = [[0 for i in range(v)] for j in range(v)]
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                g.Add_Into_Adjlist(int(row[0]), Node_Distance(int(row[1]),int(row[2])))
                graph[int(row[0])][int(row[1])] = int(row[2])                
                line_count += 1

    for i in range(v):
        g.Dijkstras_Shortest_Path(i)

if __name__ == "__main__" :
    start = time.time()
    main()
    end = time.time()
    runtime = end - start;  # calculate the program runtime
    print("\n\nRuntime: " + str(runtime))

