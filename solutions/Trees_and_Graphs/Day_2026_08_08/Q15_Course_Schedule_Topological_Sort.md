# Course Schedule (Topological Sort)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Given the number of courses and the array of prerequisites, return `true` if it is possible to finish all courses, and `false` otherwise. For example, if `numCourses = 2` and `prerequisites = [[1,0]]`, the function should return `true` because you can take course `0` first and then course `1`. However, if `numCourses = 2` and `prerequisites = [[1,0],[0,1]]`, the function should return `false` because there is a cycle in the graph.

## Approach
The approach to solve this problem is to use a topological sort algorithm. We create a graph using the given prerequisites and then check if the graph has any cycles. If the graph has a cycle, it is not possible to finish all courses.

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
        // Create a graph using the given prerequisites
        vector<vector<int>> graph(numCourses);
        vector<int> visited(numCourses, 0);
        
        // Build the graph
        for (const auto& prerequisite : prerequisites) {
            graph[prerequisite[1]].push_back(prerequisite[0]);
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
        // If the course is marked as visited and is in the current path, there is a cycle
        if (visited[course] == -1) {
            return false;
        }
        
        // If the course is already visited and not in the current path, return true
        if (visited[course] == 1) {
            return true;
        }
        
        // Mark the course as visited and in the current path
        visited[course] = -1;
        
        // Check all the prerequisites of the course
        for (const auto& neighbor : graph[course]) {
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
- Topological sort is used to order the vertices of a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering.
- The presence of a cycle in the graph indicates that it is not possible to finish all courses.
- Depth-first search (DFS) is used to detect cycles in the graph.