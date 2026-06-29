# Clone Graph

## Problem Statement
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. A new node will be created with the same properties and connections as the original node. The nodes are labeled uniquely. The given node is a node from the original graph. The nodes in the given graph are labeled from 1 to n, where n is the number of nodes in the graph. The edges in the graph are undirected, and there are no multiple edges between any two nodes. The graph is connected, and it is not guaranteed that all nodes are reachable from the given node. The graph does not contain cycles. The number of nodes in the graph is between 1 and 100. The number of edges in the graph is between 1 and 500. The label of each node is between 1 and n, where n is the number of nodes in the graph. The neighbors of each node are given as a list of node labels.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the graph and clone each node. It uses an unordered map to store the cloned nodes to avoid cloning the same node multiple times. The DFS function is used recursively to clone the neighbors of each node.

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
        return clone(node, cloned);
    }
    
    Node* clone(Node* node, unordered_map<Node*, Node*>& cloned) {
        if (cloned.find(node) != cloned.end()) return cloned[node];
        Node* newNode = new Node(node->val);
        cloned[node] = newNode;
        for (Node* neighbor : node->neighbors) {
            newNode->neighbors.push_back(clone(neighbor, cloned));
        }
        return newNode;
    }
};
```

## Test Cases
```
Input: [[2,1],[1,2]]
Output: [[2,1],[1,2]]
```

## Key Takeaways
- Use DFS to traverse the graph and clone each node.
- Use an unordered map to store the cloned nodes to avoid cloning the same node multiple times.
- Recursively clone the neighbors of each node using the DFS function.