# Course Schedule (Topological Sort)

## Problem Statement
Given the number of courses `n` and a list of prerequisite pairs `prerequisites` where `prerequisites[i] = [ai, bi]` means that to take course `bi`, you must first take course `ai`, determine if it's possible to finish all courses. If it's possible, return `true`. Otherwise, return `false`. There are no duplicate edges and no self-loops in the graph. For example, if `n = 2` and `prerequisites = [[1,0]]`, it's possible to finish all courses by taking course 0 first and then taking course 1. However, if `n = 2` and `prerequisites = [[1,0],[0,1]]`, it's impossible to finish all courses because taking course 0 requires taking course 1, but taking course 1 requires taking course 0.

## Approach
The problem can be solved by using a topological sort. We build a graph based on the given prerequisites and then use a depth-first search (DFS) to detect any cycles. If a cycle is found, it means that it's impossible to finish all courses.

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
        // Build the graph
        vector<vector<int>> graph(numCourses);
        vector<int> visited(numCourses, 0);
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

    bool dfs(vector<vector<int>>& graph, vector<int>& visited, int course) {
        // If the course is already visited and in the current path, there's a cycle
        if (visited[course] == -1) {
            return false;
        }
        // If the course is already visited and not in the current path, return true
        if (visited[course] == 1) {
            return true;
        }
        // Mark the course as visited and in the current path
        visited[course] = -1;
        // Visit all the prerequisites
        for (int neighbor : graph[course]) {
            if (!dfs(graph, visited, neighbor)) {
                return false;
            }
        }
        // Mark the course as visited and not in the current path
        visited[course] = 1;
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
- Topological sort can be used to detect cycles in a graph.
- DFS can be used to perform a topological sort.
- The `visited` array can be used to keep track of the visited nodes and detect cycles.