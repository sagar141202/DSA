# Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, and weighted graph with V vertices and E edges, find the Minimum Spanning Tree (MST) of the graph using Prim's algorithm. The graph is represented as an adjacency list, where each edge is a tuple of (u, v, w) representing an edge between vertices u and v with weight w. The MST is a subgraph that connects all vertices with the minimum total weight. The constraints are 1 ≤ V ≤ 10^5 and 1 ≤ E ≤ 10^6. For example, given a graph with vertices {0, 1, 2, 3, 4} and edges {(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)}, the MST should have a total weight of 19.

## Approach
Prim's algorithm works by maintaining a set of visited vertices and iteratively adding the minimum-weight edge that connects a visited vertex to an unvisited vertex. The algorithm uses a priority queue to efficiently select the minimum-weight edge. The key intuition is to always choose the locally optimal edge, which leads to a globally optimal solution.

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
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) {
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

class Graph {
public:
    int V;
    vector<vector<pair<int, int>>> adj;
    Graph(int v) {
        V = v;
        adj.resize(v);
    }
    void addEdge(int u, int v, int w) {
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }
    vector<pair<int, int>> primMST() {
        vector<pair<int, int>> mst;
        vector<bool> visited(V, false);
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
        pq.push({0, {0, -1}});
        while (!pq.empty()) {
            int w = pq.top().first;
            int u = pq.top().second.first;
            int v = pq.top().second.second;
            pq.pop();
            if (!visited[u]) {
                visited[u] = true;
                if (v != -1) {
                    mst.push_back({u, v});
                }
                for (auto neighbor : adj[u]) {
                    if (!visited[neighbor.first]) {
                        pq.push({neighbor.second, {neighbor.first, u}});
                    }
                }
            }
        }
        return mst;
    }
};

int main() {
    int V = 5;
    Graph g(V);
    g.addEdge(0, 1, 10);
    g.addEdge(0, 2, 6);
    g.addEdge(0, 3, 5);
    g.addEdge(1, 3, 15);
    g.addEdge(2, 3, 4);
    vector<pair<int, int>> mst = g.primMST();
    int totalWeight = 0;
    for (auto edge : mst) {
        totalWeight += g.adj[edge.first][0].second;
    }
    cout << "Total weight of MST: " << totalWeight << endl;
    return 0;
}
```

## Test Cases
```
Input: 
Vertices: 5
Edges: [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
Output: 
Total weight of MST: 19
```

## Key Takeaways
- Prim's algorithm is a greedy algorithm that finds the Minimum Spanning Tree of a graph by iteratively adding the minimum-weight edge that connects a visited vertex to an unvisited vertex.
- The time complexity of Prim's algorithm is O(E log V) using a priority queue, where E is the number of edges and V is the number of vertices.
- The space complexity of Prim's algorithm is O(V + E), where V is the number of vertices and E is the number of edges.