# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors. The number of nodes in the graph is in the range [1, 100] for each test case. The node val is in the range [1, 100] for each test case. The graph is guaranteed to be connected and undirected. The graph may contain cycles. There are no duplicate edges in the graph. The graph may contain self-loops. 

## Approach
To solve this problem, we will use a depth-first search (DFS) algorithm to traverse the graph and create a copy of each node. We will also use an unordered map to keep track of the nodes that have already been cloned. This will help us avoid infinite loops in case the graph contains cycles.

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
        
        unordered_map<Node*, Node*> clones;
        return clone(node, clones);
    }
    
    Node* clone(Node* node, unordered_map<Node*, Node*>& clones) {
        if (clones.find(node) != clones.end()) return clones[node];
        
        Node* cloneNode = new Node(node->val);
        clones[node] = cloneNode;
        
        for (Node* neighbor : node->neighbors) {
            cloneNode->neighbors.push_back(clone(neighbor, clones));
        }
        
        return cloneNode;
    }
};
```

## Test Cases
```
Input: [[2,1],[1,2]]
Output: [[2,1],[1,2]]
```

## Key Takeaways
- To clone a graph, we need to create a copy of each node and its neighbors.
- We can use DFS to traverse the graph and clone each node.
- We need to keep track of the nodes that have already been cloned to avoid infinite loops in case the graph contains cycles.