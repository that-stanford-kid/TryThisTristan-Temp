"""
Created on Sun Mar 27 18:44:00 2022
dijkstra_Algorithm 
@author: p0ne
"""
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns
import numpy as np
import string 
import json_wrapper
import graphviz as viz


graph = {
    
'a':{'b':3,'c':4, 'd':7},
'b':{'c':1,'f':5},
'c':{'f':6,'d':2},
'd':{'e':3, 'g':6},
'e':{'g':3, 'h':4},
'f':{'e':1, 'h':8},
'g':{'h':2},
'h':{'g':2}
}

def dijkstraAlgorithm(graph,start,goal):
    shortest_distance = {} # mange the cost to reach to the desired node, update as we move in graph
    track_predecessor = {} # track the path that led us to this node
    unseenNodes = graph # iterates through the entire graph
    infinity = 9999999999999 # infinity allows any very large number "inf" | --oo.
    track_path = [] # trace our traversal back to sour node - optimal route to take.
    
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    
    while unseenNodes:
        
        min_distance_node = None
        
        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node
                
        path_options = graph[min_distance_node].items()
        
        for child_node, weight in path_options:
            
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node
                
        unseenNodes.pop(min_distance_node)
        
    currentNode = goal
    
    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
            
        except KeyError:
            print("Path not in reach")
            break
        
    track_path.insert(0,start)
    
    # --oo | inf
    if shortest_distance[goal] != infinity:
        print("shortest distance is " + str(shortest_distance[goal]))
        print("optimal choice of path is " + str(track_path))
        print("P.ONEIL")
        print("queue fifo- value of x1 for n queue " + str(track_path)) 

dijkstraAlgorithm(graph, 'a', 'h')
