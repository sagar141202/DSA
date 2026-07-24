# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors. The given node will always be in the graph and unique. The number of nodes in the graph is in the range [1, 100] for each test case, and 1 <= Node.val <= 100. The edges of the graph are undirected and may contain cycles.

## Approach
We will use a depth-first search (DFS) approach to traverse the graph and clone each node. We will also use an unordered map to store the cloned nodes to avoid cloning the same node multiple times.

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
    unordered_map<Node*, Node*> visited;
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        if (visited.find(node) != visited.end()) return visited[node];
        
        Node* clone = new Node(node->val);
        visited[node] = clone;
        
        for (Node* neighbor : node->neighbors) {
            clone->neighbors.push_back(cloneGraph(neighbor));
        }
        
        return clone;
    }
};
```

## Test Cases
```
Input: [[2,1]], Node with label 1 connected to Node with label 2
Output: [[2,1]], Node with label 1 connected to Node with label 2
```

## Key Takeaways
- Use DFS to traverse the graph and clone each node.
- Use an unordered map to store the cloned nodes to avoid cloning the same node multiple times.
- The time complexity is O(N + M) where N is the number of nodes and M is the number of edges in the graph.