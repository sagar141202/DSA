# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of a nested list. Your task is to flatten the multilevel linked list into a single-level doubly linked list. The nodes in the flattened list should be in the order of their appearance in the original list. For example, if the input list is 1 -> 2 -> 3 -> 4 -> 5 -> 6, where 3 has a child node 7 -> 8 -> 9, and 8 has a child node 10 -> 11, the output list should be 1 -> 2 -> 3 -> 7 -> 8 -> 10 -> 11 -> 9 -> 4 -> 5 -> 6.

## Approach
We will use a recursive approach to traverse the linked list and flatten it. We will start by traversing the main list and whenever we encounter a node with a child, we will recursively traverse the child list and append it to the main list.

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
        Node* curr = head;
        while (curr) {
            if (curr->child) {
                // Find the tail of the child list
                Node* childTail = curr->child;
                while (childTail->next) {
                    childTail = childTail->next;
                }
                
                // Connect the child list to the main list
                childTail->next = curr->next;
                if (curr->next) {
                    curr->next->prev = childTail;
                }
                curr->next = curr->child;
                curr->child->prev = curr;
                curr->child = nullptr;
            }
            curr = curr->next;
        }
        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6, where 3 has a child node 7 -> 8 -> 9, and 8 has a child node 10 -> 11
Output: 1 -> 2 -> 3 -> 7 -> 8 -> 10 -> 11 -> 9 -> 4 -> 5 -> 6
```

## Key Takeaways
- The key to solving this problem is to identify the child nodes and connect them to the main list.
- We use a recursive approach to traverse the linked list and flatten it.
- The time complexity of the solution is O(N), where N is the total number of nodes in the linked list.