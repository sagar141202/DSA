# Tarjan's Algorithm (SCC)

## Problem Statement
Tarjan's algorithm is used to find Strongly Connected Components (SCCs) in a directed graph. A strongly connected component is a subgraph that has a path from every vertex to every other vertex. The problem statement is to find all SCCs in a given directed graph. The graph can have multiple edges between two vertices and self-loops. The graph is represented as an adjacency list. The algorithm should output the number of SCCs and the vertices in each SCC.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to find SCCs. It assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex. The algorithm then uses this information to identify the SCCs.

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
        int idx = 0;
        vector<bool> onStack(n, false);
        stack<int> stack;
        vector<vector<int>> sccs;

        for (int i = 0; i < n; i++) {
            if (index[i] == -1) {
                strongconnect(i, index, low, idx, onStack, stack, graph, sccs);
            }
        }

        return sccs;
    }

    void strongconnect(int v, vector<int>& index, vector<int>& low, int& idx, vector<bool>& onStack, stack<int>& stack, vector<vector<int>>& graph, vector<vector<int>>& sccs) {
        index[v] = low[v] = idx++;
        stack.push(v);
        onStack[v] = true;

        for (int w : graph[v]) {
            if (index[w] == -1) {
                strongconnect(w, index, low, idx, onStack, stack, graph, sccs);
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
    int n = 5;
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}};

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
Input: 
Graph:
0 -> 1
1 -> 0, 2
2 -> 1, 3
3 -> 2, 4
4 -> 3

Output: 
Number of SCCs: 1
SCC 1: 0 1 2 3 4
```

## Key Takeaways
- Tarjan's algorithm uses DFS to find SCCs in a directed graph.
- The algorithm assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex.
- The algorithm uses a stack to keep track of vertices that are currently being visited.