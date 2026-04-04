# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors. The given node will always be in the graph and will never be null. The number of nodes in the graph is in the range [1, 100] for each test case. Each node has a unique value from 1 to 100. The undirected graph is represented as a graph where the nodes are numbered from 1 to N, and there is an edge between nodes i and j if and only if the absolute difference between i and j is 1.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the graph and clone each node. It utilizes a hashmap to store the cloned nodes to avoid cloning the same node multiple times. The DFS function is called recursively for each neighbor of the current node.

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
Input: node with value 1 and neighbors [2, 3]
Output: cloned node with value 1 and neighbors [cloned 2, cloned 3]
```

## Key Takeaways
- Use a hashmap to store the cloned nodes to avoid cloning the same node multiple times.
- Utilize a DFS approach to traverse the graph and clone each node.
- The cloned graph will have the same structure and values as the original graph.