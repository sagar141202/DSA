# Tarjan's Algorithm (SCC)

## Problem Statement
Tarjan's Algorithm is used to find Strongly Connected Components (SCCs) in a directed graph. A Strongly Connected Component is a subgraph where there is a path from every vertex to every other vertex. The algorithm works by performing a depth-first search on the graph and keeping track of the discovery time and low value of each vertex. The goal is to identify all SCCs in the graph. For example, given a graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1), (1, 2), (2, 0), (3, 4)}, the algorithm should output two SCCs: {0, 1, 2} and {3, 4}.

## Approach
The algorithm uses a depth-first search to traverse the graph, keeping track of the discovery time and low value of each vertex. The low value of a vertex is the smallest discovery time of any vertex that is reachable from it. When a vertex is visited, its low value is updated if a smaller discovery time is found. If the low value of a vertex is equal to its discovery time, it is the root of a new SCC.

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
        vector<int> stack;
        vector<bool> onStack(n, false);
        vector<vector<int>> sccs;
        int time = 0;

        for (int i = 0; i < n; i++) {
            if (disc[i] == -1) {
                dfs(i, graph, disc, low, stack, onStack, sccs, time);
            }
        }

        return sccs;
    }

    void dfs(int u, vector<vector<int>>& graph, vector<int>& disc, vector<int>& low, vector<int>& stack, vector<bool>& onStack, vector<vector<int>>& sccs, int& time) {
        disc[u] = low[u] = time++;
        stack.push_back(u);
        onStack[u] = true;

        for (int v : graph[u]) {
            if (disc[v] == -1) {
                dfs(v, graph, disc, low, stack, onStack, sccs, time);
                low[u] = min(low[u], low[v]);
            } else if (onStack[v]) {
                low[u] = min(low[u], disc[v]);
            }
        }

        if (low[u] == disc[u]) {
            vector<int> scc;
            while (true) {
                int v = stack.back();
                stack.pop_back();
                onStack[v] = false;
                scc.push_back(v);
                if (v == u) break;
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
Graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1), (1, 2), (2, 0), (3, 4)}
Output: 
0 1 2 
3 4 
```

## Key Takeaways
- Tarjan's Algorithm uses depth-first search to find SCCs in a directed graph.
- The algorithm keeps track of the discovery time and low value of each vertex to identify SCCs.
- The time complexity of the algorithm is O(V + E), where V is the number of vertices and E is the number of edges.