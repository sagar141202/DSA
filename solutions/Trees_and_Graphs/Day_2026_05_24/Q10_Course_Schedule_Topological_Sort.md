# Course Schedule (Topological Sort)

## Problem Statement
Given a number of courses (`numCourses`) and a list of prerequisite pairs (`prerequisites`), determine if it's possible to finish all courses. Each prerequisite pair is represented as an array where the first element is the course and the second element is the prerequisite. For example, if `prerequisites[i] = [a, b]`, then course `a` must be taken after course `b`. The function should return `true` if it's possible to finish all courses and `false` otherwise. The number of courses will not exceed 10^5, and the number of prerequisites will not exceed 10^5.

## Approach
The problem can be solved using a topological sort algorithm. We create a graph where each course is a node, and the prerequisites are the edges. We then perform a depth-first search (DFS) to detect any cycles in the graph. If a cycle is found, it's impossible to finish all courses.

## Complexity
- Time: O(N + M)
- Space: O(N + M)

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
            graph[prerequisite[0]].push_back(prerequisite[1]);
        }

        // Perform DFS to detect cycles
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(graph, visited, i)) {
                return false;
            }
        }

        return true;
    }

    // Helper function to perform DFS
    bool dfs(const vector<vector<int>>& graph, vector<int>& visited, int course) {
        if (visited[course] == 1) {
            // If we're visiting a node that's already being visited, there's a cycle
            return false;
        }

        if (visited[course] == 2) {
            // If we've already visited this node, we don't need to visit it again
            return true;
        }

        visited[course] = 1; // Mark as visiting

        // Visit all the neighbors
        for (const auto& neighbor : graph[course]) {
            if (!dfs(graph, visited, neighbor)) {
                return false;
            }
        }

        visited[course] = 2; // Mark as visited

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
- Topological sort can be used to detect cycles in a directed graph.
- DFS is a useful algorithm for detecting cycles and performing topological sorts.
- The visited array can be used to keep track of the state of each node during the DFS traversal.