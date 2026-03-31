# Course Schedule (Topological Sort)

## Problem Statement
Given a number of courses (`numCourses`) and a list of prerequisite pairs (`prerequisites`), determine if it's possible to finish all courses. Each prerequisite pair is represented as an array where the first element is the course and the second element is the prerequisite. For example, `[1, 0]` means you need to take course `0` before course `1`. If it's possible to finish all courses, return a boolean indicating that it's possible. Otherwise, return a boolean indicating that it's not possible. The constraints are `1 <= numCourses <= 2000` and `0 <= prerequisites.length <= numCourses * (numCourses - 1) / 2`.

## Approach
We can solve this problem using a topological sort algorithm, which is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. The intuition is to find if there's a cycle in the graph, in which case it's impossible to finish all courses.

## Complexity
- Time: O(numCourses + prerequisites.size())
- Space: O(numCourses + prerequisites.size())

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // Create an adjacency list representation of the graph
        vector<vector<int>> graph(numCourses);
        vector<int> visited(numCourses, 0); // 0: not visited, 1: visiting, 2: visited

        // Build the graph
        for (const auto& pair : prerequisites) {
            graph[pair[1]].push_back(pair[0]);
        }

        // Check for cycles using DFS
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(graph, visited, i)) {
                return false;
            }
        }

        return true;
    }

    bool dfs(const vector<vector<int>>& graph, vector<int>& visited, int course) {
        // If we're visiting a course and it's already being visited, there's a cycle
        if (visited[course] == 1) {
            return false;
        }

        // If we've already visited this course, return true
        if (visited[course] == 2) {
            return true;
        }

        // Mark the course as being visited
        visited[course] = 1;

        // Visit all the neighbors of the course
        for (const auto& neighbor : graph[course]) {
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
Input: numCourses = 2, prerequisites = [[1, 0]]
Output: true
Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
Output: false
```

## Key Takeaways
- Topological sort can be used to detect cycles in a directed graph.
- DFS is a suitable algorithm for detecting cycles in a graph.
- The `visited` array can be used to keep track of the visiting status of each course.