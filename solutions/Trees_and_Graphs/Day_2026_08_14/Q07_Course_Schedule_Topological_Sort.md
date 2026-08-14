# Course Schedule (Topological Sort)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from 0 to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return `true` if you can finish all courses, otherwise return `false`. For example, if `numCourses = 2` and `prerequisites = [[1,0]]`, you can take course 0 first and then course 1, so the function should return `true`. If `numCourses = 2` and `prerequisites = [[1,0],[0,1]]`, it's impossible to take both courses, so the function should return `false`.

## Approach
The problem can be solved using Topological Sort, which is a linear ordering of vertices in a directed acyclic graph (DAG). We can use a depth-first search (DFS) or breadth-first search (BFS) algorithm to perform the topological sort. If a cycle is detected during the sort, it means that it's impossible to finish all courses.

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
        // Create a graph using an adjacency list
        vector<vector<int>> graph(numCourses);
        vector<int> visited(numCourses, 0); // 0: not visited, 1: visiting, 2: visited

        // Build the graph
        for (const auto& prerequisite : prerequisites) {
            graph[prerequisite[1]].push_back(prerequisite[0]);
        }

        // Perform DFS
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(graph, visited, i)) {
                return false;
            }
        }

        return true;
    }

    bool dfs(const vector<vector<int>>& graph, vector<int>& visited, int course) {
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

        // Visit all the neighboring courses
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
- Use Topological Sort to solve the problem.
- Detect cycles during the sort to determine if it's possible to finish all courses.
- Use DFS or BFS to perform the topological sort.