# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. The task is to create a deep copy of the original list. The node structure is defined as follows: each node has a value, a next pointer, and a random pointer. The constraints are that the list can be empty, and the random pointer can be null. An example of this is a list with the following structure: 
-1 -> 2 -> 3 with random pointers 2 -> 1, 1 -> 3, 3 -> 2. The output should be a new list with the same structure but with different node objects.

## Approach
The algorithm involves creating a new node for each node in the original list, copying the values, and then updating the next and random pointers. We use a hash map to store the mapping between original nodes and their copies. This allows us to efficiently find the copy of a node when updating the random pointers.

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

        // Create a hash map to store the mapping between original nodes and their copies
        unordered_map<Node*, Node*> nodeMap;

        // Create a new node for each node in the original list
        Node* curr = head;
        while (curr) {
            nodeMap[curr] = new Node(curr->val);
            curr = curr->next;
        }

        // Update the next and random pointers
        curr = head;
        while (curr) {
            if (curr->next) nodeMap[curr]->next = nodeMap[curr->next];
            if (curr->random) nodeMap[curr]->random = nodeMap[curr->random];
            curr = curr->next;
        }

        return nodeMap[head];
    }
};
```

## Test Cases
```
Input: 
-1 -> 2 -> 3 
with random pointers 
2 -> 1, 
1 -> 3, 
3 -> 2
Output: 
A new list with the same structure but with different node objects
```

## Key Takeaways
- We use a hash map to store the mapping between original nodes and their copies to efficiently find the copy of a node when updating the random pointers.
- We create a new node for each node in the original list and update the next and random pointers separately to avoid confusion.