# Clone Graph

## Problem Statement
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. Create a deep copy of the graph so that all of the nodes are copied and the neighbors of the copied nodes are also copied. The labels of the nodes are integers from 1 to n, where n is the number of nodes. There are no duplicate labels. The graph is connected and undirected. The input is a node of the graph, and the output should be a node of the cloned graph. For example, if we have a graph with two nodes, 1 and 2, where node 1 is connected to node 2, the cloned graph should also have two nodes, 1 and 2, where node 1 is connected to node 2.

## Approach
The approach to solve this problem is to use a depth-first search (DFS) algorithm to traverse the graph and clone each node. We will use an unordered map to store the cloned nodes to avoid cloning the same node multiple times.

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
Input: Node with value 1 and neighbors [Node with value 2, Node with value 3]
Output: Cloned Node with value 1 and neighbors [Cloned Node with value 2, Cloned Node with value 3]
```

## Key Takeaways
- Use DFS to traverse the graph and clone each node.
- Use an unordered map to store the cloned nodes and avoid cloning the same node multiple times.
- The time complexity is O(N + M) where N is the number of nodes and M is the number of edges.