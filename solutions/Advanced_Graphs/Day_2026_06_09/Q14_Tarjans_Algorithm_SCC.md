# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, and the function should return a list of lists, where each inner list contains the vertices of an SCC. The graph can have up to 10^5 vertices and 10^5 edges.

## Approach
Tarjan's algorithm uses depth-first search to find SCCs. It assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex. The algorithm then groups vertices into SCCs based on their lowest reachable indices.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void tarjan(vector<vector<int>>& graph, int vertex, vector<int>& index, vector<int>& low, vector<bool>& onStack, stack<int>& s, vector<vector<int>>& sccs, int& time) {
    index[vertex] = low[vertex] = time++;
    s.push(vertex);
    onStack[vertex] = true;

    for (int neighbor : graph[vertex]) {
        if (index[neighbor] == -1) {
            tarjan(graph, neighbor, index, low, onStack, s, sccs, time);
            low[vertex] = min(low[vertex], low[neighbor]);
        } else if (onStack[neighbor]) {
            low[vertex] = min(low[vertex], index[neighbor]);
        }
    }

    if (low[vertex] == index[vertex]) {
        vector<int> scc;
        while (true) {
            int w = s.top();
            s.pop();
            onStack[w] = false;
            scc.push_back(w);
            if (w == vertex) break;
        }
        sccs.push_back(scc);
    }
}

vector<vector<int>> findSCCs(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> index(n, -1);
    vector<int> low(n, -1);
    vector<bool> onStack(n, false);
    stack<int> s;
    vector<vector<int>> sccs;
    int time = 0;

    for (int i = 0; i < n; i++) {
        if (index[i] == -1) {
            tarjan(graph, i, index, low, onStack, s, sccs, time);
        }
    }
    return sccs;
}

int main() {
    int n = 5;
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}};
    vector<vector<int>> sccs = findSCCs(graph);
    for (auto& scc : sccs) {
        for (int vertex : scc) {
            cout << vertex << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 vertices and edges: (0, 1), (1, 0), (1, 2), (2, 1), (2, 3), (3, 2), (3, 4), (4, 3)
Output: 
0 1 2 3 4
```

## Key Takeaways
- Tarjan's algorithm is used to find strongly connected components in a directed graph.
- It uses depth-first search to assign a unique index to each vertex based on the order of visitation.
- The algorithm keeps track of the lowest reachable index for each vertex to group vertices into SCCs.