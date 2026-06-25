# Course Schedule (Topological Sort)

## Problem Statement
Given a number of courses (`numCourses`) and a list of prerequisites (`prerequisites`) where `prerequisites[i] = [ai, bi]`, which means you must take course `ai` before course `bi`, determine if it is possible to finish all courses. If it is possible, return a valid course schedule, otherwise return an empty array. There are no duplicate edges and no self-loops in the graph.

## Approach
The problem can be solved using Topological Sort, which is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. We will create a graph from the given prerequisites and then perform a topological sort to find a valid course schedule.

## Complexity
- Time: O(N + M)
- Space: O(N + M)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // Create a graph from the given prerequisites
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses, 0);
        for (auto& edge : prerequisites) {
            graph[edge[1]].push_back(edge[0]);
            indegree[edge[0]]++;
        }

        // Initialize a queue with nodes having no incoming edges
        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        // Perform topological sort
        vector<int> schedule;
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            schedule.push_back(node);
            for (int neighbor : graph[node]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }

        // If all courses are not included in the schedule, return an empty array
        if (schedule.size() != numCourses) {
            return {};
        }

        return schedule;
    }
};
```

## Test Cases
```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3]
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2],[4,3]]
Output: [0,1,2,3,4]
```

## Key Takeaways
- Topological sort is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering.
- The given problem can be modeled as a graph where each course is a node, and the prerequisites are the directed edges between the nodes.
- The Kahn's algorithm is used to perform the topological sort, which involves finding nodes with no incoming edges and then removing them from the graph.