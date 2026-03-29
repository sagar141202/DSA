# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node is followed by the last node, then the second node is followed by the second to last node, and so on. The reordered list should be in the form: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …, where L0, L1, L2, …, Ln-1, Ln are the nodes of the original list. For example, if the input list is 1 -> 2 -> 3 -> 4, the output should be 1 -> 4 -> 2 -> 3.

## Approach
To solve this problem, we will first find the middle of the linked list, then reverse the second half of the list. Finally, we will reorder the list by alternating between the first half and the reversed second half.

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
        // base case
        if (!head || !head->next || !head->next->next) return;

        // find the middle of the list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // reverse the second half of the list
        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* prev = nullptr;
        while (second) {
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }

        // reorder the list
        ListNode* first = head;
        while (prev) {
            ListNode* temp1 = first->next;
            ListNode* temp2 = prev->next;
            first->next = prev;
            prev->next = temp1;
            first = temp1;
            prev = temp2;
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
- Finding the middle of a linked list can be done using the slow and fast pointer technique.
- Reversing a linked list can be done by iterating through the list and reversing the next pointers.
- Reordering a linked list can be done by alternating between two halves of the list.