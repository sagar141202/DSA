# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph can have up to 10^5 vertices and 10^5 edges. The vertices are numbered from 1 to n, where n is the number of vertices.

## Approach
Tarjan's algorithm uses depth-first search to find all SCCs in a graph. It works by maintaining a stack of vertices and a low-link value for each vertex, which is the smallest index reachable from that vertex. The algorithm iteratively pops vertices from the stack and assigns them to the current SCC if their low-link value is greater than or equal to the index of the current SCC.

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
int time = 0;
stack<int> st;

void tarjan(int u) {
    disc[u] = low[u] = time++;
    visited[u] = true;
    st.push(u);

    for (int v : graph[u]) {
        if (!disc[v]) {
            tarjan(v);
            low[u] = min(low[u], low[v]);
        } else if (visited[v]) {
            low[u] = min(low[u], disc[v]);
        }
    }

    if (low[u] == disc[u]) {
        vector<int> component;
        while (true) {
            int v = st.top();
            st.pop();
            visited[v] = false;
            component.push_back(v);
            if (v == u) break;
        }
        scc.push_back(component);
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    graph.resize(n);
    visited.resize(n, false);
    low.resize(n);
    disc.resize(n);

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        u--, v--; // 0-based indexing
        graph[u].push_back(v);
    }

    for (int i = 0; i < n; i++) {
        if (!disc[i]) tarjan(i);
    }

    for (auto component : scc) {
        for (int vertex : component) {
            cout << vertex + 1 << " "; // 1-based indexing
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
1 2
2 3
3 1
3 4
4 5

Output: 
1 2 3 
4 
5 
```

## Key Takeaways
- Tarjan's algorithm uses a depth-first search approach to find all strongly connected components in a graph.
- The low-link value is used to determine whether a vertex belongs to the current SCC.
- The algorithm has a linear time complexity, making it efficient for large graphs.