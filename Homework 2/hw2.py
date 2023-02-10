#input will be stored in a dictionary, so 'A' = {"B"} or 2 = {1, 5, 6, 3}
#use dict to do DFS
import sys

def represents_int(s):
    '''
    helper function to check if a string is an integer.
    '''
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True

def makeDict():
    '''
    function to make a dict to store key value pairs
    '''
    d = {}
    t = int(input())
    n = 0
    temp = input()
    while (t >= 0):
        temp = input() 
        if represents_int(temp) and n == 0: 
            n = int(temp) - 1 
        else: 
            s = temp
            split = s.split(' ')
            split.pop(0)
            key  = split[0]
            d[key] = split
            t -= 1
    return d 


def dfs(visited, graph, node):  
    '''
    DFS function
    ''' 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

graph = makeDict()
visited = set()
keys = list(graph.keys())

dfs(visited, graph, graph[keys[0]])