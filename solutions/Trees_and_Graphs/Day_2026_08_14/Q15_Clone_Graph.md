# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors. The nodes are numbered from 1 to N, where N is the number of nodes in the graph. The graph is represented as an adjacency list where each index i in the list represents a node and each value at index i is a list of node indices that node i is connected to. The graph does not contain any duplicate edges or self-edges. The number of nodes in the graph is in the range [1, 100] for each test case. The val of each node is in the range [1, 100]. It is guaranteed that the input graph is connected.

## Approach
To clone the graph, we can use a depth-first search (DFS) approach to traverse the original graph and create a deep copy of each node. We will use a hashmap to store the cloned nodes to avoid cloning the same node multiple times. The algorithm will start at the given node and recursively clone its neighbors.

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
        unordered_map<Node*, Node*> cloned;
        return clone(node, cloned);
    }
    
    Node* clone(Node* node, unordered_map<Node*, Node*>& cloned) {
        if (cloned.find(node) != cloned.end()) return cloned[node];
        Node* cloneNode = new Node(node->val);
        cloned[node] = cloneNode;
        for (Node* neighbor : node->neighbors) {
            cloneNode->neighbors.push_back(clone(neighbor, cloned));
        }
        return cloneNode;
    }
};
```

## Test Cases
```
Input: [[2, 1], [1, 2]]
Output: [[2, 1], [1, 2]]
```

## Key Takeaways
- Use a hashmap to store the cloned nodes to avoid cloning the same node multiple times.
- Use DFS to traverse the original graph and create a deep copy of each node.
- The time complexity is O(N + M) where N is the number of nodes and M is the number of edges in the graph.