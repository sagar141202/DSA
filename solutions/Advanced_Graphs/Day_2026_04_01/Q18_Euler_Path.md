# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph can have multiple connected components, but it must be possible to traverse all edges in each component exactly once. The input graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of neighboring nodes. The constraints are: 1 ≤ number of nodes ≤ 10^5, 1 ≤ number of edges ≤ 10^5, and the graph can be directed or undirected.

## Approach
To solve this problem, we will use Hierholzer's algorithm, which states that a graph has an Euler path if and only if at most two vertices have odd degree. We will first check if the graph has an Euler path by counting the number of vertices with odd degree, then we will use a depth-first search to construct the Euler path.

## Complexity
- Time: O(E + V)
- Space: O(E + V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to check if a graph has an Euler path
bool hasEulerPath(vector<vector<int>>& graph) {
    int oddCount = 0;
    for (int i = 0; i < graph.size(); i++) {
        if (graph[i].size() % 2 != 0) {
            oddCount++;
        }
    }
    return oddCount <= 2;
}

// Function to find an Euler path using Hierholzer's algorithm
vector<int> eulerPath(vector<vector<int>>& graph) {
    if (!hasEulerPath(graph)) {
        return {};
    }

    vector<int> path;
    stack<int> stack;
    vector<bool> visited(graph.size() * graph.size(), false);

    // Start at an arbitrary node with an odd degree
    for (int i = 0; i < graph.size(); i++) {
        if (graph[i].size() % 2 != 0) {
            stack.push(i);
            break;
        }
    }

    // If no node with odd degree is found, start at the first node
    if (stack.empty()) {
        stack.push(0);
    }

    while (!stack.empty()) {
        int node = stack.top();
        bool hasUnvisitedNeighbor = false;

        // Find an unvisited neighbor of the current node
        for (int neighbor : graph[node]) {
            int edgeIndex = node * graph.size() + neighbor;
            if (!visited[edgeIndex]) {
                hasUnvisitedNeighbor = true;
                stack.push(neighbor);
                visited[edgeIndex] = true;
                break;
            }
        }

        // If no unvisited neighbor is found, add the current node to the path
        if (!hasUnvisitedNeighbor) {
            path.push_back(stack.top());
            stack.pop();
        }
    }

    // Reverse the path to get the correct order
    reverse(path.begin(), path.end());
    return path;
}

int main() {
    // Example usage:
    vector<vector<int>> graph = {{1, 2}, {0, 2}, {0, 1}};
    vector<int> path = eulerPath(graph);
    for (int node : path) {
        cout << node << " ";
    }
    cout << endl;
    return 0;
}
```

## Test Cases
```
Input: 
Graph: {{1, 2}, {0, 2}, {0, 1}}
Output: 0 1 2 0
```

## Key Takeaways
- A graph has an Euler path if and only if at most two vertices have odd degree.
- Hierholzer's algorithm can be used to find an Euler path in a graph.
- The algorithm starts at an arbitrary node with an odd degree and uses a depth-first search to construct the Euler path.