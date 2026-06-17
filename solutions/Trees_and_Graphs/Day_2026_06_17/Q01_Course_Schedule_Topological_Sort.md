# Course Schedule (Topological Sort)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from 0 to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return `true` if you can finish all courses, and `false` otherwise.

## Approach
The problem can be solved using Topological Sort, a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. We will use Depth-First Search (DFS) to detect cycles in the graph.

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
        // Create adjacency list
        vector<vector<int>> graph(numCourses);
        vector<int> visited(numCourses, 0);
        
        // Build the graph
        for (auto& edge : prerequisites) {
            graph[edge[1]].push_back(edge[0]);
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
        // If the node is marked as visiting, it means a cycle is detected
        if (visited[node] == -1) {
            return false;
        }
        
        // If the node is already visited, return true
        if (visited[node] == 1) {
            return true;
        }
        
        // Mark the node as visiting
        visited[node] = -1;
        
        // Recur for all neighboring nodes
        for (int neighbor : graph[node]) {
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
- Topological Sort can be used to solve problems involving dependencies between objects.
- DFS can be used to detect cycles in a graph.
- The `visited` array can be used to keep track of the visiting status of each node.