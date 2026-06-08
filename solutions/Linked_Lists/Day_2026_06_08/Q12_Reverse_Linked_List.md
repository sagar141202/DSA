# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes' values are in the range [-5000, 5000]. The list is guaranteed to be non-empty, except for the case where the list is empty. For example, if the input is 1 -> 2 -> 3 -> 4 -> 5, the output should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
The approach to solve this problem is to initialize three pointers: previous, current, and next. We initialize the previous pointer to NULL and the current pointer to the head of the list. Then, we traverse the list and reverse the next pointer of each node. The algorithm runs in a loop until the current pointer becomes NULL.

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
        // Initialize previous, current, and next pointers
        ListNode* prev = NULL;
        ListNode* curr = head;
        ListNode* next = NULL;

        // Traverse the list and reverse the next pointer of each node
        while (curr != NULL) {
            // Store the next node
            next = curr->next;
            // Reverse the next pointer
            curr->next = prev;
            // Move the previous and current pointers one step forward
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
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1
Input: 1 -> 2
Output: 2 -> 1
Input: 1
Output: 1
```

## Key Takeaways
- Initialize three pointers to keep track of the previous, current, and next nodes in the list.
- Traverse the list and reverse the next pointer of each node to reverse the list.
- Return the new head of the reversed list, which is the last non-NULL node in the original list.