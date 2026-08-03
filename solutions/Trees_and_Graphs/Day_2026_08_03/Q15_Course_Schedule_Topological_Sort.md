# Course Schedule (Topological Sort)

## Problem Statement
Given a number of courses and their prerequisites, determine if it is possible to finish all courses. The input is represented as a 2D array where each pair of elements represents a course and its prerequisite. For example, if `prerequisites[i] = [ai, bi]`, then course `bi` is a prerequisite of course `ai`. The function should return `true` if it is possible to finish all courses, otherwise return `false`. For instance, if we have `numCourses = 2` and `prerequisites = [[1,0]]`, the function should return `true` because we can take course 0 first and then course 1. However, if `numCourses = 2` and `prerequisites = [[1,0],[0,1]]`, the function should return `false` because there is a cycle in the graph and it's impossible to take both courses.

## Approach
The problem can be solved by using a topological sort algorithm, which orders the vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. We can use a depth-first search (DFS) or breadth-first search (BFS) to detect cycles in the graph. If a cycle is detected, it means that it's impossible to finish all courses.

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
        // Create an adjacency list representation of the graph
        vector<vector<int>> graph(numCourses);
        vector<int> visited(numCourses, 0);
        
        // Build the graph
        for (const auto& prerequisite : prerequisites) {
            graph[prerequisite[1]].push_back(prerequisite[0]);
        }
        
        // Perform DFS to detect cycles
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(graph, visited, i)) {
                return false;
            }
        }
        
        return true;
    }
    
    bool dfs(const vector<vector<int>>& graph, vector<int>& visited, int course) {
        // If the course is marked as visiting, it means we have a cycle
        if (visited[course] == -1) {
            return false;
        }
        
        // If the course is already visited, we don't need to visit it again
        if (visited[course] == 1) {
            return true;
        }
        
        // Mark the course as visiting
        visited[course] = -1;
        
        // Visit all the neighboring courses
        for (const auto& neighbor : graph[course]) {
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
- Topological sort is a useful algorithm for ordering vertices in a directed acyclic graph (DAG).
- Depth-first search (DFS) can be used to detect cycles in a graph.
- The problem can be solved by using a combination of graph representation, DFS, and cycle detection.