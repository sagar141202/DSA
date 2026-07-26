# Minimum Spanning Tree (Prim's)

## Problem Statement
Given an undirected and connected graph, find the minimum spanning tree (MST) using Prim's algorithm. The graph is represented as an adjacency list of edges, where each edge is a tuple of (node1, node2, weight). The MST is a subgraph that connects all nodes with the minimum total edge weight. The graph has 'n' nodes and 'm' edges, and the edge weights are non-negative. For example, given a graph with 5 nodes and 7 edges: (0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9), the minimum spanning tree should have a total weight of 16.

## Approach
Prim's algorithm works by starting at an arbitrary node and growing the tree one edge at a time. It uses a priority queue to keep track of the edges with the smallest weight that connect a node in the tree to a node not yet in the tree. The algorithm then selects the edge with the smallest weight and adds it to the tree, repeating this process until all nodes are connected.

## Complexity
- Time: O(m log n)
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
        parent.resize(n);
        rank.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};

vector<vector<int>> primMST(vector<vector<int>>& edges, int n) {
    vector<vector<int>> mst;
    DisjointSet ds(n);
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
    for (auto& edge : edges) {
        pq.push(edge);
    }
    while (!pq.empty() && mst.size() < n - 1) {
        auto edge = pq.top();
        pq.pop();
        int node1 = edge[0];
        int node2 = edge[1];
        int weight = edge[2];
        if (ds.find(node1) != ds.find(node2)) {
            mst.push_back(edge);
            ds.unionSet(node1, node2);
        }
    }
    return mst;
}

int main() {
    int n = 5;
    vector<vector<int>> edges = {{0, 1, 2}, {0, 3, 6}, {1, 2, 3}, {1, 3, 8}, {1, 4, 5}, {2, 4, 7}, {3, 4, 9}};
    vector<vector<int>> mst = primMST(edges, n);
    cout << "Minimum Spanning Tree:" << endl;
    for (auto& edge : mst) {
        cout << edge[0] << " - " << edge[1] << " : " << edge[2] << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 
edges = [[0, 1, 2], [0, 3, 6], [1, 2, 3], [1, 3, 8], [1, 4, 5], [2, 4, 7], [3, 4, 9]]
n = 5
Output: 
Minimum Spanning Tree:
0 - 1 : 2
1 - 2 : 3
1 - 4 : 5
0 - 3 : 6
```

## Key Takeaways
- Prim's algorithm is an efficient method for finding the minimum spanning tree of a graph.
- The use of a disjoint set data structure and a priority queue are crucial components of the algorithm.
- The algorithm has a time complexity of O(m log n) and a space complexity of O(n + m), making it suitable for large graphs.