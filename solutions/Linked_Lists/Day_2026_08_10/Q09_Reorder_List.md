# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node becomes the first node of the reordered list, the last node becomes the second node, the second node becomes the third node, and so on. The reordered list should be in the form: `1 -> n -> 2 -> (n-1) -> 3 -> (n-2) -> ...`. If the list has only one node, it remains unchanged. For example, given the list `1 -> 2 -> 3 -> 4`, the reordered list would be `1 -> 4 -> 2 -> 3`.

## Approach
The approach involves finding the middle of the linked list, reversing the second half, and then merging the two halves. We use slow and fast pointers to find the middle and a simple iterative approach to reverse the second half.

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
    void reorderList(ListNode* head) {
        if (!head || !head->next || !head->next->next) return;

        // Find the middle of the list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Reverse the second half
        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* prev = nullptr;
        while (second) {
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }

        // Merge two sorted lists
        ListNode* first = head;
        second = prev;
        while (second) {
            ListNode* temp1 = first->next;
            ListNode* temp2 = second->next;
            first->next = second;
            second->next = temp1;
            first = temp1;
            second = temp2;
        }
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4
Output: 1 -> 4 -> 2 -> 3
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 5 -> 2 -> 4 -> 3
```

## Key Takeaways
- We use slow and fast pointers to find the middle of the linked list efficiently.
- Reversing the second half of the list is crucial for achieving the desired reorder.
- Merging the two halves requires careful handling of node pointers to avoid losing any nodes.