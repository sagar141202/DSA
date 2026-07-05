# Course Schedule (Topological Sort)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Given the number of courses and the array of prerequisites, return `true` if it is possible to finish all courses, and `false` otherwise. For example, if `numCourses = 2` and `prerequisites = [[1,0]]`, the output should be `true` because you can take course `0` first and then course `1`. However, if `numCourses = 2` and `prerequisites = [[1,0],[0,1]]`, the output should be `false` because you cannot take both courses.

## Approach
This problem can be solved using a topological sort algorithm, which is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. We will use a graph to represent the courses and their prerequisites, and then perform a topological sort to check if it is possible to finish all courses.

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
        // Create a graph to represent the courses and their prerequisites
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses, 0);
        
        // Build the graph and calculate the indegree of each node
        for (const auto& prerequisite : prerequisites) {
            graph[prerequisite[1]].push_back(prerequisite[0]);
            indegree[prerequisite[0]]++;
        }
        
        // Initialize a queue with nodes that have an indegree of 0
        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        // Perform a topological sort
        int count = 0;
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            count++;
            
            // Decrease the indegree of all nodes that are adjacent to the current node
            for (int neighbor : graph[node]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        // If all nodes have been visited, it is possible to finish all courses
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
- Topological sort can be used to solve problems that involve ordering nodes in a directed acyclic graph (DAG).
- The indegree of a node represents the number of edges that point to it, and nodes with an indegree of 0 can be used as starting points for a topological sort.
- If a cycle is detected during the topological sort, it is not possible to finish all courses.