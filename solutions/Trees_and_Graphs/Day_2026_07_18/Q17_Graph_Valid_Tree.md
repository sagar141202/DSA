# Graph Valid Tree

## Problem Statement
Given `n` nodes and an array of edges, determine if the graph is a valid tree. A valid tree is a graph that is connected and has no cycles. The input is given as `n` (the number of nodes) and `edges` (a 2D array representing the edges in the graph). The function should return `true` if the graph is a valid tree and `false` otherwise. For example, given `n = 5` and `edges = [[0, 1], [0, 2], [0, 3], [1, 4]]`, the function should return `true`. However, given `n = 5` and `edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]`, the function should return `false` because the graph has a cycle.

## Approach
To solve this problem, we can use a union-find algorithm to check if the graph is connected and has no cycles. We iterate over the edges and union the nodes. If we find a cycle (i.e., two nodes that are already in the same set), we return `false`. If we have iterated over all edges and the number of sets is 1, we return `true`.

## Complexity
- Time: O(n + m * α(n))
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class UnionFind {
public:
    vector<int> parent;
    int count;

    UnionFind(int n) {
        parent.resize(n);
        count = n;
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
            count--;
        }
    }

    int getCount() {
        return count;
    }
};

bool validTree(int n, vector<vector<int>>& edges) {
    UnionFind uf(n);
    for (auto& edge : edges) {
        int x = edge[0];
        int y = edge[1];
        if (uf.find(x) == uf.find(y)) {
            return false;
        }
        uf.unionSet(x, y);
    }
    return uf.getCount() == 1;
}

int main() {
    int n = 5;
    vector<vector<int>> edges = {{0, 1}, {0, 2}, {0, 3}, {1, 4}};
    cout << boolalpha << validTree(n, edges) << endl;  // Output: true
    return 0;
}
```

## Test Cases
```
Input: n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true
Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false
```

## Key Takeaways
- A valid tree is a graph that is connected and has no cycles.
- The union-find algorithm can be used to check if a graph is a valid tree.
- The time complexity of the union-find algorithm is O(n + m * α(n)), where n is the number of nodes and m is the number of edges.