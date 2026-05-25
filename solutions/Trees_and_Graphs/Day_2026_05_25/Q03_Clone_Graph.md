# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors. The given node will always be in the graph and it will always be a single node with val 1. The graph will always be connected. The number of nodes in the graph will not exceed 100.

## Approach
We can solve this problem by using a depth-first search (DFS) algorithm to traverse the graph and create a copy of each node. We will use a hashmap to store the nodes we have already visited to avoid infinite loops. The DFS function will recursively visit each neighbor of a node and create a copy of it if it has not been visited before.

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
        
        unordered_map<Node*, Node*> visited;
        
        return dfs(node, visited);
    }
    
    Node* dfs(Node* node, unordered_map<Node*, Node*>& visited) {
        if (visited.find(node) != visited.end()) {
            return visited[node];
        }
        
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
- Use a hashmap to store the nodes we have already visited to avoid infinite loops.
- Use a depth-first search algorithm to traverse the graph and create a copy of each node.
- Create a new node for each unvisited node and add its neighbors recursively.