# https://leetcode.com/problems/course-schedule-ii/

# Solution 1

    # A course has 3 possible states:
    # visited -> a course (crs) has been added to output
    # visiting -> crs not added to output, but added to cycle
    # unvisited -> crs not added to output or cycle

output = []
visit, cycle = set(), set()


# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # A list of lists to represent an adjacency list
        self.prereq = [[] for num in range(n)]
 
        # add edges to the directed graph
        for (crs, pre) in edges:
            self.prereq[crs].append(pre)


# Function to perform DFS traversal on the graph on a graph
def DFS(graph, crs):
    if crs in cycle:
        return False
    if crs in visit:
        return True
    
    cycle.add(crs)
    for pre in graph.prereq[crs]:
        if DFS(graph, pre) == False:
            return False
    cycle.remove(crs)
    visit.add(crs)
    output.append(crs)
    return True


if __name__ == '__main__':
 
    # List of graph edges as per the above diagram
    edges = [
        # Notice that node 0 is unconnected
        (1, 0), (2, 0), (3, 1), (3, 2)
        #(1, 0), (2, 0), (3, 2), (0, 1)
    ]
 
    # total number of nodes in the graph (labelled from 0 to 12)
    numCourses = 4
 
    # build a graph from the given edges
    graph = Graph(edges, numCourses)
 
    # Perform DFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    for i in range(numCourses):
        if DFS(graph, i) == False:
            print([])
            break
    print(output)


# Solution as 1 function (as LeetCode requires to)

# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         prereq = [[] for pre in range(numCourses)]
#         for crs, pre in prerequisites:
#             prereq[crs].append(pre)
            
#         output = []
#         visit, cycle = set(), set()
        
#         def DFS(crs):
#             if crs in cycle:
#                 return False
#             if crs in visit:
#                 return True

#             cycle.add(crs) 
#             for pre in prereq[crs]:
#                 if DFS(pre) == False:
#                     return False
#             cycle.remove(crs)
#             visit.add(crs)
#             output.append(crs)
#             return True

#         for course in range(numCourses):
#             if DFS(course) == False:
#                 return []
#         return output