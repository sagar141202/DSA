# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) using Prim's algorithm. The MST is a subgraph that connects all vertices with the minimum total edge weight. The graph is represented as an adjacency list, where each edge is a tuple of (u, v, w) denoting an edge between vertices u and v with weight w. The input graph may have multiple edges between the same pair of vertices, and the graph may contain self-loops.

## Approach
Prim's algorithm works by maintaining a set of visited vertices and iteratively adding the minimum-weight edge that connects a visited vertex to an unvisited vertex. The algorithm starts with an arbitrary vertex and grows the MST by adding edges one by one. The key intuition is to always choose the minimum-weight edge that does not form a cycle.

## Complexity
- Time: O(E log V)
- Space: O(V + E)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class DisjointSet {
public:
    vector<int> parent, rank;
    DisjointSet(int n) {
        parent.resize(n + 1);
        rank.resize(n + 1, 0);
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
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
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};

vector<vector<int>> primMST(vector<vector<int>>& graph, int V) {
    vector<vector<int>> mst;
    DisjointSet ds(V);
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
    for (int i = 1; i <= V; i++) {
        for (auto& edge : graph[i]) {
            pq.push({edge[2], i, edge[0]});
        }
    }
    while (!pq.empty() && mst.size() < V - 1) {
        auto edge = pq.top();
        pq.pop();
        if (ds.find(edge[1]) != ds.find(edge[2])) {
            mst.push_back({edge[1], edge[2], edge[0]});
            ds.unionSet(edge[1], edge[2]);
        }
    }
    return mst;
}

int main() {
    int V = 5;
    vector<vector<int>> graph(V + 1);
    graph[1].push_back({2, 2});
    graph[1].push_back({3, 3});
    graph[2].push_back({1, 2});
    graph[2].push_back({3, 1});
    graph[2].push_back({4, 1});
    graph[2].push_back({5, 4});
    graph[3].push_back({1, 3});
    graph[3].push_back({2, 1});
    graph[3].push_back({5, 5});
    graph[4].push_back({2, 1});
    graph[4].push_back({5, 1});
    graph[5].push_back({2, 4});
    graph[5].push_back({3, 5});
    graph[5].push_back({4, 1});
    vector<vector<int>> mst = primMST(graph, V);
    for (auto& edge : mst) {
        cout << edge[0] << " " << edge[1] << " " << edge[2] << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 
Graph with 5 vertices and edges: (1, 2, 2), (1, 3, 3), (2, 3, 1), (2, 4, 1), (2, 5, 4), (3, 5, 5), (4, 5, 1)
Output: 
2 1 2
2 3 1
2 4 1
4 5 1
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm that works by maintaining a set of visited vertices and iteratively adding the minimum-weight edge that connects a visited vertex to an unvisited vertex.
- The algorithm uses a disjoint-set data structure to keep track of connected components and avoid cycles.
- The time complexity of Prim's algorithm is O(E log V) due to the use of a priority queue to select the minimum-weight edge.