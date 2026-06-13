# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, and the task is to identify all SCCs in the graph. For example, in a graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1), (1, 2), (2, 0), (3, 4)}, there are two SCCs: {0, 1, 2} and {3, 4}.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to traverse the graph and identify SCCs. It maintains a stack of vertices and assigns a low-link value to each vertex, which is the smallest index reachable from that vertex. The algorithm iterates through the graph, popping vertices from the stack when a strongly connected component is found.

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
        vector<int> stack;
        vector<vector<int>> result;
        int idx = 0;

        function<void(int)> strongconnect = [&](int node) {
            index[node] = idx;
            low[node] = idx;
            idx++;
            stack.push_back(node);

            for (int neighbor : graph[node]) {
                if (index[neighbor] == -1) {
                    strongconnect(neighbor);
                    low[node] = min(low[node], low[neighbor]);
                } else if (find(stack.begin(), stack.end(), neighbor) != stack.end()) {
                    low[node] = min(low[node], index[neighbor]);
                }
            }

            if (low[node] == index[node]) {
                vector<int> component;
                while (true) {
                    int w = stack.back();
                    stack.pop_back();
                    component.push_back(w);
                    if (w == node) break;
                }
                result.push_back(component);
            }
        };

        for (int i = 0; i < n; i++) {
            if (index[i] == -1) strongconnect(i);
        }

        return result;
    }
};

int main() {
    int n = 5;
    vector<vector<int>> graph(n);
    graph[0].push_back(1);
    graph[1].push_back(2);
    graph[2].push_back(0);
    graph[3].push_back(4);

    Tarjan tarjan;
    vector<vector<int>> sccs = tarjan.scc(graph);

    for (const auto& scc : sccs) {
        for (int node : scc) {
            cout << node << " ";
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
- Tarjan's algorithm uses DFS to find strongly connected components in a graph.
- The algorithm maintains a stack of vertices and assigns a low-link value to each vertex.
- The time complexity of Tarjan's algorithm is O(V + E), where V is the number of vertices and E is the number of edges.