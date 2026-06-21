# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node becomes the last node of the first half, the second node becomes the first node of the second half, the third node becomes the second node of the second half, and so on. For example, if the input list is 1 -> 2 -> 3 -> 4, the reordered list should be 1 -> 4 -> 2 -> 3. The list should be reordered in-place.

## Approach
The approach is to find the middle of the linked list, reverse the second half of the list, and then merge the two halves. We can use the slow and fast pointer technique to find the middle of the list, and then reverse the second half.

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
        
        // reverse the second half of the list
        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* prev = nullptr;
        while (second) {
            ListNode* nextTemp = second->next;
            second->next = prev;
            prev = second;
            second = nextTemp;
        }
        
        // merge the two halves
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
- Use the slow and fast pointer technique to find the middle of a linked list.
- Reverse the second half of the list by iterating through it and changing the `next` pointers.
- Merge the two halves by iterating through both halves and changing the `next` pointers.