# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors. The nodes are numbered from 1 to N, where N is the number of nodes in the graph. The graph is represented as a map where each key is a node and its corresponding value is a list of its neighbors. The constraints are: 1 <= N <= 100, 1 <= Node.val <= 100, Node.neighbor.length == the number of neighbors of Node, 0 <= Edge.length <= N - 1, and Edges[i] is a valid edge between two nodes with different values. For example, if we have a graph with nodes 1, 2, and 3 where node 1 is connected to nodes 2 and 3, and node 2 is connected to node 3, then the clone of this graph should also have the same structure and connections.

## Approach
The approach is to use a depth-first search (DFS) traversal to clone the graph. We will create a new node for each node we visit and add its neighbors to the new node. We will use a hashmap to store the mapping of the original nodes to the cloned nodes.

## Complexity
- Time: O(N + M)
- Space: O(N)

## C++ Solution
```cpp
#include <unordered_map>
#include <vector>

class Node {
public:
    int val;
    std::vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = {};
    }
    Node(int _val) {
        val = _val;
        neighbors = {};
    }
    Node(int _val, std::vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        std::unordered_map<Node*, Node*> visited;
        return dfs(node, visited);
    }
    
    Node* dfs(Node* node, std::unordered_map<Node*, Node*>& visited) {
        if (visited.find(node) != visited.end()) return visited[node];
        Node* newNode = new Node(node->val, {});
        visited[node] = newNode;
        for (auto neighbor : node->neighbors) {
            newNode->neighbors.push_back(dfs(neighbor, visited));
        }
        return newNode;
    }
};
```

## Test Cases
```
Input: Node with value 1 and neighbors [Node with value 2, Node with value 3]
Output: New Node with value 1 and neighbors [New Node with value 2, New Node with value 3]
```

## Key Takeaways
- Use DFS traversal to clone the graph.
- Create a new node for each node we visit and add its neighbors to the new node.
- Use a hashmap to store the mapping of the original nodes to the cloned nodes.