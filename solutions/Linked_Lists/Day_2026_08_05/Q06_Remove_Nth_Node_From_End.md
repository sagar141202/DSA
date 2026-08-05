# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is between 1 and 30,000. n will be between 1 and sz (inclusive). It is guaranteed that n is a valid node to remove. For example, if we have a list 1 -> 2 -> 3 -> 4 -> 5 and n = 2, then after removing the 2nd node from the end, the list becomes 1 -> 2 -> 3 -> 5.

## Approach
The algorithm uses two pointers, both starting at the head of the list. The first pointer moves n steps ahead, then both pointers move one step at a time until the first pointer reaches the end. At this point, the second pointer is at the node right before the one to be removed. We then remove the nth node from the end by updating the next pointer of the second pointer's node.

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
        
        // If first pointer has reached the end, remove the head node
        if (first == nullptr) {
            return head->next;
        }
        
        // Move both pointers one step at a time until first pointer reaches the end
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
- Move the first pointer n steps ahead to create a gap of n nodes between the two pointers.
- When the first pointer reaches the end, the second pointer will be at the node right before the one to be removed.