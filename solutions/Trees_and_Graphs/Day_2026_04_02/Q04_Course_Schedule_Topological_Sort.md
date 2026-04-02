# Course Schedule (Topological Sort)

## Problem Statement
Given the number of courses `numCourses` and an array of prerequisites `prerequisites` where `prerequisites[i] = [ai, bi]` means that you must take course `bi` before taking course `ai`, determine if it is possible to finish all courses. If it is possible, return a valid course schedule. If it is not possible, return an empty array. The input array will not contain duplicate pairs and `1 <= numCourses <= 1000`.

## Approach
The problem can be solved using a topological sort algorithm, which is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. The algorithm works by first building a graph from the given prerequisites, then using a depth-first search (DFS) or breadth-first search (BFS) to perform the topological sort.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // Create an adjacency list representation of the graph
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses, 0);
        
        // Build the graph and calculate the indegree of each node
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
        
        // Initialize the result vector
        vector<int> result;
        
        // Perform topological sort using BFS
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            result.push_back(node);
            
            // Decrease the indegree of all neighbors of the current node
            for (int neighbor : graph[node]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        // If the result vector contains all courses, return it; otherwise, return an empty vector
        if (result.size() == numCourses) {
            return result;
        } else {
            return {};
        }
    }
};
```

## Test Cases
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3]
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2],[4,3],[4,2]]
Output: [0,2,1,3,4]
```

## Key Takeaways
- Topological sort can be used to solve course scheduling problems.
- The algorithm works by building a graph from the given prerequisites and then using a DFS or BFS to perform the topological sort.
- The result is a valid course schedule if the topological sort is possible; otherwise, it is not possible to finish all courses.