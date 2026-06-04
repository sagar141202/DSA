# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors. The underlying graph can be traversed using DFS or BFS, but the solution should not depend on this. The graph is represented as a map where each key is a node and its corresponding value is a list of its neighbors. The task is to create a new graph that is a clone of the original graph. For example, if we have a graph with three nodes (1, 2, 3) where node 1 is connected to nodes 2 and 3, and node 2 is connected to node 3, the clone of this graph should have the same structure and connections.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the graph and create a clone of each node. It utilizes a hash map to store the cloned nodes to avoid redundant cloning. The DFS traversal ensures that all nodes and their neighbors are visited and cloned.

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
        
        unordered_map<Node*, Node*> clonedNodes;
        
        return dfs(node, clonedNodes);
    }
    
    Node* dfs(Node* node, unordered_map<Node*, Node*>& clonedNodes) {
        if (clonedNodes.find(node) != clonedNodes.end()) {
            return clonedNodes[node];
        }
        
        Node* clonedNode = new Node(node->val);
        clonedNodes[node] = clonedNode;
        
        for (Node* neighbor : node->neighbors) {
            clonedNode->neighbors.push_back(dfs(neighbor, clonedNodes));
        }
        
        return clonedNode;
    }
};
```

## Test Cases
```
Input: node with val = 1 and neighbors = [node with val = 2, node with val = 3]
Output: cloned node with val = 1 and neighbors = [cloned node with val = 2, cloned node with val = 3]
```

## Key Takeaways
- Use DFS to traverse the graph and clone each node.
- Utilize a hash map to store the cloned nodes to avoid redundant cloning.
- The time complexity is O(N + M), where N is the number of nodes and M is the number of edges.