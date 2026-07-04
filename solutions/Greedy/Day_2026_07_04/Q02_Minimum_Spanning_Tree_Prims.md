# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph, find the Minimum Spanning Tree (MST) using Prim's algorithm. The graph is represented as an adjacency list, where each node is connected to its neighboring nodes with their respective edge weights. The goal is to find the subset of edges that connect all nodes in the graph with the minimum total edge weight. The graph has 'n' nodes and 'm' edges, and the edge weights are non-negative.

## Approach
Prim's algorithm uses a greedy approach to find the MST by selecting the minimum-weight edge that connects a node in the MST to a node not yet in the MST. This process is repeated until all nodes are included in the MST. The algorithm starts with an arbitrary node and grows the tree by adding the minimum-weight edge at each step.

## Complexity
- Time: O((n + m) log n)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class DisjointSet {
public:
    vector<int> parent;
    vector<int> rank;

    DisjointSet(int n) {
        parent.resize(n + 1);
        rank.resize(n + 1, 0);
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
        }
    }

    int find(int node) {
        if (node == parent[node]) {
            return node;
        }
        return parent[node] = find(parent[node]);
    }

    void unionByRank(int u, int v) {
        int op1 = find(u);
        int op2 = find(v);
        if (op1 == op2) {
            return;
        }
        if (rank[op1] < rank[op2]) {
            parent[op1] = op2;
        } else if (rank[op2] < rank[op1]) {
            parent[op2] = op1;
        } else {
            parent[op1] = op2;
            rank[op2]++;
        }
    }
};

vector<vector<int>> primMST(int n, vector<vector<int>>& edges) {
    vector<vector<int>> result;
    DisjointSet ds(n);
    vector<vector<int>> adjList(n);
    for (auto& edge : edges) {
        adjList[edge[0]].push_back({edge[1], edge[2]});
        adjList[edge[1]].push_back({edge[0], edge[2]});
    }
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
    pq.push({0, 0, 0}); // weight, node, parent
    while (!pq.empty()) {
        auto edge = pq.top();
        pq.pop();
        int weight = edge[0];
        int node = edge[1];
        int parent = edge[2];
        if (ds.find(node) != ds.find(parent)) {
            result.push_back({parent, node, weight});
            ds.unionByRank(node, parent);
            for (auto& neighbor : adjList[node]) {
                if (ds.find(neighbor[0]) != ds.find(node)) {
                    pq.push({neighbor[1], neighbor[0], node});
                }
            }
        }
    }
    return result;
}

int main() {
    int n = 5;
    vector<vector<int>> edges = {{0, 1, 2}, {0, 3, 6}, {1, 2, 3}, {1, 3, 8}, {1, 4, 5}, {2, 4, 7}, {3, 4, 9}};
    vector<vector<int>> mst = primMST(n, edges);
    for (auto& edge : mst) {
        cout << edge[0] << " - " << edge[1] << " : " << edge[2] << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 
n = 5
edges = [[0, 1, 2], [0, 3, 6], [1, 2, 3], [1, 3, 8], [1, 4, 5], [2, 4, 7], [3, 4, 9]]
Output: 
0 - 1 : 2
1 - 2 : 3
1 - 4 : 5
0 - 3 : 6
```

## Key Takeaways
- Prim's algorithm is used to find the Minimum Spanning Tree of a connected, undirected, and weighted graph.
- The algorithm starts with an arbitrary node and grows the tree by adding the minimum-weight edge at each step.
- The time complexity of Prim's algorithm is O((n + m) log n), where 'n' is the number of nodes and 'm' is the number of edges in the graph.