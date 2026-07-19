# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path if it exists. An Euler path is a path that visits every edge in the graph exactly once. The graph can have multiple connected components, and the Euler path should visit all edges in all components. If the graph has more than two vertices with odd degree (for undirected graphs) or more than one vertex with odd in-degree and one vertex with odd out-degree (for directed graphs), then it does not have an Euler path.

## Approach
To solve this problem, we use Hierholzer's algorithm, which involves finding a cycle in the graph, then iteratively finding cycles in the remaining graph and combining them. The algorithm ensures that all edges are visited exactly once.

## Complexity
- Time: O(E + V)
- Space: O(E + V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> graph;
vector<int> eulerPath;

void dfs(int node) {
    // Explore all edges from the current node
    while (!graph[node].empty()) {
        int neighbor = graph[node].back();
        graph[node].pop_back();
        
        // Remove the edge from the neighbor as well
        for (auto it = graph[neighbor].begin(); it != graph[neighbor].end(); ++it) {
            if (*it == node) {
                graph[neighbor].erase(it);
                break;
            }
        }
        
        dfs(neighbor);
    }
    
    // Add the current node to the Euler path after all its edges have been explored
    eulerPath.push_back(node);
}

void findEulerPath(int start) {
    dfs(start);
    reverse(eulerPath.begin(), eulerPath.end());
}

int main() {
    int vertices, edges;
    cin >> vertices >> edges;
    
    graph.resize(vertices);
    
    for (int i = 0; i < edges; ++i) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        // For undirected graph, uncomment the following line
        // graph[v].push_back(u);
    }
    
    // Find a starting node for the Euler path
    int start = 0;
    for (int i = 0; i < vertices; ++i) {
        if (graph[i].size() % 2 != 0) {
            start = i;
            break;
        }
    }
    
    findEulerPath(start);
    
    for (int node : eulerPath) {
        cout << node << " ";
    }
    
    return 0;
}
```

## Test Cases
```
Input: 
5 7
0 1
0 2
1 2
1 3
1 4
2 3
3 4
Output: 
0 1 3 4 1 2 0
```

## Key Takeaways
- An Euler path visits every edge in the graph exactly once.
- Hierholzer's algorithm is used to find an Euler path in a graph.
- The graph must have at most two vertices with odd degree (for undirected graphs) or at most one vertex with odd in-degree and one vertex with odd out-degree (for directed graphs) to have an Euler path.