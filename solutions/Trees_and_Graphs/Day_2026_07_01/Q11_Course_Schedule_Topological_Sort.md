# Course Schedule (Topological Sort)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return `true` if you can finish all courses, otherwise return `false`. For example, if `numCourses = 2` and `prerequisites = [[1,0]]`, you can finish all courses because you can take course `0` first and then course `1`. On the other hand, if `numCourses = 2` and `prerequisites = [[1,0],[0,1]]`, you cannot finish all courses because you cannot take course `0` and course `1` at the same time.

## Approach
We can solve this problem using Topological Sort with Depth-First Search (DFS). The idea is to build a graph based on the given prerequisites and then check if there is a cycle in the graph. If there is a cycle, it means we cannot finish all courses.

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
        // Create a graph
        vector<vector<int>> graph(numCourses);
        vector<int> visited(numCourses, 0);
        
        // Build the graph
        for (const auto& prerequisite : prerequisites) {
            graph[prerequisite[1]].push_back(prerequisite[0]);
        }
        
        // Check for cycle using DFS
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(graph, visited, i)) {
                return false;
            }
        }
        
        return true;
    }
    
    bool dfs(const vector<vector<int>>& graph, vector<int>& visited, int node) {
        // If the node is being visited, it means there is a cycle
        if (visited[node] == -1) {
            return false;
        }
        
        // If the node has been visited, return true
        if (visited[node] == 1) {
            return true;
        }
        
        // Mark the node as being visited
        visited[node] = -1;
        
        // Visit all the neighbors
        for (const auto& neighbor : graph[node]) {
            if (!dfs(graph, visited, neighbor)) {
                return false;
            }
        }
        
        // Mark the node as visited
        visited[node] = 1;
        
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
- Topological Sort can be used to solve problems that involve ordering or scheduling.
- DFS can be used to detect cycles in a graph.
- The `visited` array can be used to keep track of the nodes that have been visited during the DFS traversal.