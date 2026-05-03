# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) using Tarjan's algorithm. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, and the algorithm should output all SCCs. For example, given a graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1), (1, 2), (2, 0), (1, 3), (3, 4)}, the output should be {[0, 1, 2], [3, 4]}.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to traverse the graph and identify SCCs. It maintains a stack of vertices and assigns a unique index to each vertex based on the order it is visited. The algorithm then uses the low-link value to determine if a vertex is part of an SCC.

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
        vector<bool> onStack(n, false);
        stack<int> stack;
        vector<vector<int>> sccs;
        int idx = 0;

        for (int i = 0; i < n; i++) {
            if (index[i] == -1) {
                strongConnect(i, graph, index, low, onStack, stack, sccs, idx);
            }
        }

        return sccs;
    }

    void strongConnect(int v, vector<vector<int>>& graph, vector<int>& index, vector<int>& low, vector<bool>& onStack, stack<int>& stack, vector<vector<int>>& sccs, int& idx) {
        index[v] = idx;
        low[v] = idx;
        idx++;
        stack.push(v);
        onStack[v] = true;

        for (int w : graph[v]) {
            if (index[w] == -1) {
                strongConnect(w, graph, index, low, onStack, stack, sccs, idx);
                low[v] = min(low[v], low[w]);
            } else if (onStack[w]) {
                low[v] = min(low[v], index[w]);
            }
        }

        if (low[v] == index[v]) {
            vector<int> scc;
            while (true) {
                int w = stack.top();
                stack.pop();
                onStack[w] = false;
                scc.push_back(w);
                if (w == v) break;
            }
            sccs.push_back(scc);
        }
    }
};

int main() {
    vector<vector<int>> graph = {{1}, {2, 3}, {0}, {4}, {}};
    Tarjan tarjan;
    vector<vector<int>> sccs = tarjan.scc(graph);

    for (auto scc : sccs) {
        cout << "{";
        for (int i = 0; i < scc.size(); i++) {
            cout << scc[i];
            if (i < scc.size() - 1) cout << ", ";
        }
        cout << "} ";
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1), (1, 2), (2, 0), (1, 3), (3, 4)}
Output: 
{0, 1, 2} {3, 4}
```

## Key Takeaways
- Tarjan's algorithm is an efficient method for finding strongly connected components in a directed graph.
- The algorithm uses a depth-first search approach with a stack to keep track of vertices.
- The low-link value is used to determine if a vertex is part of an SCC.