# Course Schedule (Topological Sort)

## Problem Statement
Given a number of courses and their prerequisites, determine if it's possible to take all courses. The courses are represented by an array of pairs, where each pair contains two values: the course and its prerequisite. For example, `[1, 0]` means course 1 has a prerequisite of course 0. If it's possible to take all courses, return `true`; otherwise, return `false`. There are `numCourses` courses in total, labeled from 0 to `numCourses - 1`. 

## Approach
This problem can be solved using a topological sort, which is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. The algorithm works by detecting cycles in the graph and returning `false` if a cycle is found, indicating it's impossible to take all courses.

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
        // Create a graph and initialize the indegree of each node
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses, 0);
        
        // Build the graph and update the indegree
        for (const auto& prerequisite : prerequisites) {
            graph[prerequisite[1]].push_back(prerequisite[0]);
            indegree[prerequisite[0]]++;
        }
        
        // Initialize a queue with nodes having an indegree of 0
        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        // Initialize the count of visited nodes
        int count = 0;
        
        // Perform topological sort
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            count++;
            
            // Decrease the indegree of neighboring nodes
            for (const auto& neighbor : graph[node]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        // If all nodes are visited, it's possible to take all courses
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
- Topological sort is used to detect cycles in a directed graph.
- If a cycle is detected, it's impossible to take all courses.
- The algorithm works by maintaining the indegree of each node and performing a BFS traversal.