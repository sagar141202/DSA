# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz. sz will be between 1 and 30. n will be between 1 and sz. It is guaranteed that the nth node from the end is unique. For example, if we have a list 1 -> 2 -> 3 -> 4 -> 5 and n = 2, we should return the head of the list 1 -> 2 -> 3 -> 5.

## Approach
We can solve this problem by using two pointers. The first pointer will be nth steps ahead of the second pointer. When the first pointer reaches the end of the list, the second pointer will be at the node right before the node to be deleted.

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
        
        // Move the first pointer nth steps ahead
        for (int i = 0; i < n; i++) {
            first = first->next;
        }
        
        // If the first pointer is nullptr, it means we need to delete the head
        if (first == nullptr) {
            return head->next;
        }
        
        // Move both pointers until the first pointer reaches the end
        while (first->next != nullptr) {
            first = first->next;
            second = second->next;
        }
        
        // Delete the nth node from the end
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
- Use two pointers to solve this problem efficiently.
- Handle edge cases where n is equal to the length of the list.
- Make sure to update the next pointer of the node before the node to be deleted.