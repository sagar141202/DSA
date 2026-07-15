# Course Schedule (Topological Sort)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from 0 to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Given the number of courses and the array of prerequisites, return whether it's possible to finish all courses. For example, if `numCourses = 2` and `prerequisites = [[1,0]]`, the output should be `true` because you can take the courses in the order [0, 1]. However, if `numCourses = 2` and `prerequisites = [[1,0],[0,1]]`, the output should be `false` because there is a cycle and you cannot finish all courses.

## Approach
We will use a topological sort algorithm to solve this problem. The idea is to create a graph from the given prerequisites and then check if the graph contains a cycle. If the graph contains a cycle, it's impossible to finish all courses.

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
        for (const auto& prerequisite : prerequisites) {
            int course = prerequisite[0];
            int prerequisiteCourse = prerequisite[1];
            graph[prerequisiteCourse].push_back(course);
            indegree[course]++;
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
            for (int neighbor : graph[node]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        // If all nodes are visited, it's possible to finish all courses
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
- The indegree of a node represents the number of edges pointing to it.
- A node with an indegree of 0 can be safely removed from the graph without introducing any cycles.