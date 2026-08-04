# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node is followed by the last node, then the second node is followed by the second to last node, and so on. The problem requires a solution that modifies the original linked list in-place. For example, given the linked list `1 -> 2 -> 3 -> 4`, the reordered list would be `1 -> 4 -> 2 -> 3`. The solution should handle edge cases such as an empty linked list or a linked list with only one node.

## Approach
The algorithm involves finding the middle of the linked list, reversing the second half, and then merging the two halves. This approach ensures that the nodes are reordered as required. The solution uses a two-pointer technique to find the middle of the list and a recursive approach to reverse the second half.

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

        // find the middle of the list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // reverse the second half
        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* prev = nullptr;
        while (second) {
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }

        // merge the two halves
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
- The two-pointer technique is used to find the middle of the linked list.
- The second half of the list is reversed using a recursive approach.
- The two halves are merged to form the final reordered list.