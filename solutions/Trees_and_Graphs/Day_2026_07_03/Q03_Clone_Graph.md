# Clone Graph

## Problem Statement
Clone an undirected graph, where each node contains a label (int) and a list (list<Node>) of its neighbors. The task is to create a deep copy of the given graph, i.e., create a new graph with the same nodes and edges as the original graph. The nodes in the new graph should be different from the original nodes, but they should have the same values (labels) and the same neighbors. The given graph is represented as a list of nodes, where each node is a reference to a node object. The node object has two attributes: val (an integer representing the node's label) and neighbors (a list of node objects representing the node's neighbors). The graph is guaranteed to be connected and undirected.

## Approach
The approach to solve this problem is to use a depth-first search (DFS) algorithm to traverse the graph and create a copy of each node. We will use a hashmap to store the nodes we have already visited to avoid infinite loops. We will recursively call the DFS function for each neighbor of the current node.

## Complexity
- Time: O(N + M), where N is the number of nodes and M is the number of edges
- Space: O(N), where N is the number of nodes

## C++ Solution
```cpp
/*
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
*/
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        unordered_map<Node*, Node*> visited;
        return dfs(node, visited);
    }
    
    Node* dfs(Node* node, unordered_map<Node*, Node*>& visited) {
        if (visited.count(node)) return visited[node];
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
```

## Key Takeaways
- Use a hashmap to store the visited nodes to avoid infinite loops.
- Use DFS to traverse the graph and create a copy of each node.
- Recursively call the DFS function for each neighbor of the current node.