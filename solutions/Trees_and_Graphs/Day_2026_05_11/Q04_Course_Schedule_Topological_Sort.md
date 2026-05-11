# Course Schedule (Topological Sort)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return `true` if you can finish all courses, and `false` otherwise. For example, if `numCourses = 2` and `prerequisites = [[1,0]]`, then you can finish all courses because you can take course `0` first and then course `1`. However, if `numCourses = 2` and `prerequisites = [[1,0],[0,1]]`, then you cannot finish all courses because you will be stuck in an infinite loop.

## Approach
We can solve this problem using a topological sort algorithm, which orders the nodes in a directed acyclic graph (DAG) such that for every edge (u,v), node u comes before v in the ordering. If we can perform a topological sort on the graph, then we can finish all courses. Otherwise, there is a cycle in the graph and we cannot finish all courses.

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
        // Create an adjacency list to represent the graph
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses, 0);
        
        // Build the graph and calculate the indegree of each node
        for (auto& edge : prerequisites) {
            graph[edge[1]].push_back(edge[0]);
            indegree[edge[0]]++;
        }
        
        // Initialize a queue with all nodes that have an indegree of 0
        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        // Initialize a counter to keep track of the number of visited nodes
        int count = 0;
        
        // Perform a topological sort using BFS
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            count++;
            
            // Decrease the indegree of all neighbors of the current node
            for (int neighbor : graph[node]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        // If we have visited all nodes, then we can finish all courses
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
- Topological sort can be used to detect cycles in a directed graph.
- The indegree of a node is the number of edges that point to it.
- A node with an indegree of 0 can be safely removed from the graph without affecting the existence of a topological sort.