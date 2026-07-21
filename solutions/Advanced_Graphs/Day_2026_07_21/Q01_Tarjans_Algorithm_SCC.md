# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its neighbors. The algorithm should output the number of SCCs and the vertices in each SCC.

## Approach
Tarjan's algorithm is used to find SCCs in a directed graph. It works by performing a depth-first search (DFS) on the graph and keeping track of the discovery time and low value of each vertex. The low value of a vertex is the smallest discovery time of any vertex that is reachable from it. If the low value of a vertex is equal to its discovery time, then it is the root of an SCC.

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
        vector<int> disc(n, -1);
        vector<int> low(n, -1);
        vector<bool> onStack(n, false);
        stack<int> st;
        vector<vector<int>> sccs;
        int time = 0;

        for (int i = 0; i < n; i++) {
            if (disc[i] == -1) {
                dfs(i, graph, disc, low, onStack, st, sccs, time);
            }
        }

        return sccs;
    }

    void dfs(int u, vector<vector<int>>& graph, vector<int>& disc, vector<int>& low, vector<bool>& onStack, stack<int>& st, vector<vector<int>>& sccs, int& time) {
        disc[u] = low[u] = time++;
        st.push(u);
        onStack[u] = true;

        for (int v : graph[u]) {
            if (disc[v] == -1) {
                dfs(v, graph, disc, low, onStack, st, sccs, time);
                low[u] = min(low[u], low[v]);
            } else if (onStack[v]) {
                low[u] = min(low[u], disc[v]);
            }
        }

        if (low[u] == disc[u]) {
            vector<int> scc;
            while (true) {
                int v = st.top();
                st.pop();
                onStack[v] = false;
                scc.push_back(v);
                if (v == u) break;
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
        for (int u : sccs[i]) {
            cout << u << " ";
        }
        cout << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 vertices and the following edges:
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
- Tarjan's algorithm uses a depth-first search (DFS) to find strongly connected components in a directed graph.
- The algorithm keeps track of the discovery time and low value of each vertex to determine the root of each SCC.
- The time complexity of Tarjan's algorithm is O(V + E), where V is the number of vertices and E is the number of edges.