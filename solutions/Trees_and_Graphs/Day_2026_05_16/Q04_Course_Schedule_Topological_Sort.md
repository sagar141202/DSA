# Course Schedule (Topological Sort)

## Problem Statement
Given a number of courses and their prerequisites, determine if it's possible to finish all courses. The input is a 2D array where each pair represents a course and its prerequisite. For example, `[1, 0]` means course 1 requires course 0 as a prerequisite. If it's possible to finish all courses, return true; otherwise, return false. There are `numCourses` courses in total, labeled from 0 to `numCourses - 1`. 

## Approach
The problem can be solved using a topological sort algorithm, which detects cycles in a directed graph. If a cycle exists, it's impossible to finish all courses. We will use a depth-first search (DFS) to traverse the graph and detect any cycles.

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
        
        // Build the graph
        for (auto& pair : prerequisites) {
            graph[pair[1]].push_back(pair[0]);
        }
        
        // Perform DFS to detect cycles
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(graph, visited, i)) {
                return false;
            }
        }
        
        return true;
    }
    
    bool dfs(vector<vector<int>>& graph, vector<int>& visited, int course) {
        // If the course is marked as visiting, a cycle is detected
        if (visited[course] == -1) {
            return false;
        }
        
        // If the course is already visited, return true
        if (visited[course] == 1) {
            return true;
        }
        
        // Mark the course as visiting
        visited[course] = -1;
        
        // Visit all neighboring courses
        for (int neighbor : graph[course]) {
            if (!dfs(graph, visited, neighbor)) {
                return false;
            }
        }
        
        // Mark the course as visited
        visited[course] = 1;
        
        return true;
    }
};
```

## Test Cases
```
Input: numCourses = 2, prerequisites = [[1, 0]]
Output: true
Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
Output: false
```

## Key Takeaways
- Topological sort is used to detect cycles in a directed graph.
- DFS is used to traverse the graph and detect cycles.
- A course is marked as visiting if it's currently being visited, and marked as visited if all its prerequisites are visited.