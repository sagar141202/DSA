# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors. The given node will always be in the graph and will never be null. The number of nodes in the graph is in the range [1, 100] for each test case. There are no duplicate values in the graph, and the values of the nodes are between 1 and 100 for each test case.

## Approach
We will use a Depth-First Search (DFS) approach to traverse the graph and clone each node. We will also use an unordered map to keep track of the cloned nodes to avoid cloning the same node multiple times. The DFS will recursively clone the neighbors of each node.

## Complexity
- Time: O(N + M), where N is the number of nodes and M is the number of edges in the graph.
- Space: O(N), where N is the number of nodes in the graph.

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
        if (cloned.find(node) != cloned.end()) {
            return cloned[node];
        }
        Node* clonedNode = new Node(node->val);
        cloned[node] = clonedNode;
        for (Node* neighbor : node->neighbors) {
            clonedNode->neighbors.push_back(clone(neighbor, cloned));
        }
        return clonedNode;
    }
};
```

## Test Cases
```
Input: Node with value 1 and neighbors [Node with value 2, Node with value 3]
Output: Cloned Node with value 1 and neighbors [Cloned Node with value 2, Cloned Node with value 3]
```

## Key Takeaways
- Use DFS to traverse the graph and clone each node.
- Use an unordered map to keep track of the cloned nodes to avoid cloning the same node multiple times.
- Recursively clone the neighbors of each node.