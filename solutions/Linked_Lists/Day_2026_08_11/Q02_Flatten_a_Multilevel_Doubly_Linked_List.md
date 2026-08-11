# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a pointer to the next node, a pointer to the previous node, and a pointer to the child node. The task is to flatten the multilevel doubly linked list into a single-level doubly linked list. The list should be flattened in a way that all nodes at depth 1 come first, followed by all nodes at depth 2, and so on. If there are two nodes at the same depth, the node with the smaller topological value comes first.

## Approach
We will use a recursive approach to traverse the multilevel linked list and append the child nodes to the main list. We will keep track of the current node and its next node to correctly update the pointers.

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
    Node* prev;
    Node* next;
    Node* child;
};

class Solution {
public:
    Node* flatten(Node* head) {
        if (!head) return head;
        Node* dummy = new Node();
        dummy->next = head;
        flattenHelper(dummy, head);
        dummy->next->prev = nullptr;
        return dummy->next;
    }
    
    void flattenHelper(Node* prev, Node* curr) {
        if (!curr) return;
        curr->prev = prev;
        prev->next = curr;
        Node* temp = curr->next;
        if (curr->child) {
            flattenHelper(curr, curr->child);
            curr->child = nullptr;
            curr = prev->next;
            flattenHelper(curr, temp);
        } else {
            flattenHelper(curr, temp);
        }
    }
};
```

## Test Cases
```
Input: 
1---2---3---4---5---6
    |
    7---8---9---10
        |
        11---12

Output: 
1---2---7---8---11---12---9---10---3---4---5---6
```

## Key Takeaways
- Use a recursive helper function to flatten the multilevel linked list.
- Keep track of the current node and its next node to correctly update the pointers.
- Use a dummy node to simplify the code and handle edge cases.