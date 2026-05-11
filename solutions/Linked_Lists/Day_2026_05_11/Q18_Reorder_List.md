# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node becomes the last node of the first half, the second node becomes the last node of the second half, and so on. The problem requires a solution that runs in linear time complexity. For example, given the list 1 -> 2 -> 3 -> 4, the reordered list should be 1 -> 4 -> 2 -> 3. The list can have any number of nodes (including 0 or 1), and the nodes' values can be any integer.

## Approach
The algorithm involves finding the middle of the linked list, reversing the second half, and then merging the two halves. This approach ensures that the list is reordered as required. The solution utilizes a two-pointer technique to find the middle and a recursive function to reverse the second half.

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
        
        // Find the middle of the linked list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        // Reverse the second half of the linked list
        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* prev = nullptr;
        while (second) {
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }
        
        // Merge the two halves
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
- The two-pointer technique is useful for finding the middle of a linked list.
- Reversing a linked list can be done iteratively or recursively, and the choice depends on the problem constraints.
- Merging two linked lists requires careful handling of node pointers to avoid losing nodes or creating cycles.