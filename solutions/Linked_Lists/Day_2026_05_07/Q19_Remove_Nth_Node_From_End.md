# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The removal is 1-indexed, meaning the last node is the 1st node from the end. The number of nodes in the list is in the range [1, 30]. It is guaranteed that n is a valid node from the end.

## Approach
We will use two pointers, both starting at the head of the list, with the second pointer being n nodes ahead of the first pointer. Then, we will move both pointers one node at a time until the second pointer reaches the end of the list. At this point, the first pointer will be at the node right before the nth node from the end, allowing us to remove the nth node.

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
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // Initialize two pointers
        ListNode* first = head;
        ListNode* second = head;
        
        // Move the second pointer n nodes ahead
        for (int i = 0; i < n; i++) {
            second = second->next;
        }
        
        // If the second pointer is NULL, we need to remove the head
        if (second == NULL) {
            return head->next;
        }
        
        // Move both pointers until the second pointer reaches the end
        while (second->next != NULL) {
            first = first->next;
            second = second->next;
        }
        
        // Remove the nth node from the end
        first->next = first->next->next;
        
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
- Use two pointers to traverse the linked list, with one pointer being n nodes ahead of the other.
- Move both pointers until the second pointer reaches the end of the list.
- Remove the nth node from the end by updating the next pointer of the node before it.