# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. Create a deep copy of the original list. The list has the following definition for its nodes: 
```cpp
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
```
The constraints are that we cannot modify the original list, and we should minimize extra space. An example is when the input is a list with three nodes where the first node points to the second node, the second node points to the third node, and the third node's random pointer points to the first node.

## Approach
We can solve this problem by using a hash map to store the nodes of the original list as we create new nodes for the copied list. This allows us to keep track of which nodes we have already created and to correctly set the random pointers of the new nodes.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return NULL;
        
        // Create a hash map to store the nodes
        unordered_map<Node*, Node*> map;
        
        // Create a new node for each node in the original list
        Node* curr = head;
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        // Set the next and random pointers for the new nodes
        curr = head;
        while (curr) {
            if (curr->next) map[curr]->next = map[curr->next];
            if (curr->random) map[curr]->random = map[curr->random];
            curr = curr->next;
        }
        
        return map[head];
    }
};
```

## Test Cases
```
Input: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

## Key Takeaways
- We use a hash map to keep track of the nodes we have already created.
- We create new nodes for the copied list in two passes: one to create the nodes and one to set the next and random pointers.
- This approach has a time complexity of O(N) and a space complexity of O(N), where N is the number of nodes in the original list.