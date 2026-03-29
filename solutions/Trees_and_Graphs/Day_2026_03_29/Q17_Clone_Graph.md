# Clone Graph

## Problem Statement
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. The nodes are labeled uniquely. We need to create a deep copy of the given graph. The nodes in the given graph are connected in a specific way, and the same connection should exist in the cloned graph. The cloned graph should have the same nodes with the same values and the same edges between them. The constraints are that the number of nodes in the graph will not exceed 100, and the nodes' values are between 1 and 100.

## Approach
We will use a depth-first search (DFS) approach to traverse the graph and clone each node. We will also use an unordered map to store the cloned nodes to avoid cloning the same node multiple times. The algorithm will start from a given node, clone it, and then recursively clone its neighbors.

## Complexity
- Time: O(N + M)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return NULL;
        unordered_map<Node*, Node*> map;
        return dfs(node, map);
    }
    
    Node* dfs(Node* node, unordered_map<Node*, Node*>& map) {
        if (map.find(node) != map.end()) return map[node];
        Node* clone = new Node(node->val);
        map[node] = clone;
        for (Node* neighbor : node->neighbors) {
            clone->neighbors.push_back(dfs(neighbor, map));
        }
        return clone;
    }
};
```

## Test Cases
```
Input: [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
```

## Key Takeaways
- Use DFS to traverse the graph and clone each node.
- Use an unordered map to store the cloned nodes to avoid cloning the same node multiple times.
- The time complexity is O(N + M), where N is the number of nodes and M is the number of edges.