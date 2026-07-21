# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors. The given node will always be in the graph and will never be null. The number of nodes in the graph is in the range [1, 100] for each test case. There are no duplicate values in the graph.

## Approach
We will use a depth-first search (DFS) approach to traverse the graph and create a clone of each node. We will store the cloned nodes in a hashmap to avoid cloning the same node multiple times. The DFS function will recursively clone the neighbors of each node.

## Complexity
- Time: O(N + M)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for a Node.
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
        unordered_map<Node*, Node*> m;
        return dfs(node, m);
    }
    
    Node* dfs(Node* node, unordered_map<Node*, Node*>& m) {
        if (m.find(node) != m.end()) return m[node];
        Node* clone = new Node(node->val);
        m[node] = clone;
        for (Node* neighbor : node->neighbors) {
            clone->neighbors.push_back(dfs(neighbor, m));
        }
        return clone;
    }
};
```

## Test Cases
```
Input: [[2,1],[1,2]]
Output: [[2,1],[1,2]]
```

## Key Takeaways
- Use a hashmap to store the cloned nodes to avoid cloning the same node multiple times.
- Use a DFS approach to traverse the graph and clone each node.
- The DFS function should recursively clone the neighbors of each node.