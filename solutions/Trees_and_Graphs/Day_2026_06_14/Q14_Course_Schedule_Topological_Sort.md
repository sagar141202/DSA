# Course Schedule (Topological Sort)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Given the number of courses and the array of prerequisites, return whether it is possible to finish all courses. If it is possible, return an array representing one possible order in which the courses can be taken. The input array `prerequisites` is guaranteed to be non-empty, and each pair of elements in `prerequisites` represents a prerequisite relationship.

## Approach
This problem can be solved using topological sort, which is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. We can use a graph to represent the courses and their prerequisites, and then perform a topological sort on the graph to find a valid order in which the courses can be taken.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
    vector<int> res;
    vector<int> visited(numCourses, 0);
    vector<vector<int>> graph(numCourses);
    
    // build the graph
    for (auto& p : prerequisites) {
        graph[p[1]].push_back(p[0]);
    }
    
    // perform topological sort using DFS
    for (int i = 0; i < numCourses; i++) {
        if (!visited[i] && !dfs(i, graph, visited, res)) {
            return {};
        }
    }
    
    return res;
}

bool dfs(int node, vector<vector<int>>& graph, vector<int>& visited, vector<int>& res) {
    if (visited[node] == -1) {
        return false; // cycle detected
    }
    if (visited[node] == 1) {
        return true; // already visited
    }
    
    visited[node] = -1; // mark as visiting
    for (int neighbor : graph[node]) {
        if (!dfs(neighbor, graph, visited, res)) {
            return false;
        }
    }
    visited[node] = 1; // mark as visited
    res.push_back(node);
    return true;
}
```

## Test Cases
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3]
```

## Key Takeaways
- Topological sort can be used to solve problems involving ordering of vertices in a directed acyclic graph (DAG).
- The `visited` array can be used to keep track of the visiting status of each node, where `0` represents not visited, `1` represents visited, and `-1` represents visiting.
- The `dfs` function can be used to perform a depth-first search on the graph, and it returns `false` if a cycle is detected.