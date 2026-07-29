# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an integer data and two pointers, `next` and `random`. The `next` pointer points to the next node in the linked list, and the `random` pointer points to any node in the linked list. The task is to create a deep copy of the given linked list. The constraints are: (1) the number of nodes in the linked list is in the range [0, 1000], (2) the value of each node is in the range [-10^4, 10^4], and (3) the `random` pointer of each node can point to any node in the linked list or be `nullptr`.

## Approach
To solve this problem, we can use a hash map to store the mapping of the original nodes to their corresponding copied nodes. Then, we can traverse the linked list and for each node, create a copy of it and store it in the hash map. Finally, we can update the `next` and `random` pointers of the copied nodes.

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
        if (head == nullptr) return nullptr;
        
        // Create a hash map to store the mapping of the original nodes to their corresponding copied nodes
        unordered_map<Node*, Node*> map;
        Node* curr = head;
        
        // Traverse the linked list and create a copy of each node
        while (curr != nullptr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        // Update the next and random pointers of the copied nodes
        curr = head;
        while (curr != nullptr) {
            if (curr->next != nullptr) {
                map[curr]->next = map[curr->next];
            }
            if (curr->random != nullptr) {
                map[curr]->random = map[curr->random];
            }
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
- Use a hash map to store the mapping of the original nodes to their corresponding copied nodes.
- Traverse the linked list twice: once to create the copies of the nodes and once to update the `next` and `random` pointers.
- The time complexity is O(N), where N is the number of nodes in the linked list, and the space complexity is also O(N) due to the hash map.