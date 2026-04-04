# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes' values are in the range [-5000, 5000]. The list is guaranteed to be non-empty, except for the case where the list is empty. For example, given the linked list 1 -> 2 -> 3 -> 4 -> 5, the reversed linked list should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
We can solve this problem by initializing three pointers: previous, current, and next. We initialize the previous pointer to NULL and the current pointer to the head of the list. Then, we traverse the list, updating the next pointer of each node to point to the previous node. This approach allows us to reverse the linked list in-place.

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
        // Initialize three pointers: previous, current, and next
        ListNode* prev = NULL;
        ListNode* curr = head;
        ListNode* next = NULL;

        // Traverse the list and reverse the links
        while (curr != NULL) {
            // Store the next node
            next = curr->next;
            // Reverse the link
            curr->next = prev;
            // Move the pointers one step forward
            prev = curr;
            curr = next;
        }

        // Return the new head of the reversed list
        return prev;
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
Input: [1, 2]
Output: [2, 1]
Input: []
Output: []
```

## Key Takeaways
- Initialize three pointers: previous, current, and next to reverse the linked list.
- Traverse the list and update the next pointer of each node to point to the previous node.
- Return the new head of the reversed list, which is the last non-NULL node in the original list.