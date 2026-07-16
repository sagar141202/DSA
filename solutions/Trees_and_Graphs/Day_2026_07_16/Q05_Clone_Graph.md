# Clone Graph

## Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors. The number of nodes in the graph is in the range [0, 100] for each test case. There is no repeated val value for each node in the graph. In other words, for any two nodes x and y, if x.val == y.val, then they must be the same node. For the given node, each of its neighbors must already exist in the graph, with no duplicates.

## Approach
We can solve this problem by using a depth-first search (DFS) approach and storing the visited nodes in a hashmap to avoid revisiting them. We create a new node for each visited node and add its neighbors to the new node. This approach ensures that each node is visited only once and its neighbors are correctly added to the cloned graph.

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
        
        unordered_map<Node*, Node*> visited;
        return dfs(node, visited);
    }
    
    Node* dfs(Node* node, unordered_map<Node*, Node*>& visited) {
        if (visited.count(node)) return visited[node];
        
        Node* newNode = new Node(node->val);
        visited[node] = newNode;
        
        for (Node* neighbor : node->neighbors) {
            newNode->neighbors.push_back(dfs(neighbor, visited));
        }
        
        return newNode;
    }
};
```

## Test Cases
```
Input: [[2,1],[1,2]]
Output: [[2,1],[1,2]]
```

## Key Takeaways
- Use a hashmap to store the visited nodes to avoid revisiting them.
- Create a new node for each visited node and add its neighbors to the new node.
- Use DFS to traverse the graph and clone each node.