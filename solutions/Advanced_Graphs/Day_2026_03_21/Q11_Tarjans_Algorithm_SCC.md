# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, and the task is to identify all SCCs. For example, in a graph with vertices {1, 2, 3, 4, 5} and edges {(1, 2), (2, 3), (3, 1), (4, 5)}, the SCCs are {1, 2, 3} and {4, 5}.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to find SCCs. It assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex. The algorithm then groups vertices into SCCs based on these indices. Tarjan's algorithm has a time complexity of O(V + E), where V is the number of vertices and E is the number of edges.

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
        vector<int> index(n, -1);
        vector<int> low(n, -1);
        vector<int> stack;
        vector<vector<int>> sccs;
        int idx = 0;

        for (int i = 0; i < n; ++i) {
            if (index[i] == -1) {
                strongConnect(i, graph, index, low, stack, sccs, idx);
            }
        }

        return sccs;
    }

    void strongConnect(int v, const vector<vector<int>>& graph, vector<int>& index, vector<int>& low, vector<int>& stack, vector<vector<int>>& sccs, int& idx) {
        index[v] = idx;
        low[v] = idx;
        idx++;
        stack.push_back(v);

        for (int w : graph[v]) {
            if (index[w] == -1) {
                strongConnect(w, graph, index, low, stack, sccs, idx);
                low[v] = min(low[v], low[w]);
            } else if (find(stack.begin(), stack.end(), w) != stack.end()) {
                low[v] = min(low[v], index[w]);
            }
        }

        if (low[v] == index[v]) {
            vector<int> scc;
            while (true) {
                int w = stack.back();
                stack.pop_back();
                scc.push_back(w);
                if (w == v) break;
            }
            sccs.push_back(scc);
        }
    }
};

int main() {
    vector<vector<int>> graph = {{1}, {2}, {0}, {4}, {3}};
    Tarjan tarjan;
    vector<vector<int>> sccs = tarjan.scc(graph);
    for (const auto& scc : sccs) {
        cout << "SCC: ";
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
Graph with vertices {1, 2, 3, 4, 5} and edges {(1, 2), (2, 3), (3, 1), (4, 5)}
Output: 
SCC: 0 1 2 
SCC: 3 4 
```

## Key Takeaways
- Tarjan's algorithm uses DFS to find SCCs in a directed graph.
- The algorithm assigns a unique index to each vertex based on the order of visitation and keeps track of the lowest reachable index for each vertex.
- The time complexity of Tarjan's algorithm is O(V + E), where V is the number of vertices and E is the number of edges.