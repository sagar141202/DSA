# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors. The given node will always be in the graph and will never be null. The number of nodes in the graph is in the range [1, 100] for each test case. 1 <= Node.val <= 100. Node.neighors is a list of Node objects.

## Approach
We can use a depth-first search (DFS) or breadth-first search (BFS) algorithm to traverse the graph and clone each node. We will use an unordered_map to store the cloned nodes to avoid cloning the same node multiple times.

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
        if (cloned.count(node)) return cloned[node];
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
Input: [[2,1],[1,2]]
Output: [[2,1],[1,2]]
```

## Key Takeaways
- Use DFS or BFS to traverse the graph and clone each node.
- Use an unordered_map to store the cloned nodes to avoid cloning the same node multiple times.
- Be careful with the memory management when cloning the nodes.