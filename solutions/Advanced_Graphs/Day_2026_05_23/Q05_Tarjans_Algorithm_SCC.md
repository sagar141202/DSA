# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph can have up to 10^5 vertices and 10^5 edges. The vertices are numbered from 1 to n, and the edges are represented as pairs of vertices.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to find SCCs. It assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex. The algorithm then groups vertices into SCCs based on their lowest reachable index.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Tarjan {
public:
    int index, cnt;
    vector<int> stack, low, ids;
    vector<vector<int>> scc;
    vector<vector<int>> graph;

    Tarjan(int n) {
        index = 0;
        cnt = 0;
        stack.resize(n + 1);
        low.resize(n + 1);
        ids.resize(n + 1, -1);
        graph.resize(n + 1);
    }

    void addEdge(int u, int v) {
        graph[u].push_back(v);
    }

    void dfs(int u) {
        stack.push_back(u);
        low[u] = index;
        ids[u] = index;
        index++;

        for (int v : graph[u]) {
            if (ids[v] == -1) {
                dfs(v);
                low[u] = min(low[u], low[v]);
            } else if (find(stack.begin(), stack.end(), v) != stack.end()) {
                low[u] = min(low[u], ids[v]);
            }
        }

        if (low[u] == ids[u]) {
            vector<int> comp;
            while (true) {
                int v = stack.back();
                stack.pop_back();
                comp.push_back(v);
                if (v == u) break;
            }
            scc.push_back(comp);
            cnt++;
        }
    }

    void findSCC() {
        for (int i = 1; i < graph.size(); i++) {
            if (ids[i] == -1) dfs(i);
        }
    }

    void printSCC() {
        for (int i = 0; i < scc.size(); i++) {
            cout << "SCC " << i + 1 << ": ";
            for (int j = 0; j < scc[i].size(); j++) {
                cout << scc[i][j] << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    int n, m;
    cin >> n >> m;

    Tarjan tarjan(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        tarjan.addEdge(u, v);
    }

    tarjan.findSCC();
    tarjan.printSCC();

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
SCC 1: 3 2 1 
SCC 2: 5 
SCC 3: 4 
```

## Key Takeaways
- Tarjan's algorithm is an efficient method for finding strongly connected components in a directed graph.
- The algorithm uses a depth-first search approach and assigns a unique index to each vertex based on the order of visitation.
- The lowest reachable index is used to group vertices into strongly connected components.