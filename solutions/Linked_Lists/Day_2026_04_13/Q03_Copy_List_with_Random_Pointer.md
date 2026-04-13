# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. Create a deep copy of the original list. The node structure is given as follows: 
```cpp
struct Node {
    int val;
    Node *next;
    Node *random;
    Node(int x) : val(x), next(NULL), random(NULL) {}
};
```
The constraints are: 
- The number of nodes in the list will not exceed 100.
- 1 <= val <= 100.
- The list is not guaranteed to be non-circular.

## Approach
The algorithm involves creating a hash map to store the mapping of the original nodes to their copies. Then, we iterate through the original list and create copies of each node. Finally, we update the next and random pointers of the copied nodes.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for a Node.
struct Node {
    int val;
    Node *next;
    Node *random;
    Node(int x) : val(x), next(NULL), random(NULL) {}
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return NULL;
        
        // Create a hash map to store the mapping of the original nodes to their copies
        unordered_map<Node*, Node*> map;
        Node* curr = head;
        
        // Create copies of each node
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        curr = head;
        
        // Update the next and random pointers of the copied nodes
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
- Use a hash map to store the mapping of the original nodes to their copies.
- Create copies of each node before updating the pointers.
- Update the next and random pointers of the copied nodes based on the mapping.