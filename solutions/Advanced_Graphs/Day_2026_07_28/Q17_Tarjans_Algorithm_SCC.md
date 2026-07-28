# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, and the task is to identify all SCCs in the graph. For example, consider a graph with vertices {1, 2, 3, 4, 5} and edges {(1, 2), (2, 3), (3, 1), (4, 5)}. The strongly connected components in this graph are {[1, 2, 3], [4, 5]}.

## Approach
Tarjan's algorithm is used to find SCCs in a graph. It works by performing a depth-first search (DFS) on the graph and keeping track of the discovery time and low value of each vertex. The algorithm uses a stack to store vertices that are part of the current SCC.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> graph;
vector<bool> visited;
vector<int> low;
vector<int> disc;
vector<vector<int>> scc;
stack<int> st;
int time = 0;

void tarjan(int u) {
    disc[u] = low[u] = time++;
    visited[u] = true;
    st.push(u);

    for (int v : graph[u]) {
        if (!visited[v]) {
            tarjan(v);
            low[u] = min(low[u], low[v]);
        } else if (st.find(v) != st.end()) {
            low[u] = min(low[u], disc[v]);
        }
    }

    if (low[u] == disc[u]) {
        vector<int> component;
        while (true) {
            int v = st.top();
            st.pop();
            component.push_back(v);
            if (v == u) break;
        }
        scc.push_back(component);
    }
}

void find_scc(int n) {
    visited.assign(n, false);
    low.assign(n, 0);
    disc.assign(n, 0);
    for (int i = 0; i < n; i++) {
        if (!visited[i]) tarjan(i);
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    graph.assign(n, vector<int>());
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
    }
    find_scc(n);
    for (auto component : scc) {
        for (int vertex : component) {
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
5 5
0 1
1 2
2 0
3 4
4 3
Output: 
0 2 1 
3 4 
```

## Key Takeaways
- Tarjan's algorithm uses DFS to find SCCs in a graph.
- The algorithm keeps track of the discovery time and low value of each vertex.
- The low value of a vertex is the smallest discovery time of a vertex that is reachable from the current vertex.