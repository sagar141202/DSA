# Course Schedule (Topological Sort)

## Problem Statement
Given a number of courses (`numCourses`) and a list of prerequisite pairs (`prerequisites`), determine if it is possible to finish all courses. Each prerequisite pair is represented as an array where the first element is the course and the second element is the prerequisite. For example, if `prerequisites[i] = [a, b]`, then course `a` must be taken after course `b`. The function should return `true` if it is possible to finish all courses and `false` otherwise. The constraints are: `1 <= numCourses <= 1000`, `0 <= prerequisites.length <= 10000`, and `0 <= prerequisites[i][0], prerequisites[i][1] < numCourses`.

## Approach
The problem can be solved using a topological sort, which is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. The algorithm works by first building a graph from the given prerequisites, then using a depth-first search (DFS) to detect any cycles in the graph. If a cycle is detected, it is not possible to finish all courses.

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
        // Create a graph from the prerequisites
        vector<vector<int>> graph(numCourses);
        vector<int> visited(numCourses, 0);
        for (const auto& pair : prerequisites) {
            graph[pair[1]].push_back(pair[0]);
        }

        // Use DFS to detect any cycles in the graph
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(graph, visited, i)) {
                return false;
            }
        }
        return true;
    }

    bool dfs(vector<vector<int>>& graph, vector<int>& visited, int course) {
        // If the course is currently being visited, there is a cycle
        if (visited[course] == -1) {
            return false;
        }
        // If the course has already been visited, return true
        if (visited[course] == 1) {
            return true;
        }
        // Mark the course as being visited
        visited[course] = -1;
        // Visit all the prerequisites of the course
        for (int nextCourse : graph[course]) {
            if (!dfs(graph, visited, nextCourse)) {
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
- Topological sort can be used to solve problems involving dependencies between items.
- DFS can be used to detect cycles in a graph.
- The visited array can be used to keep track of the state of each node in the graph.