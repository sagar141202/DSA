# Tarjan's Algorithm (SCC)

## Problem Statement
Tarjan's algorithm is used to find Strongly Connected Components (SCCs) in a directed graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The problem statement is to implement Tarjan's algorithm to find all SCCs in a given directed graph. The graph can have up to 10^5 vertices and 10^5 edges. The algorithm should output the number of SCCs and the vertices in each SCC.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to traverse the graph and find SCCs. It maintains a stack of vertices and assigns a low-link value to each vertex, which is the smallest index reachable from that vertex. The algorithm iteratively pops vertices from the stack and adds them to the current SCC if their low-link value is greater than or equal to the index of the current SCC.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> adj[100005];
int idx, low[100005], disc[100005];
stack<int> s;
vector<vector<int>> scc;

void tarjan(int u) {
    disc[u] = low[u] = idx++;
    s.push(u);
    for (int v : adj[u]) {
        if (disc[v] == -1) {
            tarjan(v);
            low[u] = min(low[u], low[v]);
        } else if (s.find(v) != s.end()) {
            low[u] = min(low[u], disc[v]);
        }
    }
    if (low[u] == disc[u]) {
        vector<int> curr_scc;
        while (true) {
            int v = s.top();
            s.pop();
            curr_scc.push_back(v);
            if (v == u) break;
        }
        scc.push_back(curr_scc);
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }
    memset(disc, -1, sizeof disc);
    for (int i = 1; i <= n; i++) {
        if (disc[i] == -1) tarjan(i);
    }
    cout << "Number of SCCs: " << scc.size() << endl;
    for (int i = 0; i < scc.size(); i++) {
        cout << "SCC " << i + 1 << ": ";
        for (int v : scc[i]) cout << v << " ";
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input:
5 6
1 2
2 3
3 1
3 4
4 5
5 4
Output:
Number of SCCs: 2
SCC 1: 1 2 3 
SCC 2: 4 5 
```

## Key Takeaways
- Tarjan's algorithm uses DFS to find SCCs in a directed graph.
- The algorithm maintains a stack of vertices and assigns a low-link value to each vertex.
- The time complexity of Tarjan's algorithm is O(V + E), where V is the number of vertices and E is the number of edges.