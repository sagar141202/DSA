# Course Schedule (Topological Sort)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses-1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return `true` if you can finish all courses, and `false` otherwise. For example, if `numCourses = 2` and `prerequisites = [[1,0]]`, then you can take course `0` first and then course `1`, so the function should return `true`. However, if `numCourses = 2` and `prerequisites = [[1,0],[0,1]]`, then there is a cycle in the graph and you cannot finish all courses, so the function should return `false`.

## Approach
The problem can be solved using Topological Sort, which is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. We can use a graph and a visited array to detect cycles. If a cycle is detected, we return `false`, otherwise we return `true`.

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
        for (auto& prereq : prerequisites) {
            graph[prereq[1]].push_back(prereq[0]);
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
        // If the node is marked as visiting, then a cycle is detected
        if (visited[node] == -1) {
            return false;
        }
        
        // If the node is already visited, then return true
        if (visited[node] == 1) {
            return true;
        }
        
        // Mark the node as visiting
        visited[node] = -1;
        
        // Visit all the neighbors
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
- Topological Sort can be used to detect cycles in a directed graph.
- We can use DFS to perform Topological Sort.
- If a cycle is detected, we return `false`, otherwise we return `true`.