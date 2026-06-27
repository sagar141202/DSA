# Clone Graph

## Problem Statement
Clone an undirected graph, given as a Node object with a val and a list of its neighbors. Each Node has a unique val and a list of its neighbors. The graph is not guaranteed to be connected. The input graph will only contain unique Node values (i.e., no duplicate values). The nodes are numbered from 1 to N, where N is the number of nodes in the graph. The graph is represented as a map where the key is the node number and the value is a list of neighboring nodes. The function should return the cloned graph, with the same node values and the same neighbors. For example, if we have a graph with two nodes, 1 and 2, where node 1 is connected to node 2, and node 2 is connected to node 1, the cloned graph should also have two nodes, 1 and 2, where node 1 is connected to node 2, and node 2 is connected to node 1.

## Approach
The approach to solve this problem is to use a depth-first search (DFS) algorithm to traverse the graph and clone each node. We will use a hash map to store the cloned nodes to avoid cloning the same node multiple times. We will start the DFS from each unvisited node to handle disconnected graphs.

## Complexity
- Time: O(N + M)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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
Input: [[2],[1]]
Output: [[2],[1]]
Input: [[]]
Output: [[]]
Input: []
Output: []
```

## Key Takeaways
- Use DFS to traverse the graph and clone each node.
- Use a hash map to store the cloned nodes to avoid cloning the same node multiple times.
- Handle disconnected graphs by starting the DFS from each unvisited node.