# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors. The given node will always be in the graph and will never be null. The number of nodes in the graph is in the range [1, 100] for each test case. There are no repeated nodes in the graph and no self-loops (i.e., a node cannot have an edge to itself). The edge list of each node will only contain unique edges to other nodes.

## Approach
To clone the graph, we can use a depth-first search (DFS) or breadth-first search (BFS) algorithm to traverse the original graph and create a copy of each node and its neighbors. We will use an unordered map to keep track of the cloned nodes to avoid cloning the same node multiple times.

## Complexity
- Time: O(N + M), where N is the number of nodes and M is the number of edges in the graph.
- Space: O(N), where N is the number of nodes in the graph.

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
        return clone(node, cloned);
    }
    
    Node* clone(Node* node, unordered_map<Node*, Node*>& cloned) {
        if (cloned.count(node)) return cloned[node];
        Node* newNode = new Node(node->val);
        cloned[node] = newNode;
        for (Node* neighbor : node->neighbors) {
            newNode->neighbors.push_back(clone(neighbor, cloned));
        }
        return newNode;
    }
};
```

## Test Cases
```
Input: node with value 1 and neighbors 2 and 3
Output: cloned node with value 1 and neighbors 2 and 3
```

## Key Takeaways
- Use an unordered map to keep track of the cloned nodes to avoid cloning the same node multiple times.
- Use a recursive DFS or BFS algorithm to traverse the original graph and create a copy of each node and its neighbors.
- The time complexity is O(N + M), where N is the number of nodes and M is the number of edges in the graph, because we visit each node and edge once.