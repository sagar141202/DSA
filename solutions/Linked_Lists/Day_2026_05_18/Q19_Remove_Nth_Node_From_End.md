# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is at least n + 1. You are guaranteed that n is valid for the list. For example, given a linked list 1 -> 2 -> 3 -> 4 -> 5 and n = 2, after removing the second node from the end, the list becomes 1 -> 2 -> 3 -> 5.

## Approach
The algorithm uses two pointers, both starting at the head of the list. The first pointer moves n steps ahead, then both pointers move one step at a time until the first pointer reaches the end of the list. At this point, the second pointer is at the node right before the node to be removed. We then remove the nth node from the end by updating the next pointer of the second pointer.

## Complexity
- Time: O(L)
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // Initialize two pointers
        ListNode* first = head;
        ListNode* second = head;
        
        // Move first pointer n steps ahead
        for (int i = 0; i < n; i++) {
            first = first->next;
        }
        
        // If first pointer has reached the end, remove the head
        if (first == nullptr) {
            return head->next;
        }
        
        // Move both pointers one step at a time
        while (first->next != nullptr) {
            first = first->next;
            second = second->next;
        }
        
        // Remove the nth node from the end
        second->next = second->next->next;
        
        return head;
    }
};
```

## Test Cases
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Input: head = [1], n = 1
Output: []
Input: head = [1,2], n = 1
Output: [1]
```

## Key Takeaways
- Use two pointers to track the node to be removed and the node before it.
- Move the first pointer n steps ahead to create a gap between the two pointers.
- Move both pointers one step at a time to maintain the gap until the first pointer reaches the end.
- Remove the nth node from the end by updating the next pointer of the second pointer.