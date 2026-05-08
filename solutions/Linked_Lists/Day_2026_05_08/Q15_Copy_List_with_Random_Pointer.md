# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. Create a deep copy of the original list.

## Approach
We will use a hash map to store the mapping between the original nodes and the copied nodes. Then, we will traverse the original list to copy the next and random pointers.

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
        
        // Traverse the original list to create the copied nodes
        Node* curr = head;
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        // Traverse the original list to copy the next and random pointers
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
Node 1: val = 7, next = Node 2, random = Node 1
Node 2: val = 13, next = Node 3, random = Node 0 (NULL)
Node 3: val = 11, next = Node 4, random = Node 2
Node 4: val = 10, next = Node 5, random = Node 4
Node 5: val = 1, next = NULL, random = Node 3

Output: 
The copied list will have the same structure and values as the original list.
```

## Key Takeaways
- To solve this problem, we need to use a hash map to store the mapping between the original nodes and the copied nodes.
- We need to traverse the original list twice: once to create the copied nodes and once to copy the next and random pointers.
- This solution has a time complexity of O(N) and a space complexity of O(N), where N is the number of nodes in the list.