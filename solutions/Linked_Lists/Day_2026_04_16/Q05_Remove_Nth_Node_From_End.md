# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is at least 1 and at most 30. 0 <= Node.val <= 100, and 1 <= n <= sz. It is guaranteed that the nth node from the end is unique.

## Approach
The algorithm uses two pointers, both starting at the head of the list. The first pointer moves n steps ahead, then both pointers move together until the first pointer reaches the end of the list. At this point, the second pointer is at the node before the nth node from the end, allowing for easy removal of the nth node.

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
        
        // Move first pointer n steps ahead
        for (int i = 0; i < n; i++) {
            first = first->next;
        }
        
        // If first pointer has reached the end, remove the head
        if (first == NULL) {
            return head->next;
        }
        
        // Move both pointers together until first pointer reaches the end
        while (first->next != NULL) {
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
- Use two pointers to traverse the linked list and remove the nth node from the end.
- Handle edge cases where n is equal to the length of the linked list.
- Ensure the solution has a time complexity of O(L) and a space complexity of O(1), where L is the length of the linked list.