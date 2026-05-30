# Course Schedule (Topological Sort)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return `true` if you can finish all courses, and `false` otherwise. For example, if `numCourses = 2` and `prerequisites = [[1,0]]`, then the output is `true` because you can take course `0` first and then take course `1`. However, if `numCourses = 2` and `prerequisites = [[1,0],[0,1]]`, then the output is `false` because you cannot take both courses.

## Approach
The problem can be solved using a topological sort algorithm. We create a graph from the given prerequisites and then check for cycles in the graph. If a cycle is detected, it means we cannot finish all courses.

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
        // Create a graph from the given prerequisites
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses, 0);
        
        // Build the graph and calculate indegree
        for (auto& edge : prerequisites) {
            int u = edge[0];
            int v = edge[1];
            graph[v].push_back(u);
            indegree[u]++;
        }
        
        // Initialize a queue with nodes having indegree 0
        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        // Perform topological sort
        int count = 0;
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            count++;
            
            for (int neighbor : graph[node]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        // If all nodes are visited, then we can finish all courses
        return count == numCourses;
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
- We can use topological sort to detect cycles in a directed graph.
- The problem can be represented as a graph where each course is a node and the prerequisites are directed edges.
- If a cycle is detected in the graph, it means we cannot finish all courses.