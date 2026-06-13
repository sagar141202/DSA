# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors. The given node will always be in the graph and the graph will always be connected. The number of nodes in the graph will not exceed 100. The nodes' values will be between 1 and 100. The graph is represented as a dictionary where each key is a node and its corresponding value is a list of its neighbors.

## Approach
We can solve this problem using Depth-First Search (DFS) or Breadth-First Search (BFS) to traverse the graph and create a copy of each node. We will use a hash map to store the mapping between the original nodes and their clones.

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
Input: [[2, 1], [1, 2]]
Output: [[2, 1], [1, 2]]
```

## Key Takeaways
- Create a hash map to store the mapping between the original nodes and their clones.
- Use DFS or BFS to traverse the graph and create a copy of each node.
- Use the hash map to avoid creating duplicate clones of the same node.