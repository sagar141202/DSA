# Course Schedule (Topological Sort)

## Problem Statement
Given a number of courses and their prerequisites, determine if it is possible to finish all courses. The courses are represented by an array of pairs, where each pair contains two integers representing a course and its prerequisite. For example, if the input is `[[0, 1], [0, 2], [1, 2], [2, 3]]`, then course 0 has prerequisites 1 and 2, and course 1 has prerequisite 2. The goal is to find out if there is a valid order in which all courses can be taken. If there is a cycle in the graph, then it is not possible to finish all courses.

## Approach
The problem can be solved using a topological sort, which is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge u -> v, vertex u comes before v in the ordering. We will use a depth-first search (DFS) algorithm to detect cycles in the graph. If a cycle is detected, then it is not possible to finish all courses.

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
        vector<int> visited(numCourses, 0);
        
        // Build the graph
        for (auto& pair : prerequisites) {
            graph[pair[1]].push_back(pair[0]);
        }
        
        // Perform DFS to detect cycles
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(graph, visited, i)) {
                return false;
            }
        }
        
        return true;
    }
    
    bool dfs(vector<vector<int>>& graph, vector<int>& visited, int node) {
        // If the node is being visited, then a cycle is detected
        if (visited[node] == -1) {
            return false;
        }
        
        // If the node has been visited, then return true
        if (visited[node] == 1) {
            return true;
        }
        
        // Mark the node as being visited
        visited[node] = -1;
        
        // Visit all neighbors of the node
        for (int neighbor : graph[node]) {
            if (!dfs(graph, visited, neighbor)) {
                return false;
            }
        }
        
        // Mark the node as visited
        visited[node] = 1;
        
        return true;
    }
};

int main() {
    Solution solution;
    vector<vector<int>> prerequisites = {{1, 0}};
    int numCourses = 2;
    cout << solution.canFinish(numCourses, prerequisites) << endl;  // Output: 1
    return 0;
}
```

## Test Cases
```
Input: numCourses = 2, prerequisites = [[1, 0]]
Output: true
Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
Output: false
```

## Key Takeaways
- Use topological sort to determine if it is possible to finish all courses.
- Use DFS to detect cycles in the graph.
- If a cycle is detected, then it is not possible to finish all courses.