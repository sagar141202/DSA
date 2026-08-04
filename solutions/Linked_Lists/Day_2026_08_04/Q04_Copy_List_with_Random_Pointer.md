# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. The task is to create a deep copy of the linked list, ensuring that the random pointers in the new list point to the corresponding nodes in the new list. The given linked list is defined by a Node class with attributes val, next, and random.

## Approach
We will use a hash map to store the mapping between the original nodes and their copies. Then, we will traverse the original list and create a copy of each node. We will use the hash map to update the next and random pointers of the copied nodes.

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

        // Create a hash map to store the mapping between the original nodes and their copies
        unordered_map<Node*, Node*> map;
        Node* oldNode = head;

        // Create a copy of each node and store it in the hash map
        while (oldNode) {
            map[oldNode] = new Node(oldNode->val);
            oldNode = oldNode->next;
        }

        oldNode = head;

        // Update the next and random pointers of the copied nodes
        while (oldNode) {
            if (oldNode->next) {
                map[oldNode]->next = map[oldNode->next];
            }
            if (oldNode->random) {
                map[oldNode]->random = map[oldNode->random];
            }
            oldNode = oldNode->next;
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
- Use a hash map to store the mapping between the original nodes and their copies.
- Traverse the original list to create a copy of each node and update the hash map.
- Traverse the original list again to update the next and random pointers of the copied nodes.