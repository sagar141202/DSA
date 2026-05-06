# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) using Tarjan's algorithm. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The input graph is represented as an adjacency list, and the output should be a list of lists, where each inner list contains the vertices of an SCC. The graph has n vertices and m edges, and the vertices are numbered from 1 to n.

## Approach
Tarjan's algorithm uses a depth-first search (DFS) to traverse the graph and find SCCs. It maintains a stack of vertices and assigns a low-link value to each vertex, which is the smallest index reachable from that vertex. The algorithm iteratively pops vertices from the stack and adds them to the current SCC if their low-link value is greater than or equal to the index of the current vertex.

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
        vector<int> index(n, -1);
        vector<int> low(n, -1);
        vector<bool> onStack(n, false);
        stack<int> stack;
        vector<vector<int>> scc;
        int idx = 0;

        for (int i = 0; i < n; i++) {
            if (index[i] == -1) {
                strongConnect(i, index, low, onStack, stack, scc, idx, graph);
            }
        }

        return scc;
    }

private:
    void strongConnect(int v, vector<int>& index, vector<int>& low, vector<bool>& onStack, stack<int>& stack, vector<vector<int>>& scc, int& idx, vector<vector<int>>& graph) {
        index[v] = idx;
        low[v] = idx;
        idx++;
        stack.push(v);
        onStack[v] = true;

        for (int w : graph[v]) {
            if (index[w] == -1) {
                strongConnect(w, index, low, onStack, stack, scc, idx, graph);
                low[v] = min(low[v], low[w]);
            } else if (onStack[w]) {
                low[v] = min(low[v], index[w]);
            }
        }

        if (low[v] == index[v]) {
            vector<int> component;
            while (true) {
                int w = stack.top();
                stack.pop();
                onStack[w] = false;
                component.push_back(w);
                if (w == v) break;
            }
            scc.push_back(component);
        }
    }
};

int main() {
    int n = 5;
    vector<vector<int>> graph = {{1}, {0, 2}, {1, 3}, {2, 4}, {3}};

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
    0 -> 1
    1 -> 0, 2
    2 -> 1, 3
    3 -> 2, 4
    4 -> 3
Output: 
    0 1 
    2 3 4 
```

## Key Takeaways
- Tarjan's algorithm uses a depth-first search to find strongly connected components in a directed graph.
- The algorithm maintains a stack of vertices and assigns a low-link value to each vertex to determine the strongly connected components.
- The time complexity of Tarjan's algorithm is O(V + E), where V is the number of vertices and E is the number of edges in the graph.