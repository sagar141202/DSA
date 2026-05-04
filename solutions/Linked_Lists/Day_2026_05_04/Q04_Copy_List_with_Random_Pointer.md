# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. The task is to create a deep copy of the original list, ensuring that the random pointers in the new list point to the corresponding nodes in the new list. Each node in the list has a unique value. The list is represented as a sequence of nodes, where each node is defined as `Node(val, next, random)`, and `val`, `next`, and `random` are the value of the node, the next node in the sequence, and a random node in the sequence respectively.

## Approach
We can solve this problem by using a hash map to store the mapping between the original nodes and the new nodes. Then, we can iterate over the original list and create a new node for each node in the original list. We use the hash map to find the corresponding new node for the next and random pointers.

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
        if (head == NULL) return NULL;

        // Create a hash map to store the mapping between the original nodes and the new nodes
        unordered_map<Node*, Node*> map;
        Node* old_node = head;
        while (old_node != NULL) {
            map[old_node] = new Node(old_node->val);
            old_node = old_node->next;
        }

        // Update the next and random pointers of the new nodes
        old_node = head;
        while (old_node != NULL) {
            if (old_node->next != NULL) {
                map[old_node]->next = map[old_node->next];
            }
            if (old_node->random != NULL) {
                map[old_node]->random = map[old_node->random];
            }
            old_node = old_node->next;
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
- Use a hash map to store the mapping between the original nodes and the new nodes.
- Iterate over the original list to create a new node for each node in the original list.
- Update the next and random pointers of the new nodes using the hash map.