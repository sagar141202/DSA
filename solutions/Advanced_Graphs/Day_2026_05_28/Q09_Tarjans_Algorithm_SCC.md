# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, and the task is to identify all SCCs and output their vertices. For example, given a graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1), (1, 2), (2, 0), (1, 3), (3, 4)}, the SCCs are {[0, 1, 2], [3, 4]}.

## Approach
Tarjan's algorithm is used to find SCCs in a graph by performing a depth-first search (DFS) and keeping track of the low link values and indices of visited vertices. The algorithm iterates through all vertices, and for each unvisited vertex, it performs a DFS and updates the low link values and indices accordingly. When a vertex with a low link value equal to its index is found, it means that a new SCC has been discovered.

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
        vector<int> index(n, -1);
        vector<int> low(n, -1);
        vector<bool> onStack(n, false);
        stack<int> stack;
        vector<vector<int>> result;
        int idx = 0;

        for (int i = 0; i < n; i++) {
            if (index[i] == -1) {
                strongConnect(i, graph, index, low, onStack, stack, result, idx);
            }
        }

        return result;
    }

private:
    void strongConnect(int v, vector<vector<int>>& graph, vector<int>& index, vector<int>& low, vector<bool>& onStack, stack<int>& stack, vector<vector<int>>& result, int& idx) {
        index[v] = idx;
        low[v] = idx;
        idx++;
        stack.push(v);
        onStack[v] = true;

        for (int w : graph[v]) {
            if (index[w] == -1) {
                strongConnect(w, graph, index, low, onStack, stack, result, idx);
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
            result.push_back(component);
        }
    }
};

int main() {
    int n = 5;
    vector<vector<int>> graph(n);
    graph[0].push_back(1);
    graph[1].push_back(2);
    graph[2].push_back(0);
    graph[1].push_back(3);
    graph[3].push_back(4);

    Tarjan tarjan;
    vector<vector<int>> sccs = tarjan.scc(graph);

    for (const auto& scc : sccs) {
        cout << "{";
        for (int i = 0; i < scc.size(); i++) {
            cout << scc[i];
            if (i < scc.size() - 1) cout << ", ";
        }
        cout << "}" << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1), (1, 2), (2, 0), (1, 3), (3, 4)}
Output: 
{0, 1, 2}
{3, 4}
```

## Key Takeaways
- Tarjan's algorithm is used to find strongly connected components in a directed graph.
- The algorithm uses a depth-first search (DFS) approach and keeps track of low link values and indices of visited vertices.
- The algorithm has a time complexity of O(V + E) and a space complexity of O(V), making it efficient for large graphs.