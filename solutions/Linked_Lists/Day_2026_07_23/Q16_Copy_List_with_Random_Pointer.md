# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. The task is to create a deep copy of the given linked list. The given linked list contains nodes with integer values and a random pointer. The constraints are that each node has a unique integer value. For example, if we have a list with nodes having values 1, 2, and 3, and node 1 points to node 3, and node 2 points to node 1, then the copied list should also have the same structure and relationships.

## Approach
We will use a hashmap to store the mapping of original nodes to their copies. Then we will traverse the original list and for each node, create a copy and store it in the hashmap. After that, we will traverse the list again to set the next and random pointers of the copied nodes.

## Complexity
- Time: O(n)
- Space: O(n)

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

        // Create a hashmap to store the mapping of original nodes to their copies
        unordered_map<Node*, Node*> hashmap;
        
        // Traverse the original list and create a copy of each node
        Node* original = head;
        while (original) {
            hashmap[original] = new Node(original->val);
            original = original->next;
        }
        
        // Traverse the list again to set the next and random pointers of the copied nodes
        original = head;
        while (original) {
            if (original->next) hashmap[original]->next = hashmap[original->next];
            if (original->random) hashmap[original]->random = hashmap[original->random];
            original = original->next;
        }
        
        // Return the head of the copied list
        return hashmap[head];
    }
};
```

## Test Cases
```
Input: 
    Node 1 -> Node 2
    Node 1 -> Node 2 (random)
    Node 2 -> Node 3
    Node 2 -> Node 1 (random)
Output: 
    Copied Node 1 -> Copied Node 2
    Copied Node 1 -> Copied Node 2 (random)
    Copied Node 2 -> Copied Node 3
    Copied Node 2 -> Copied Node 1 (random)
```

## Key Takeaways
- Use a hashmap to store the mapping of original nodes to their copies.
- Traverse the original list twice to create copies and set the next and random pointers.
- The time complexity is O(n) where n is the number of nodes in the list.