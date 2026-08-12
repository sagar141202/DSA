# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors. The nodes are numbered from 1 to N, and their values are from 1 to N. Each node has a unique value, and there are no duplicate edges or self-loops in the graph. The graph is connected and undirected, meaning that the edges between nodes are bidirectional. The graph is represented using an adjacency list, where each index in the list represents a node, and the value at each index is a list of the node's neighbors. For example, if the graph has three nodes with values 1, 2, and 3, and the edges are between nodes 1 and 2, and nodes 2 and 3, the graph can be represented as: [[2],[1,3],[2]].

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the graph and clone each node. It utilizes a hashmap to store the cloned nodes to avoid cloning the same node multiple times. The DFS function is used recursively to clone the neighbors of each node.

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
Input: [[2],[1,3],[2]]
Output: [[2],[1,3],[2]]
```

## Key Takeaways
- Use a hashmap to store the cloned nodes to avoid cloning the same node multiple times.
- Utilize a depth-first search (DFS) approach to traverse the graph and clone each node.
- The time complexity is O(N + M), where N is the number of nodes and M is the number of edges.