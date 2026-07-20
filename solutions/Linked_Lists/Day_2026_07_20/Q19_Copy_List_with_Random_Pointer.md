# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. The task is to create a deep copy of the linked list, ensuring that the random pointers in the new list point to the corresponding nodes in the new list. The given linked list is defined by a Node class with attributes `val`, `next`, and `random`. The constraint is that we cannot modify the original list.

## Approach
We will use a hash map to store the mapping of original nodes to their copies. Then, we will iterate through the original list, creating a copy of each node and updating its `next` and `random` pointers accordingly. This approach ensures that the random pointers in the new list point to the correct nodes.

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
        // Create a hash map to store the mapping of original nodes to their copies
        unordered_map<Node*, Node*> map;
        
        // Iterate through the original list to create a copy of each node
        Node* curr = head;
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        // Update the next and random pointers of each node in the new list
        curr = head;
        while (curr) {
            if (curr->next) {
                map[curr]->next = map[curr->next];
            }
            if (curr->random) {
                map[curr]->random = map[curr->random];
            }
            curr = curr->next;
        }
        
        // Return the head of the new list
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
- Use a hash map to store the mapping of original nodes to their copies for efficient lookups.
- Create a copy of each node in the original list before updating the pointers to avoid modifying the original list.
- Update the `next` and `random` pointers of each node in the new list using the hash map.