# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors. The deep copy should have the same structure and node values as the original graph.

## Approach
The approach involves using a depth-first search (DFS) to traverse the graph and clone each node. We will use a hash map to keep track of the cloned nodes to avoid cloning the same node multiple times. The algorithm will recursively clone the neighbors of each node.

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
        
        // Create a hash map to store the cloned nodes
        unordered_map<Node*, Node*> cloneMap;
        
        // Perform DFS to clone the graph
        return dfs(node, cloneMap);
    }
    
    Node* dfs(Node* node, unordered_map<Node*, Node*>& cloneMap) {
        // If the node is already cloned, return the cloned node
        if (cloneMap.find(node) != cloneMap.end()) {
            return cloneMap[node];
        }
        
        // Clone the node
        Node* clone = new Node(node->val);
        cloneMap[node] = clone;
        
        // Clone the neighbors
        for (Node* neighbor : node->neighbors) {
            clone->neighbors.push_back(dfs(neighbor, cloneMap));
        }
        
        return clone;
    }
};
```

## Test Cases
```
Input: 
     1
   / | \
  2  3  4
 / \
5   6

Output: 
     1
   / | \
  2  3  4
 / \
5   6
```

## Key Takeaways
- Use a hash map to keep track of the cloned nodes to avoid cloning the same node multiple times.
- Perform DFS to traverse the graph and clone each node.
- Recursively clone the neighbors of each node to maintain the graph structure.