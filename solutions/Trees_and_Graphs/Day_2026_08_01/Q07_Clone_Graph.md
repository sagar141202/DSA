# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors. The given node will always be in the graph and will never be null. The number of nodes in the graph is in the range [1, 100] for each test case. The values of the nodes are in the range [1, 100]. The edges of the graph are in the range [1, 100] for each test case. The graph is guaranteed to be connected.

## Approach
To clone the graph, we can use a depth-first search (DFS) approach to traverse the graph and create a copy of each node. We will use a hashmap to store the copied nodes to avoid creating duplicate copies.

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
        unordered_map<Node*, Node*> visited;
        return dfs(node, visited);
    }
    
    Node* dfs(Node* node, unordered_map<Node*, Node*>& visited) {
        if (visited.count(node)) return visited[node];
        Node* clone = new Node(node->val);
        visited[node] = clone;
        for (Node* neighbor : node->neighbors) {
            clone->neighbors.push_back(dfs(neighbor, visited));
        }
        return clone;
    }
};
```

## Test Cases
```
Input: [[2,1],[1,2]]
Output: [[2,1],[1,2]]
```

## Key Takeaways
- Use DFS to traverse the graph and create a copy of each node.
- Use a hashmap to store the copied nodes to avoid creating duplicate copies.
- The time complexity is O(N + M) where N is the number of nodes and M is the number of edges.