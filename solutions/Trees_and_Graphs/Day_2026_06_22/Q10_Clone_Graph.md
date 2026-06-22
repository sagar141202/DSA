# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors. The nodes are numbered from 1 to N, where N is the number of nodes in the graph. For a given node, neighbors is a list of node values such that node i is a neighbor of the given node. The graph is represented as a map where each key is a node and its corresponding value is a list of its neighbors. The function should return a reference to the cloned node of the given node. The graph is guaranteed to be connected and undirected, but it may contain cycles.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the graph and clone each node. It utilizes an unordered map to store the cloned nodes to avoid cloning the same node multiple times. The DFS function recursively clones the neighbors of each node.

## Complexity
- Time: O(N + M)
- Space: O(N)

## C++ Solution
```cpp
#include <unordered_map>
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
        if (cloned.find(node) != cloned.end()) {
            return cloned[node];
        }
        
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
Input: node with value 1 and neighbors [node with value 2, node with value 3]
Output: cloned node with value 1 and neighbors [cloned node with value 2, cloned node with value 3]
```

## Key Takeaways
- Use an unordered map to store the cloned nodes to avoid cloning the same node multiple times.
- Utilize a depth-first search (DFS) approach to traverse the graph and clone each node.
- Recursively clone the neighbors of each node to ensure all nodes are cloned correctly.