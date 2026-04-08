# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. The task is to create a deep copy of the linked list, including the random pointers. The given linked list is represented as a sequence of nodes, where each node contains a value and two pointers: `next` and `random`. The `next` pointer points to the next node in the sequence, while the `random` pointer points to a random node in the sequence. The constraints are that the list can be empty, and the random pointer can point to any node in the list or be `NULL`. For example, given a list with three nodes: `1 -> 2 -> 3`, where `1.random -> 3`, `2.random -> 1`, and `3.random -> 2`, the copied list should also have the same random pointers.

## Approach
The approach involves traversing the original list and creating a new node for each node in the original list. We use a hash map to store the mapping between the original nodes and their corresponding new nodes. This allows us to efficiently find the new node corresponding to the random pointer of each original node.

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

        // Create a hash map to store the mapping between original nodes and new nodes
        unordered_map<Node*, Node*> nodeMap;

        // Traverse the original list and create new nodes
        Node* original = head;
        Node* newHead = new Node(original->val);
        nodeMap[original] = newHead;
        Node* newNode = newHead;

        original = original->next;
        while (original) {
            newNode->next = new Node(original->val);
            nodeMap[original] = newNode->next;
            original = original->next;
            newNode = newNode->next;
        }

        // Traverse the original list again and set the random pointers
        original = head;
        newNode = newHead;
        while (original) {
            if (original->random) {
                newNode->random = nodeMap[original->random];
            }
            original = original->next;
            newNode = newNode->next;
        }

        return newHead;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3, where 1.random -> 3, 2.random -> 1, and 3.random -> 2
Output: 1' -> 2' -> 3', where 1'.random -> 3', 2'.random -> 1', and 3'.random -> 2'
```

## Key Takeaways
- Use a hash map to store the mapping between original nodes and new nodes to efficiently find the new node corresponding to the random pointer of each original node.
- Traverse the original list twice: once to create new nodes and once to set the random pointers.
- Handle the case where the random pointer is `NULL` by checking if the random pointer of the original node is not `NULL` before setting the random pointer of the new node.