# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors. The number of nodes in the graph is between 1 and 100, and each node has a unique value between 1 and 100. The graph is represented as an adjacency list where each index in the list represents a node, and a node at index i has a neighbor at index j if there is an edge between them. The edge is undirected, meaning if there is an edge between node i and node j, then there is an edge between node j and node i.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the graph and create a deep copy of each node. It utilizes a hashmap to store the nodes that have been visited to avoid infinite loops. The DFS function is called recursively for each neighbor of the current node.

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
        unordered_map<Node*, Node*> visited;
        return dfs(node, visited);
    }
    
    Node* dfs(Node* node, unordered_map<Node*, Node*>& visited) {
        if (visited.find(node) != visited.end()) return visited[node];
        Node* clone = new Node(node->val);
        visited[node] = clone;
        for (auto neighbor : node->neighbors) {
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
- Use a hashmap to store visited nodes and avoid infinite loops.
- Utilize DFS to traverse the graph and create a deep copy of each node.
- Create a new node for each visited node and store its neighbors recursively.