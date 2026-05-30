# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, 1 <= sz <= 30, 0 <= Node.val <= 100, 1 <= n <= sz. The problem requires a solution that works within the given constraints and returns the modified linked list.

## Approach
The algorithm uses two pointers to traverse the linked list, maintaining a distance of n nodes between them. When the first pointer reaches the end of the list, the second pointer is at the node before the one to be removed. This allows for efficient removal of the nth node from the end.

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
        
        // Move the first pointer n steps ahead
        for (int i = 0; i < n; i++) {
            first = first->next;
        }
        
        // If the first pointer is nullptr, it means the node to be removed is the head
        if (first == nullptr) {
            return head->next;
        }
        
        // Move both pointers until the first pointer reaches the end
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
- The two-pointer technique is useful for problems involving linked lists and relative positioning.
- It's essential to handle edge cases, such as when the node to be removed is the head of the list.
- The algorithm should be able to efficiently remove the nth node from the end in a single pass.