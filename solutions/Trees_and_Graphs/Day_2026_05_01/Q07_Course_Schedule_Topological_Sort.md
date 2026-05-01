# Course Schedule (Topological Sort)

## Problem Statement
Given a number of courses and their prerequisites, determine if it is possible to finish all courses. The courses are represented by an array of pairs, where each pair contains two values: the course number and the prerequisite course number. For example, if we have `numCourses = 2` and `prerequisites = [[1,0]]`, this means we have two courses (0 and 1) and course 1 has a prerequisite of course 0. We need to find out if it is possible to take all courses based on the given prerequisites. If it is possible, return `true`; otherwise, return `false`. The constraints are `1 <= numCourses <= 1000` and `0 <= prerequisites.length <= numCourses * (numCourses - 1) / 2`.

## Approach
We can solve this problem using a topological sort algorithm, which is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. If a cycle is detected, then it is not possible to finish all courses.

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
        for (const auto& pair : prerequisites) {
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

    bool dfs(const vector<vector<int>>& graph, vector<int>& visited, int node) {
        if (visited[node] == 1) {
            // Cycle detected
            return false;
        }
        if (visited[node] == 2) {
            // Already visited
            return true;
        }
        visited[node] = 1; // Mark as visiting
        for (const auto& neighbor : graph[node]) {
            if (!dfs(graph, visited, neighbor)) {
                return false;
            }
        }
        visited[node] = 2; // Mark as visited
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
- Detecting cycles in a graph can be done using DFS or BFS algorithms.
- The time complexity of the solution depends on the number of nodes and edges in the graph.