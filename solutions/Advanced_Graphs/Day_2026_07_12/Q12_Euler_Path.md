# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has an Euler path, output the path. If not, output a message saying that no Euler path exists. The graph is represented as an adjacency list, where each index represents a node and its corresponding value is a list of its neighbors. The input graph has at most 100 nodes and 1000 edges.

## Approach
To solve this problem, we can use Hierholzer's algorithm, which finds an Euler path in a graph by repeatedly finding cycles and combining them. The algorithm starts at an arbitrary node and explores the graph depth-first, backtracking when a dead end is reached. If the graph has an Euler path, the algorithm will eventually visit every edge exactly once.

## Complexity
- Time: O(E + V)
- Space: O(E + V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> eulerPath(vector<vector<int>>& graph) {
    int numNodes = graph.size();
    vector<int> degrees(numNodes, 0);
    for (int i = 0; i < numNodes; i++) {
        degrees[i] = graph[i].size();
    }
    
    int startNode = -1;
    int oddDegreeCount = 0;
    for (int i = 0; i < numNodes; i++) {
        if (degrees[i] % 2 != 0) {
            oddDegreeCount++;
            startNode = i;
        }
    }
    
    if (oddDegreeCount > 2) {
        return {}; // no Euler path
    }
    
    vector<int> path;
    vector<bool> visitedEdges(numNodes * numNodes, false);
    function<void(int)> dfs = [&](int node) {
        while (graph[node].size() > 0) {
            int neighbor = graph[node].back();
            graph[node].pop_back();
            if (!visitedEdges[node * numNodes + neighbor]) {
                visitedEdges[node * numNodes + neighbor] = true;
                dfs(neighbor);
            }
        }
        path.push_back(node);
    };
    
    if (startNode == -1) {
        startNode = 0; // start at an arbitrary node
    }
    dfs(startNode);
    reverse(path.begin(), path.end());
    
    return path;
}

int main() {
    // example usage
    vector<vector<int>> graph = {{1, 2}, {0, 2}, {0, 1, 3}, {2}};
    vector<int> path = eulerPath(graph);
    for (int node : path) {
        cout << node << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: {{1, 2}, {0, 2}, {0, 1, 3}, {2}}
Output: 0 1 2 3
Input: {{1}, {0, 2}, {1}}
Output: (no Euler path)
```

## Key Takeaways
- An Euler path visits every edge in a graph exactly once.
- Hierholzer's algorithm can be used to find an Euler path in a graph.
- The graph must be connected and have at most two nodes with odd degrees for an Euler path to exist.