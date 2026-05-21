# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors. The number of nodes in the graph is in the range [0, 100] for each test case. There is no repeated value for each node (i.e., the node values are unique). You may assume the input node is never null. The graph is represented in such a way that each node value is the same as the index of that node in the call to the cloneGraph function (0-indexed). For example, the input for the graph {1,2,2} will be node 1(1,2,2) -> {2,2,1}. For the graph {3,0,6,1,5}, the input for the cloneGraph function will be node 3(3,0,6,1,5) -> {3,0,6,1,5}.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the graph and clone each node. It utilizes a hash map to store the cloned nodes to avoid cloning the same node multiple times. The algorithm starts by cloning the given node, then recursively clones its neighbors.

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
        
        // Create a hash map to store the cloned nodes
        unordered_map<int, Node*> clonedNodes;
        
        return cloneNode(node, clonedNodes);
    }
    
    Node* cloneNode(Node* node, unordered_map<int, Node*>& clonedNodes) {
        // If the node is already cloned, return the cloned node
        if (clonedNodes.find(node->val) != clonedNodes.end()) {
            return clonedNodes[node->val];
        }
        
        // Clone the node
        Node* clonedNode = new Node(node->val);
        clonedNodes[node->val] = clonedNode;
        
        // Clone the neighbors
        for (Node* neighbor : node->neighbors) {
            clonedNode->neighbors.push_back(cloneNode(neighbor, clonedNodes));
        }
        
        return clonedNode;
    }
};
```

## Test Cases
```
Input: node with value 1 and neighbors [node with value 2, node with value 3]
Output: cloned node with value 1 and neighbors [cloned node with value 2, cloned node with value 3]
```

## Key Takeaways
- Use a hash map to store the cloned nodes to avoid cloning the same node multiple times.
- Utilize a DFS approach to traverse the graph and clone each node.
- Clone the neighbors of each node recursively.