# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an integer value and a random pointer to another node in the list. The task is to create a deep copy of the linked list. The constraints are that we cannot modify the original list and we should minimize the extra space used. For example, if we have a list with nodes having values 1, 2, and 3, and the random pointers are 2 -> 1, 1 -> 3, and 3 -> 2, the copied list should have the same structure and values.

## Approach
We will use a hash map to store the mapping between the original nodes and the copied nodes. Then we will traverse the original list to create the copied nodes and update the next and random pointers accordingly. This approach allows us to avoid infinite loops when dealing with cycles in the list.

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
        // Create a hash map to store the mapping between the original nodes and the copied nodes
        unordered_map<Node*, Node*> map;
        
        // First pass: create the copied nodes and store them in the hash map
        Node* curr = head;
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        // Second pass: update the next and random pointers of the copied nodes
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
        
        // Return the head of the copied list
        return map[head];
    }
};
```

## Test Cases
```
Input: 
Node 1 -> Node 2 -> Node 3
Node 1 random -> Node 3
Node 2 random -> Node 1
Node 3 random -> Node 2
Output: 
Copied Node 1 -> Copied Node 2 -> Copied Node 3
Copied Node 1 random -> Copied Node 3
Copied Node 2 random -> Copied Node 1
Copied Node 3 random -> Copied Node 2
```

## Key Takeaways
- Use a hash map to store the mapping between the original nodes and the copied nodes to avoid infinite loops when dealing with cycles in the list.
- Perform two passes: one to create the copied nodes and another to update the next and random pointers.
- This approach has a time complexity of O(N) and a space complexity of O(N), where N is the number of nodes in the linked list.