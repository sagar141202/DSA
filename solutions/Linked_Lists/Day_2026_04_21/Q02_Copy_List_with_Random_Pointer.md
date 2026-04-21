# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an integer data and a pointer to the next node, as well as a random pointer that can point to any node in the list. The task is to create a deep copy of this linked list, ensuring that the random pointers in the new list point to the corresponding nodes in the new list. The given linked list is defined by a Node class with three attributes: val (integer data), next (pointer to the next node), and random (random pointer to any node). The function should return the head of the copied linked list.

## Approach
The solution involves creating a hashmap to store the mapping of original nodes to their copies, then iterating through the list to create copies of each node and update their next and random pointers. This approach ensures that each node is copied only once and the random pointers are correctly updated.

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
        // Create a hashmap to store the mapping of original nodes to their copies
        unordered_map<Node*, Node*> hashmap;
        
        // Create a copy of each node and store it in the hashmap
        Node* curr = head;
        while (curr != NULL) {
            hashmap[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        // Update the next and random pointers of each copied node
        curr = head;
        while (curr != NULL) {
            if (curr->next != NULL) {
                hashmap[curr]->next = hashmap[curr->next];
            }
            if (curr->random != NULL) {
                hashmap[curr]->random = hashmap[curr->random];
            }
            curr = curr->next;
        }
        
        // Return the head of the copied linked list
        return hashmap[head];
    }
};
```

## Test Cases
```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

## Key Takeaways
- Use a hashmap to store the mapping of original nodes to their copies to avoid creating duplicate copies.
- Iterate through the list twice: once to create copies of each node and once to update their next and random pointers.
- Update the next and random pointers of each copied node using the hashmap to ensure correct connections.