# Clone Graph

## Problem Statement
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. Create a deep copy of the graph, meaning that all nodes and edges are copied. The nodes are labeled from 1 to n, and for each node, the neighbors are given as a list of node labels. The graph is guaranteed to be connected and undirected. For example, given a graph with the following nodes and edges: Node 1 -> Node 2, Node 1 -> Node 3, Node 2 -> Node 4, Node 3 -> Node 4, the cloned graph should have the same structure and connections.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the graph and clone each node. It utilizes a hashmap to store the cloned nodes to avoid revisiting them. The DFS function recursively clones the neighbors of each node.

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
Input: Node 1 -> Node 2, Node 1 -> Node 3, Node 2 -> Node 4, Node 3 -> Node 4
Output: Cloned graph with the same structure and connections
```

## Key Takeaways
- Use a hashmap to store the cloned nodes to avoid revisiting them.
- Utilize a DFS approach to traverse the graph and clone each node.
- The time complexity is O(N + M), where N is the number of nodes and M is the number of edges.