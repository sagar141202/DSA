# Course Schedule (Topological Sort)

## Problem Statement
Given a number of courses and their prerequisites, determine if it is possible to finish all courses. The courses are represented by an array of pairs, where each pair contains two values: the course number and the number of prerequisites for that course. The prerequisites are given as a 2D array, where each inner array contains a pair of course numbers, the first being the course and the second being its prerequisite. If it is possible to finish all courses, return true; otherwise, return false. For example, if there are 2 courses and the prerequisites are [[1,0]], then it is possible to finish all courses because we can take course 0 first and then course 1. However, if there are 2 courses and the prerequisites are [[1,0],[0,1]], then it is not possible to finish all courses because we cannot take course 0 before course 1 and vice versa.

## Approach
The approach to solve this problem is to use a topological sort algorithm. We create a graph where each course is a node, and the prerequisites are the edges. Then we use a depth-first search (DFS) or breadth-first search (BFS) to traverse the graph. If we encounter a cycle, then it is not possible to finish all courses.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // Create an adjacency list to represent the graph
        vector<vector<int>> graph(numCourses);
        vector<int> visited(numCourses, 0);
        
        // Populate the graph
        for (auto& pair : prerequisites) {
            graph[pair[1]].push_back(pair[0]);
        }
        
        // Perform DFS
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(graph, visited, i)) {
                return false;
            }
        }
        
        return true;
    }
    
    bool dfs(vector<vector<int>>& graph, vector<int>& visited, int node) {
        // If the node is marked as visited, then we have encountered a cycle
        if (visited[node] == 1) {
            return false;
        }
        
        // If the node is marked as completed, then we do not need to visit it again
        if (visited[node] == 2) {
            return true;
        }
        
        // Mark the node as visited
        visited[node] = 1;
        
        // Visit all the neighbors of the node
        for (auto& neighbor : graph[node]) {
            if (!dfs(graph, visited, neighbor)) {
                return false;
            }
        }
        
        // Mark the node as completed
        visited[node] = 2;
        
        return true;
    }
};
```

## Test Cases
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
```

## Key Takeaways
- Topological sort can be used to solve problems that involve ordering a set of items based on their dependencies.
- DFS or BFS can be used to perform a topological sort on a graph.
- If a cycle is encountered during the topological sort, then it is not possible to order the items based on their dependencies.