# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. The task is to create a deep copy of the original list. The deep copy should include all the nodes with their values and the random pointers should also be copied. The list can be empty and can have any number of nodes.

## Approach
Create a hash map to store the mapping of the original nodes to their copies. Traverse the list to create copies of all the nodes. Then, traverse the list again to set the next and random pointers of the copied nodes.

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
        
        // Create a hash map to store the mapping of the original nodes to their copies
        unordered_map<Node*, Node*> map;
        
        // Traverse the list to create copies of all the nodes
        Node* original = head;
        Node* copy = NULL;
        Node* prev = NULL;
        while (original) {
            Node* newNode = new Node(original->val);
            map[original] = newNode;
            if (prev) prev->next = newNode;
            prev = newNode;
            original = original->next;
        }
        
        // Traverse the list again to set the next and random pointers of the copied nodes
        original = head;
        copy = map[head];
        while (original) {
            if (original->random) copy->random = map[original->random];
            original = original->next;
            copy = copy->next;
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
- We need to create a deep copy of the list, including the random pointers.
- A hash map can be used to store the mapping of the original nodes to their copies.
- We need to traverse the list twice, once to create the copies and once to set the pointers.