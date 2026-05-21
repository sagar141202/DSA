# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, where each vertex is associated with a list of its neighbors. The graph can have up to 10^5 vertices and 10^5 edges. The task is to identify all SCCs in the graph and print the vertices in each SCC.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to find SCCs. The algorithm assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex. The algorithm then uses this information to identify the SCCs.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> scc(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> index(n, -1), low(n, -1), stack(n), onStack(n);
    vector<vector<int>> result;
    int idx = 0, stackSize = 0;

    for (int i = 0; i < n; i++) {
        if (index[i] == -1) {
            strongConnect(i, graph, index, low, stack, onStack, result, idx, stackSize);
        }
    }

    return result;
}

void strongConnect(int v, vector<vector<int>>& graph, vector<int>& index, vector<int>& low, vector<int>& stack, vector<int>& onStack, vector<vector<int>>& result, int& idx, int& stackSize) {
    index[v] = low[v] = idx++;
    stack[stackSize] = v;
    onStack[v] = true;
    stackSize++;

    for (int w : graph[v]) {
        if (index[w] == -1) {
            strongConnect(w, graph, index, low, stack, onStack, result, idx, stackSize);
            low[v] = min(low[v], low[w]);
        } else if (onStack[w]) {
            low[v] = min(low[v], index[w]);
        }
    }

    if (low[v] == index[v]) {
        vector<int> component;
        while (true) {
            int w = stack[--stackSize];
            onStack[w] = false;
            component.push_back(w);
            if (w == v) break;
        }
        result.push_back(component);
    }
}

int main() {
    // example usage
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2}};
    vector<vector<int>> sccs = scc(graph);
    for (auto& scc : sccs) {
        for (int v : scc) {
            cout << v << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 
0 -> 1
1 -> 0, 2
2 -> 1, 3
3 -> 2
Output: 
0 1 
2 3 
```

## Key Takeaways
- Tarjan's algorithm is an efficient method for finding strongly connected components in a directed graph.
- The algorithm uses depth-first search and keeps track of the lowest reachable index for each vertex to identify the SCCs.
- The time complexity of the algorithm is O(V + E), where V is the number of vertices and E is the number of edges in the graph.