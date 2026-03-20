# Course Schedule (Topological Sort)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return `true` if you can finish all courses, and `false` otherwise. For example, if `numCourses = 2` and `prerequisites = [[1,0]]`, you can finish all courses because you can take course `0` first and then take course `1`. However, if `numCourses = 2` and `prerequisites = [[1,0],[0,1]]`, you cannot finish all courses because you cannot take course `0` and course `1` at the same time.

## Approach
The problem can be solved using Topological Sort, which is a linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. We can use Depth-First Search (DFS) or Breadth-First Search (BFS) to perform the Topological Sort. In this case, we will use DFS.

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
        vector<int> visited(numCourses, 0); // 0: not visited, 1: visiting, 2: visited

        // Build the graph
        for (const auto& prerequisite : prerequisites) {
            graph[prerequisite[1]].push_back(prerequisite[0]);
        }

        // Perform DFS for each unvisited node
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(graph, visited, i)) {
                return false;
            }
        }

        return true;
    }

    // Helper function to perform DFS
    bool dfs(vector<vector<int>>& graph, vector<int>& visited, int node) {
        // If the node is being visited, it means there's a cycle
        if (visited[node] == 1) {
            return false;
        }

        // If the node has been visited, return true
        if (visited[node] == 2) {
            return true;
        }

        // Mark the node as being visited
        visited[node] = 1;

        // Visit all its neighbors
        for (const auto& neighbor : graph[node]) {
            if (!dfs(graph, visited, neighbor)) {
                return false;
            }
        }

        // Mark the node as visited
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
- Topological Sort can be used to solve problems involving Directed Acyclic Graphs (DAGs).
- Depth-First Search (DFS) can be used to perform Topological Sort.
- The problem can be solved by detecting cycles in the graph, which indicates that it's not possible to finish all courses.