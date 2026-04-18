# Clone Graph

## Problem Statement
Clone an undirected graph. The graph is represented as a map where each key is a node and its corresponding value is a list of its neighbors. Given a reference of a node in the graph, return a deep copy of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors. The number of nodes in the graph is in the range [0, 100] for each test case. There is no repeated val value for each node in the graph. In other words, no two nodes have the same value. For any node that has neighbors, the neighbors will be a non-empty list. The graph is guaranteed to be undirected, meaning that if node u has a neighbor v, then node v will also have a neighbor u.

## Approach
We can solve this problem by using a depth-first search (DFS) or breadth-first search (BFS) algorithm to traverse the graph and clone each node. We will use an unordered map to store the cloned nodes to avoid cloning the same node multiple times.

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
        
        unordered_map<Node*, Node*> cloneMap;
        
        return clone(node, cloneMap);
    }
    
    Node* clone(Node* node, unordered_map<Node*, Node*>& cloneMap) {
        if (cloneMap.find(node) != cloneMap.end()) {
            return cloneMap[node];
        }
        
        Node* newNode = new Node(node->val);
        cloneMap[node] = newNode;
        
        for (Node* neighbor : node->neighbors) {
            newNode->neighbors.push_back(clone(neighbor, cloneMap));
        }
        
        return newNode;
    }
};
```

## Test Cases
```
Input: node with val 1 and neighbors [node with val 2, node with val 3]
Output: cloned node with val 1 and neighbors [cloned node with val 2, cloned node with val 3]
```

## Key Takeaways
- Use DFS or BFS to traverse the graph and clone each node.
- Use an unordered map to store the cloned nodes to avoid cloning the same node multiple times.
- The time complexity is O(N + M) where N is the number of nodes and M is the number of edges in the graph.