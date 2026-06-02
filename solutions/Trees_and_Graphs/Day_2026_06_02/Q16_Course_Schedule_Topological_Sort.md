# Course Schedule (Topological Sort)

## Problem Statement
Given a number of courses and their prerequisites, determine if it's possible to finish all courses. The courses are represented by an array of pairs, where each pair contains two values: the course and its prerequisite. For example, if we have a course 0 with a prerequisite 1, it means we must take course 1 before taking course 0. We should return true if it's possible to finish all courses, and false otherwise. There are n courses and m prerequisites, and we can assume that the input is a 2D array where each sub-array contains two integers representing a course and its prerequisite.

## Approach
We can solve this problem using topological sort with depth-first search (DFS) or breadth-first search (BFS). The idea is to build a graph from the given courses and prerequisites, then check for any cycles in the graph. If a cycle exists, it means we cannot finish all courses.

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
        vector<int> visited(numCourses, 0); // 0 - unvisited, 1 - visiting, 2 - visited
        
        // Build the graph
        for (auto& p : prerequisites) {
            graph[p[1]].push_back(p[0]);
        }
        
        // Perform DFS
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(graph, visited, i)) {
                return false;
            }
        }
        
        return true;
    }
    
    bool dfs(vector<vector<int>>& graph, vector<int>& visited, int course) {
        // If the course is being visited, it means a cycle is detected
        if (visited[course] == 1) {
            return false;
        }
        
        // If the course has been visited, return true
        if (visited[course] == 2) {
            return true;
        }
        
        // Mark the course as being visited
        visited[course] = 1;
        
        // Visit all neighbors of the course
        for (int neighbor : graph[course]) {
            if (!dfs(graph, visited, neighbor)) {
                return false;
            }
        }
        
        // Mark the course as visited
        visited[course] = 2;
        
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
- Topological sort can be used to solve problems involving directed acyclic graphs (DAGs).
- DFS is a suitable approach for detecting cycles in a graph.
- Using a visited array can help keep track of the state of each node during the DFS traversal.