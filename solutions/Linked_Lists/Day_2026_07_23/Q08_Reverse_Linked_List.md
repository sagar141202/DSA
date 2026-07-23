# Reverse Linked List

## Problem Statement
Reverse a singly linked list. The linked list is defined as `struct ListNode { int val; ListNode *next; ListNode() : val(0), next(nullptr) {} ; ListNode(int x) : val(x), next(nullptr) {} ; ListNode(int x, ListNode *next) : val(x), next(next) {} };`. The function should take the head of the list as input and return the head of the reversed list. For example, given the list `1 -> 2 -> 3 -> 4 -> 5`, the function should return `5 -> 4 -> 3 -> 2 -> 1`. The list can contain any number of nodes, including zero nodes.

## Approach
The algorithm uses a simple iterative approach to reverse the linked list by keeping track of the current node and the previous node. It iterates through the list, reversing the `next` pointer of each node. The function returns the head of the reversed list.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // Initialize previous node as nullptr
        ListNode* prev = nullptr;
        // Initialize current node as head
        ListNode* curr = head;
        // Traverse the list
        while (curr != nullptr) {
            // Store the next node
            ListNode* nextTemp = curr->next;
            // Reverse the link
            curr->next = prev;
            // Move pointers one position ahead
            prev = curr;
            curr = nextTemp;
        }
        // At the end, 'prev' will be the new head
        return prev;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1
Input: 1 -> 2
Output: 2 -> 1
Input: 
Output: 
```

## Key Takeaways
- Initialize three pointers: previous, current, and next to keep track of the nodes.
- Traverse the list and reverse the `next` pointer of each node.
- At the end of the traversal, the `prev` pointer will be pointing to the new head of the reversed list.