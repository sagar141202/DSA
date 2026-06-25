# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. The task is to create a deep copy of the linked list, ensuring that the new list has the same structure and connections as the original list. The nodes in the new list should not be the same as the nodes in the original list, but they should have the same values and connections. For example, if we have a list `1 -> 2 -> 3` with random pointers `1 -> 3` and `2 -> 1` and `3 -> 2`, the new list should also have the same structure and connections.

## Approach
We will use a hash map to store the mapping of old nodes to new nodes, then iterate through the list to create new nodes and update their next and random pointers. This approach allows us to efficiently keep track of the new nodes and their connections.

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
        // Create a hashmap to store the mapping of old nodes to new nodes
        unordered_map<Node*, Node*> map;
        
        // Iterate through the list to create new nodes
        Node* old = head;
        Node* newHead = NULL;
        Node* newTail = NULL;
        while (old) {
            // Create a new node
            Node* newNode = new Node(old->val);
            
            // Add the new node to the map
            map[old] = newNode;
            
            // If this is the first node, set it as the new head
            if (!newHead) {
                newHead = newNode;
                newTail = newNode;
            } else {
                // Otherwise, connect the new node to the previous new node
                newTail->next = newNode;
                newTail = newNode;
            }
            
            // Move to the next old node
            old = old->next;
        }
        
        // Iterate through the list again to update the random pointers
        old = head;
        Node* newCurrent = newHead;
        while (old) {
            // If the old node has a random pointer, update the new node's random pointer
            if (old->random) {
                newCurrent->random = map[old->random];
            }
            
            // Move to the next old node and the next new node
            old = old->next;
            newCurrent = newCurrent->next;
        }
        
        // Return the new head
        return newHead;
    }
};
```

## Test Cases
```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

## Key Takeaways
- Use a hash map to store the mapping of old nodes to new nodes to efficiently keep track of the new nodes and their connections.
- Iterate through the list twice: once to create new nodes and once to update the random pointers.
- Make sure to handle the case where the random pointer points to a node that has not been created yet.