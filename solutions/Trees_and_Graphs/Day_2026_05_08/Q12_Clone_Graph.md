# Clone Graph

## Problem Statement
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. Create a deep copy of the graph, including all nodes and their neighbors. The nodes in the first graph contain a label and a list of their neighbors. The nodes in the second graph should have the same values of labels and the same structure of neighbors. The returned node should be the start of the deep copy of the graph. The graph is represented as a map where each key is a node label and each value is a list of all the nodes that the key/node is connected to. The graph only contains only positive nodes and there is only one node with a certain label. There are no duplicate edges in the graph. 1 <= Node number <= 100, 1 <= edge number <= 500, 1 <= label <= 100.

## Approach
The solution uses a depth-first search (DFS) approach to traverse the graph and clone each node. It utilizes an unordered map to store the cloned nodes and avoid cloning the same node multiple times. The algorithm starts by checking if the node is already cloned, and if so, returns the cloned node. If not, it creates a new node, adds it to the map, and recursively clones its neighbors.

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
        if (!node) return NULL;
        unordered_map<Node*, Node*> map;
        return dfs(node, map);
    }
    
    Node* dfs(Node* node, unordered_map<Node*, Node*>& map) {
        if (map.count(node)) return map[node];
        Node* clone = new Node(node->val);
        map[node] = clone;
        for (Node* neighbor : node->neighbors) {
            clone->neighbors.push_back(dfs(neighbor, map));
        }
        return clone;
    }
};
```

## Test Cases
```
Input: [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
```

## Key Takeaways
- Use DFS to traverse the graph and clone each node.
- Utilize an unordered map to store the cloned nodes and avoid cloning the same node multiple times.
- Recursively clone the neighbors of each node.