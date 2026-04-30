# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors. The original graph is given at the input of the function cloneGraph(Node* node) where node is a pointer to a node of the graph. The node.val will be between 1 and 100 for undirected graph. The number of nodes will not exceed 100 for undirected graph. There is no repeated edges and no self-loops in the graph.

## Approach
The approach involves using a depth-first search (DFS) algorithm to traverse the graph, and a hash map to store the visited nodes and their clones. This way, we can avoid revisiting the same node and reduce the time complexity.

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
Input: [[2,1],[1,2]]
Output: [[2,1],[1,2]]
Input: [[2],[1]]
Output: [[2],[1]]
```

## Key Takeaways
- We use DFS to traverse the graph and clone each node.
- We use a hash map to store the visited nodes and their clones to avoid revisiting the same node.
- The time complexity is O(N + M) where N is the number of nodes and M is the number of edges.