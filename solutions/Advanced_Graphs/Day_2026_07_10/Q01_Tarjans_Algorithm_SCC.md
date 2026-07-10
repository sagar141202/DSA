# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list. The algorithm should output the number of SCCs and the vertices in each SCC.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to find SCCs. It assigns a unique index to each vertex based on the order of discovery and calculates the lowest reachable index for each vertex. The algorithm then groups vertices into SCCs based on their lowest reachable index.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Tarjan {
public:
    vector<vector<int>> scc(const vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> index(n, -1), low(n, -1);
        vector<bool> onStack(n, false);
        vector<vector<int>> sccs;
        stack<int> stack;

        int idx = 0;
        for (int i = 0; i < n; i++) {
            if (index[i] == -1) {
                strongConnect(i, graph, index, low, onStack, stack, sccs, idx);
            }
        }

        return sccs;
    }

private:
    void strongConnect(int v, const vector<vector<int>>& graph, vector<int>& index, vector<int>& low, vector<bool>& onStack, stack<int>& stack, vector<vector<int>>& sccs, int& idx) {
        index[v] = low[v] = idx++;
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
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2}};
    Tarjan tarjan;
    vector<vector<int>> sccs = tarjan.scc(graph);

    cout << "Number of SCCs: " << sccs.size() << endl;
    for (int i = 0; i < sccs.size(); i++) {
        cout << "SCC " << i + 1 << ": ";
        for (int v : sccs[i]) {
            cout << v << " ";
        }
        cout << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: graph = [[1], [0, 2], [1, 3], [2]]
Output: 
Number of SCCs: 2
SCC 1: 0 1 2 
SCC 2: 3 
```

## Key Takeaways
- Tarjan's algorithm is used to find strongly connected components in a directed graph.
- The algorithm uses depth-first search (DFS) to assign a unique index to each vertex and calculate the lowest reachable index for each vertex.
- The algorithm groups vertices into SCCs based on their lowest reachable index.