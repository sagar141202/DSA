# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of undirected edges `edges` where `edges[i] = [ui, vi]` represents a edge between node `ui` and `vi`, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles, and it should have `n-1` edges. The nodes are numbered from 0 to `n-1`.

## Approach
We can use Depth-First Search (DFS) or Union-Find algorithm to detect cycles in the graph. If the graph has no cycles and is connected, it's a valid tree. We will use the Union-Find algorithm for this problem. The algorithm checks if the number of edges is `n-1` and if the graph is connected.

## Complexity
- Time: O(n + m * α(n))
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class UnionFind {
public:
    vector<int> parent;
    UnionFind(int n) {
        parent.resize(n);
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
            parent[rootX] = rootY;
        }
    }
};

class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if (edges.size() != n - 1) {
            return false;
        }

        UnionFind uf(n);
        for (auto& edge : edges) {
            int x = edge[0];
            int y = edge[1];
            if (uf.find(x) == uf.find(y)) {
                return false;
            }
            uf.unionSet(x, y);
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            if (uf.parent[i] == i) {
                count++;
            }
        }
        return count == 1;
    }
};
```

## Test Cases
```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

## Key Takeaways
- The Union-Find algorithm can be used to detect cycles in a graph.
- A valid tree should have `n-1` edges.
- The graph should be connected, meaning there should be only one connected component.