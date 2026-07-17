# Course Schedule (Topological Sort)

## Problem Statement
Given a number of courses and prerequisites, determine if it's possible to take all courses. The courses are represented by an array of pairs, where the first element in the pair is the course and the second element is the prerequisite. If it's possible to take all courses, return true; otherwise, return false. For example, if we have courses [[0, 1]] and [[1, 0]], it's impossible to take both courses because they depend on each other. However, for courses [[1, 0]] and [[2, 0]], it's possible to take all courses.

## Approach
We can use topological sort to solve this problem by creating a graph and checking for cycles. If a cycle exists, it's impossible to take all courses. We create an adjacency list to represent the graph and then use DFS to detect cycles.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> graph;
vector<int> visited;

bool dfs(int i) {
    // If the node is being visited, it means a cycle is present
    if (visited[i] == -1) return false;
    // If the node has been visited, return true
    if (visited[i] == 1) return true;
    // Mark the node as being visited
    visited[i] = -1;
    for (int neighbor : graph[i]) {
        if (!dfs(neighbor)) return false;
    }
    // Mark the node as visited
    visited[i] = 1;
    return true;
}

bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
    graph.resize(numCourses);
    visited.resize(numCourses, 0);
    for (auto& p : prerequisites) {
        graph[p[1]].push_back(p[0]);
    }
    for (int i = 0; i < numCourses; i++) {
        if (!dfs(i)) return false;
    }
    return true;
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
- Topological sort can be used to detect cycles in a graph.
- DFS is an efficient way to perform topological sort.
- If a cycle exists in the graph, it's impossible to take all courses.