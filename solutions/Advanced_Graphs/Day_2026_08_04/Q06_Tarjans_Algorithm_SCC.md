# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, and the task is to identify all SCCs in the graph. For example, consider a graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1), (1, 2), (2, 0), (3, 4)}. The strongly connected components in this graph are {[0, 1, 2], [3, 4]}.

## Approach
Tarjan's algorithm uses a depth-first search (DFS) approach to find SCCs. It assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex. The algorithm iteratively finds the SCCs by identifying the vertices with the same lowest reachable index.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Tarjan {
public:
    vector<vector<int>> scc(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> index(n, -1);
        vector<int> low(n, -1);
        vector<int> stack;
        vector<bool> onStack(n, false);
        vector<vector<int>> sccs;
        int idx = 0;

        for (int i = 0; i < n; i++) {
            if (index[i] == -1) {
                strongConnect(i, graph, index, low, stack, onStack, sccs, idx);
            }
        }

        return sccs;
    }

    void strongConnect(int v, vector<vector<int>>& graph, vector<int>& index, vector<int>& low, vector<int>& stack, vector<bool>& onStack, vector<vector<int>>& sccs, int& idx) {
        index[v] = idx;
        low[v] = idx;
        idx++;
        stack.push_back(v);
        onStack[v] = true;

        for (int w : graph[v]) {
            if (index[w] == -1) {
                strongConnect(w, graph, index, low, stack, onStack, sccs, idx);
                low[v] = min(low[v], low[w]);
            } else if (onStack[w]) {
                low[v] = min(low[v], index[w]);
            }
        }

        if (low[v] == index[v]) {
            vector<int> scc;
            while (true) {
                int w = stack.back();
                stack.pop_back();
                onStack[w] = false;
                scc.push_back(w);
                if (w == v) break;
            }
            sccs.push_back(scc);
        }
    }
};

int main() {
    vector<vector<int>> graph = {{1}, {2}, {0}, {4}, {3}};
    Tarjan tarjan;
    vector<vector<int>> sccs = tarjan.scc(graph);
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
Input: [[1], [2], [0], [4], [3]]
Output: 
0 1 2 
3 4 
```

## Key Takeaways
- Tarjan's algorithm is an efficient approach for finding strongly connected components in a directed graph.
- The algorithm uses a depth-first search (DFS) approach and assigns a unique index to each vertex based on the order of visitation.
- The lowest reachable index for each vertex is used to identify the strongly connected components.