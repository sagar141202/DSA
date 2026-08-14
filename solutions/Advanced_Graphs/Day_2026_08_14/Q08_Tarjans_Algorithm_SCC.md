# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its neighbors. The algorithm should output the number of SCCs and the vertices in each SCC.

## Approach
Tarjan's algorithm uses depth-first search to traverse the graph and assigns a unique index to each vertex based on the order it is visited. It also keeps track of the lowest reachable index for each vertex, which helps in identifying the SCCs.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void tarjanSCC(vector<vector<int>>& graph, int vertex, vector<int>& index, vector<int>& low, vector<bool>& onStack, stack<int>& stack, vector<vector<int>>& sccs, int& idx) {
    index[vertex] = idx;
    low[vertex] = idx;
    idx++;
    stack.push(vertex);
    onStack[vertex] = true;

    for (int neighbor : graph[vertex]) {
        if (index[neighbor] == -1) {
            tarjanSCC(graph, neighbor, index, low, onStack, stack, sccs, idx);
            low[vertex] = min(low[vertex], low[neighbor]);
        } else if (onStack[neighbor]) {
            low[vertex] = min(low[vertex], index[neighbor]);
        }
    }

    if (low[vertex] == index[vertex]) {
        vector<int> scc;
        while (true) {
            int w = stack.top();
            stack.pop();
            onStack[w] = false;
            scc.push_back(w);
            if (w == vertex) break;
        }
        sccs.push_back(scc);
    }
}

vector<vector<int>> tarjan(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> index(n, -1);
    vector<int> low(n, -1);
    vector<bool> onStack(n, false);
    stack<int> stack;
    vector<vector<int>> sccs;
    int idx = 0;

    for (int i = 0; i < n; i++) {
        if (index[i] == -1) {
            tarjanSCC(graph, i, index, low, onStack, stack, sccs, idx);
        }
    }

    return sccs;
}

int main() {
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2}};
    vector<vector<int>> sccs = tarjan(graph);

    cout << "Number of SCCs: " << sccs.size() << endl;
    for (int i = 0; i < sccs.size(); i++) {
        cout << "SCC " << i + 1 << ": ";
        for (int vertex : sccs[i]) {
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
Graph:
0 -> 1
1 -> 0, 2
2 -> 1, 3
3 -> 2

Output: 
Number of SCCs: 1
SCC 1: 0 1 2 3
```

## Key Takeaways
- Tarjan's algorithm is used to find all strongly connected components (SCCs) in a directed graph.
- The algorithm uses depth-first search to traverse the graph and assigns a unique index to each vertex based on the order it is visited.
- The lowest reachable index for each vertex helps in identifying the SCCs.