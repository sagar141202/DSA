# Course Schedule (Topological Sort)

## Problem Statement
Given a number of courses and their prerequisites, determine if it's possible to finish all courses. The courses are represented by an array of pairs, where each pair contains two numbers: the course and its prerequisite. If it's possible to finish all courses, return true; otherwise, return false. For example, if we have courses [[0, 1]] and [[1, 0]], it's impossible to finish both courses because they have a cyclic dependency. However, if we have courses [[1, 0]], it's possible to finish both courses by taking course 0 first and then course 1.

## Approach
We can solve this problem using topological sort with depth-first search (DFS). The idea is to create a graph from the given courses and their prerequisites, then perform DFS to detect any cycles. If a cycle exists, it's impossible to finish all courses.

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
        // Create a graph from the given courses and their prerequisites
        vector<vector<int>> graph(numCourses);
        vector<int> visited(numCourses, 0);
        for (auto& prerequisite : prerequisites) {
            graph[prerequisite[0]].push_back(prerequisite[1]);
        }

        // Perform DFS to detect any cycles
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(graph, visited, i)) {
                return false;
            }
        }

        return true;
    }

    bool dfs(vector<vector<int>>& graph, vector<int>& visited, int course) {
        // If the course is marked as visiting, it means a cycle exists
        if (visited[course] == -1) {
            return false;
        }

        // If the course is marked as visited, it means we've already checked it
        if (visited[course] == 1) {
            return true;
        }

        // Mark the course as visiting
        visited[course] = -1;

        // Check all prerequisites of the course
        for (int prerequisite : graph[course]) {
            if (!dfs(graph, visited, prerequisite)) {
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
- Topological sort can be used to detect cycles in a graph.
- DFS is a suitable algorithm for performing topological sort.
- A course can be marked as visiting or visited to avoid revisiting it and to detect cycles.