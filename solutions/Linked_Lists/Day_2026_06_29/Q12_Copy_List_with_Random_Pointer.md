# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. Create a deep copy of the original linked list. The linked list is represented as a sequence of nodes, and each node has a unique value. The next pointer and random pointer of each node should be copied correctly. For example, if we have a list with the following structure: 
1 -> 2 -> 3
with random pointers:
1 -> 3
2 -> 1
3 -> 2
The copied list should have the same structure and random pointers.

## Approach
We can solve this problem by using a hashmap to store the mapping between the original nodes and the copied nodes. Then we can iterate over the original list to copy the next and random pointers. This approach ensures that each node is copied only once.

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

        // Create a hashmap to store the mapping between the original nodes and the copied nodes
        unordered_map<Node*, Node*> hashmap;
        Node* curr = head;

        // First pass: create a copy of each node and store it in the hashmap
        while (curr) {
            hashmap[curr] = new Node(curr->val);
            curr = curr->next;
        }

        // Second pass: copy the next and random pointers
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
Input: 
1 -> 2 -> 3
with random pointers:
1 -> 3
2 -> 1
3 -> 2
Output: 
1 -> 2 -> 3
with random pointers:
1 -> 3
2 -> 1
3 -> 2
```

## Key Takeaways
- Use a hashmap to store the mapping between the original nodes and the copied nodes to avoid copying the same node multiple times.
- Perform two passes over the original list: one to create a copy of each node, and another to copy the next and random pointers.
- The time complexity is O(N), where N is the number of nodes in the list, and the space complexity is also O(N) due to the use of the hashmap.