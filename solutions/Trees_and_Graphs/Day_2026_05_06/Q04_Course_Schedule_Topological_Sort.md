# Course Schedule (Topological Sort)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from 0 to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return `true` if you can finish all courses, and `false` otherwise. For example, given `numCourses = 2` and `prerequisites = [[1,0]]`, the output is `true` because you can take course 0 first and then course 1. However, given `numCourses = 2` and `prerequisites = [[1,0],[0,1]]`, the output is `false` because you cannot take both courses.

## Approach
We will use a topological sort to solve this problem, which is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. If a cycle is detected, we return `false`. Otherwise, we return `true`.

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
        // Create an adjacency list
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses, 0);
        
        // Build the graph and calculate indegrees
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
        
        // If all nodes are visited, then there is no cycle
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
- Topological sort is used to detect cycles in a directed graph.
- If a cycle is detected, it is not possible to finish all courses.
- The time complexity of the solution is O(N + M), where N is the number of courses and M is the number of prerequisites.