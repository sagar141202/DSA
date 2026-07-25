# Course Schedule (Topological Sort)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from 0 to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Given the array `prerequisites` and `numCourses`, is it possible for you to finish all courses? If it's possible, return `true`; otherwise, return `false`. For example, if `numCourses = 2` and `prerequisites = [[1,0]]`, the output should be `true` because you can take course 0 first and then course 1.

## Approach
We can solve this problem using a topological sort with a depth-first search (DFS) approach. The idea is to build a graph based on the given prerequisites and then check if there is a cycle in the graph. If a cycle exists, it's impossible to finish all courses; otherwise, it's possible.

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
        // Build the graph
        vector<vector<int>> graph(numCourses);
        vector<int> visited(numCourses, 0);
        for (auto& prerequisite : prerequisites) {
            graph[prerequisite[1]].push_back(prerequisite[0]);
        }

        // Check if there is a cycle using DFS
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(graph, visited, i)) {
                return false;
            }
        }
        return true;
    }

    bool dfs(vector<vector<int>>& graph, vector<int>& visited, int course) {
        // If the course is marked as visiting, it means there is a cycle
        if (visited[course] == -1) {
            return false;
        }
        // If the course is already visited, return true
        if (visited[course] == 1) {
            return true;
        }
        // Mark the course as visiting
        visited[course] = -1;
        // Visit all the neighboring courses
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
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
```

## Key Takeaways
- Topological sort can be used to solve problems that involve ordering objects based on their dependencies.
- DFS is a useful algorithm for detecting cycles in a graph.
- Using a visited array can help avoid revisiting the same nodes multiple times and improve the efficiency of the algorithm.