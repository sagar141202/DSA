# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. The task is to create a deep copy of the linked list. The constraints are that the original list should not be modified, and the time complexity should be as low as possible. For example, given a list with nodes having values 1, 2, and 3, and the random pointers pointing to the next node, the next node, and the head node respectively, the function should return a new list with the same structure and values.

## Approach
The solution involves creating a new node for each node in the original list and then updating the next and random pointers of the new nodes based on the original list. We use a hashmap to store the mapping between the original nodes and the new nodes for efficient lookup.

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
        
        // Create a hashmap to store the mapping between the original nodes and the new nodes
        unordered_map<Node*, Node*> map;
        
        // Create a new node for each node in the original list
        Node* curr = head;
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        // Update the next and random pointers of the new nodes
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
Input: [[1,1],[2,1],[3,0]]
Output: [[1,1],[2,1],[3,0]]
```

## Key Takeaways
- We use a hashmap to store the mapping between the original nodes and the new nodes for efficient lookup.
- The time complexity is O(n) where n is the number of nodes in the list, because we are visiting each node twice.
- The space complexity is O(n) because we are creating a new node for each node in the original list and storing them in the hashmap.