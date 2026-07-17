# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an integer value and a random pointer to any other node in the list (including itself). Create a deep copy of the original list. The deep copy should have the same structure and values as the original list, but it should not share any nodes with the original list. The function should take the head of the original list as input and return the head of the copied list. The nodes in the list should have the following structure: `Node(val, next, random)`, where `val` is the node's value, `next` is a pointer to the next node, and `random` is a pointer to a random node.

## Approach
Create a hashmap to store the mapping of original nodes to their copies. Iterate over the original list to create copies of each node and store them in the hashmap. Then, iterate over the original list again to set the `next` and `random` pointers of each copied node. This approach ensures that each node is copied only once and that the `next` and `random` pointers are correctly set.

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
        // Create a hashmap to store the mapping of original nodes to their copies
        unordered_map<Node*, Node*> hashmap;
        
        // Iterate over the original list to create copies of each node
        Node* curr = head;
        while (curr) {
            hashmap[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        // Iterate over the original list again to set the next and random pointers
        curr = head;
        while (curr) {
            if (curr->next) {
                hashmap[curr]->next = hashmap[curr->next];
            }
            if (curr->random) {
                hashmap[curr]->random = hashmap[curr->random];
            }
            curr = curr->next;
        }
        
        // Return the head of the copied list
        return hashmap[head];
    }
};
```

## Test Cases
```
Input: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

## Key Takeaways
- Use a hashmap to store the mapping of original nodes to their copies to avoid duplicate copies.
- Iterate over the original list twice: once to create copies of each node and again to set the `next` and `random` pointers.
- The `copyRandomList` function returns the head of the copied list, which is stored in the hashmap.