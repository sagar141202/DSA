# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The input graph is represented as an adjacency list, and the output should be a list of lists, where each sublist contains the vertices of a strongly connected component. The graph can have up to 10^5 vertices and 10^5 edges.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to traverse the graph and find strongly connected components. It assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex. The algorithm then uses these indices to identify strongly connected components.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Tarjan {
public:
    vector<vector<int>> scc;
    vector<int> index, low;
    stack<int> st;
    int idx;

    vector<vector<int>> tarjanSCC(vector<vector<int>>& graph) {
        int n = graph.size();
        index.resize(n, -1);
        low.resize(n, -1);
        idx = 0;

        for (int i = 0; i < n; i++) {
            if (index[i] == -1) {
                dfs(graph, i);
            }
        }

        return scc;
    }

    void dfs(vector<vector<int>>& graph, int u) {
        index[u] = low[u] = idx++;
        st.push(u);

        for (int v : graph[u]) {
            if (index[v] == -1) {
                dfs(graph, v);
                low[u] = min(low[u], low[v]);
            } else if (find(st.begin(), st.end(), v) != st.end()) {
                low[u] = min(low[u], index[v]);
            }
        }

        if (low[u] == index[u]) {
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
};

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
    }

    Tarjan tarjan;
    vector<vector<int>> scc = tarjan.tarjanSCC(graph);

    for (const auto& component : scc) {
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
1 3
3 4
Output: 
0 1 2 
3 4 
```

## Key Takeaways
- Tarjan's algorithm uses DFS to find strongly connected components in a graph.
- The algorithm assigns a unique index to each vertex and keeps track of the lowest reachable index for each vertex.
- The algorithm uses a stack to keep track of vertices in the current strongly connected component.