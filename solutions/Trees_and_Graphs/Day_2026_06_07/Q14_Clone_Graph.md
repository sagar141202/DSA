# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors. The number of nodes in the graph is in the range [1, 100] for each test case. There is no repeated val value for each node in the graph. In other words, no two nodes cover the same label. You may assume the input node is never null. The graph is represented in such a way that each node value is in the range [1, 100] and for a node with val m, its neighbors are any node with values m + 1 or m - 1. The graph does not contain self-loops or parallel edges.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the graph and clone each node. It utilizes an unordered map to store the cloned nodes to avoid cloning the same node multiple times. The DFS function recursively clones the neighbors of each node.

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
        if (!node) return nullptr;
        unordered_map<Node*, Node*> cloned;
        return dfs(node, cloned);
    }
    
    Node* dfs(Node* node, unordered_map<Node*, Node*>& cloned) {
        if (cloned.find(node) != cloned.end()) return cloned[node];
        Node* clone = new Node(node->val);
        cloned[node] = clone;
        for (Node* neighbor : node->neighbors) {
            clone->neighbors.push_back(dfs(neighbor, cloned));
        }
        return clone;
    }
};
```

## Test Cases
```
Input: node with value 1 and neighbors [2, 3]
Output: cloned node with value 1 and neighbors [cloned 2, cloned 3]
```

## Key Takeaways
- Use DFS to traverse the graph and clone each node.
- Utilize an unordered map to store the cloned nodes to avoid cloning the same node multiple times.
- Recursively clone the neighbors of each node.