# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an integer value and a random pointer to any other node in the list (or null). The task is to create a deep copy of the given linked list, ensuring that the new list has the same structure and connections as the original list. The constraints are that we cannot modify the original list and we should minimize the space complexity.

## Approach
We will use a hashmap to store the mapping between the original nodes and their corresponding copied nodes. Then, we will traverse the original list and create a new node for each node, copying its value and random pointer.

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
        
        // Create a hashmap to store the mapping between the original nodes and their corresponding copied nodes
        unordered_map<Node*, Node*> map;
        
        // First pass: create a new node for each node in the original list
        Node* curr = head;
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        // Second pass: copy the next and random pointers
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
- Use a hashmap to store the mapping between the original nodes and their corresponding copied nodes.
- Create a new node for each node in the original list and then copy the next and random pointers in a second pass.
- The time complexity is O(N) and the space complexity is O(N), where N is the number of nodes in the linked list.