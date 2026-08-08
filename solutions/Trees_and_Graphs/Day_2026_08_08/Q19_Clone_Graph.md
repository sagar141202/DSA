# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors. The given node will always be in the graph and will never be null. The number of nodes in the graph is in the range [1, 100] for each test case. The nodes' values are in the range [1, 100]. Each node's neighbors are in the range [0, 100] for each test case. The graph is guaranteed to be connected.

## Approach
The solution involves using a depth-first search (DFS) to traverse the graph and create clones of each node. We use a hash map to store the clones of visited nodes to avoid revisiting them.

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
Input: Node with value 1 and neighbors [2, 3]
Output: Clone of the input graph
```

## Key Takeaways
- Use DFS to traverse the graph and create clones of each node.
- Utilize a hash map to store the clones of visited nodes to avoid revisiting them.
- Create a new clone for each unvisited node and add its neighbors recursively.