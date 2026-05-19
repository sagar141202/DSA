# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an integer value and a random pointer to another node in the list. The task is to create a deep copy of the given list. The constraints are that the given list can be empty, and the random pointer of a node can point to any node in the list, including itself. The goal is to create a new list that is a copy of the original list, including the random pointers.

## Approach
To solve this problem, we can use a hash map to store the mapping between the original nodes and their corresponding copied nodes. We will then iterate through the original list, creating a new node for each original node and updating the next and random pointers accordingly.

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

        // Create a hash map to store the mapping between the original nodes and their corresponding copied nodes
        unordered_map<Node*, Node*> map;
        Node* curr = head;

        // First pass: Create a new node for each original node and store the mapping in the hash map
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }

        // Second pass: Update the next and random pointers of the copied nodes
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
- Use a hash map to store the mapping between the original nodes and their corresponding copied nodes.
- Perform two passes: one to create the new nodes and store the mapping, and another to update the next and random pointers.
- Use the hash map to efficiently look up the copied nodes and update their pointers.