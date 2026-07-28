# Course Schedule (Topological Sort)

## Problem Statement
Given a number of courses and their prerequisites, determine if it is possible to finish all courses. The courses are represented by an array of pairs, where each pair contains two numbers: the course number and the prerequisite course number. If it is possible to finish all courses, return true; otherwise, return false. For example, if we have courses [[0, 1]] and [[1, 0]], it is impossible to finish all courses because course 0 requires course 1, and course 1 requires course 0. However, if we have courses [[1, 0]], we can finish all courses by taking course 0 first and then course 1.

## Approach
The approach to solve this problem is to use topological sort, which is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge u -> v, vertex u comes before v in the ordering. If a cycle is detected, it means we cannot finish all courses.

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
        // Create a graph using adjacency list representation
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses, 0);
        
        // Build the graph and calculate indegree
        for (const auto& prerequisite : prerequisites) {
            graph[prerequisite[1]].push_back(prerequisite[0]);
            indegree[prerequisite[0]]++;
        }
        
        // Initialize a queue with nodes having indegree 0
        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        // Initialize count of visited nodes
        int count = 0;
        
        // Perform topological sort
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            count++;
            
            // Decrease indegree of neighboring nodes
            for (const auto& neighbor : graph[node]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        // If all nodes are visited, it is possible to finish all courses
        return count == numCourses;
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
- If a cycle is detected, it means we cannot finish all courses.
- The time complexity of topological sort is O(n + m), where n is the number of nodes and m is the number of edges.