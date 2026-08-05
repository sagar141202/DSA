# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. The task is to create a deep copy of the linked list, ensuring that the random pointers in the copied list point to the corresponding nodes in the copied list. The nodes in the original list are defined as follows: each node contains a value, a next pointer, and a random pointer. The constraints are that the number of nodes in the list will not exceed 100, and the values of the nodes will be between 1 and 10^8.

## Approach
To solve this problem, we can use a hashmap to store the mapping between the original nodes and their copies. Then, we can iterate over the original list to create the copies of the nodes and store them in the hashmap. Finally, we can iterate over the original list again to set the next and random pointers of the copied nodes.

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

        // Create a hashmap to store the mapping between the original nodes and their copies
        unordered_map<Node*, Node*> hashmap;
        Node* curr = head;
        while (curr) {
            hashmap[curr] = new Node(curr->val);
            curr = curr->next;
        }

        // Set the next and random pointers of the copied nodes
        curr = head;
        while (curr) {
            if (curr->next) {
                hashmap[curr]->next = hashmap[curr->next];
            }
            if (curr->random) {
                hashmap[curr]->random = hashmap[curr->random];
            }
            curr = curr->next;
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
- We use a hashmap to store the mapping between the original nodes and their copies to avoid creating duplicate copies of the same node.
- We iterate over the original list twice: once to create the copies of the nodes and store them in the hashmap, and again to set the next and random pointers of the copied nodes.
- The time complexity of the solution is O(n), where n is the number of nodes in the list, because we iterate over the list twice. The space complexity is also O(n) because we use a hashmap to store the mapping between the original nodes and their copies.