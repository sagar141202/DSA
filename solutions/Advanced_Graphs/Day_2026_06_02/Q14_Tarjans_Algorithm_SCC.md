# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, and the function should return a list of lists, where each inner list contains the vertices in an SCC.

## Approach
Tarjan's algorithm uses depth-first search to find SCCs by maintaining a stack of vertices and a low-link value for each vertex. The algorithm iterates through the graph, assigning a unique index and low-link value to each vertex, and uses these values to identify SCCs. The low-link value represents the smallest index reachable from a vertex.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Tarjan {
public:
    vector<vector<int>> tarjanSCC(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> index(n, -1), low(n, -1);
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
    Tarjan tarjan;
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2}};
    vector<vector<int>> sccs = tarjan.tarjanSCC(graph);
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
Graph: 
0 -> 1
1 -> 0, 2
2 -> 1, 3
3 -> 2
Output: 
0 1 
2 3 
```

## Key Takeaways
- Tarjan's algorithm is used to find strongly connected components in a directed graph.
- The algorithm uses a stack to keep track of vertices and a low-link value to identify SCCs.
- The time complexity of Tarjan's algorithm is O(V + E), where V is the number of vertices and E is the number of edges.