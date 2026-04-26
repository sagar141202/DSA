# Course Schedule (Topological Sort)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from 0 to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return `true` if you can finish all courses, otherwise return `false`. For example, if `numCourses = 2` and `prerequisites = [[1,0]]`, you can take course 0 first and then course 1, so the function should return `true`. However, if `numCourses = 2` and `prerequisites = [[1,0],[0,1]]`, you cannot take any course because each course is a prerequisite of the other, so the function should return `false`.

## Approach
This problem can be solved using a topological sort algorithm, which is a linear ordering of vertices in a directed acyclic graph (DAG). We can represent the courses as vertices and the prerequisites as directed edges. If a topological sort exists, it means we can finish all courses.

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
        // Create adjacency list
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses, 0);
        
        // Build the graph and calculate indegree
        for (auto& course : prerequisites) {
            graph[course[1]].push_back(course[0]);
            indegree[course[0]]++;
        }
        
        // Initialize queue with nodes having indegree 0
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
            
            // Decrease indegree of neighboring nodes
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
- Topological sort can be used to solve problems involving directed acyclic graphs (DAGs).
- Indegree of a node can be used to identify nodes with no incoming edges, which can be used as starting points for the topological sort.
- If a topological sort exists for a given graph, it means that there are no cycles in the graph.