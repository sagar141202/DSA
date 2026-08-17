# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an integer value and a random pointer to any other node in the list (including itself). The task is to create a deep copy of the given linked list, preserving the original structure and connections. The linked list node is defined as follows: each node contains an integer val, a pointer next to the next node, and a pointer random to a random node in the list. The constraints are: 0 <= number of nodes <= 100, 0 <= Node.val <= 10^6, and the list is non-circular (i.e., it does not form a cycle).

## Approach
Create a hashmap to store the mapping of original nodes to their copies. Then, traverse the list and create a copy of each node, storing the mapping in the hashmap. Finally, traverse the list again to set the next and random pointers of the copied nodes.

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
        Node* original = head;
        Node* copy = new Node(original->val);
        hashmap[original] = copy;
        original = original->next;

        // Traverse the list and create a copy of each node
        while (original) {
            copy->next = new Node(original->val);
            hashmap[original] = copy->next;
            copy = copy->next;
            original = original->next;
        }

        // Reset pointers
        original = head;
        copy = hashmap[head];

        // Traverse the list again to set the next and random pointers of the copied nodes
        while (original) {
            if (original->random) {
                copy->random = hashmap[original->random];
            }
            original = original->next;
            copy = copy->next;
        }

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
- Use a hashmap to store the mapping of original nodes to their copies for efficient lookup.
- Traverse the list twice: first to create copies of nodes and store the mapping, and second to set the next and random pointers of the copied nodes.
- Handle edge cases such as an empty list or a list with a single node.