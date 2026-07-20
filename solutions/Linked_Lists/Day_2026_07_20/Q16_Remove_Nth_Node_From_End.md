# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is in the range [1, 30]. For example, with n = 1 and the list 1 -> 2 -> 3 -> 4 -> 5, after removing the 1st node from the end, the list becomes 1 -> 2 -> 3 -> 4. It is guaranteed that n is a valid node to remove, i.e., 1 ≤ n ≤ sz.

## Approach
We use two pointers to traverse the linked list, one pointer is n steps ahead of the other. When the ahead pointer reaches the end of the list, the behind pointer will be at the node right before the one we want to remove. We can then remove the nth node from the end by updating the next pointer of the behind pointer.

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
        ListNode* ahead = head;
        ListNode* behind = head;
        
        // Move ahead pointer n steps ahead
        for (int i = 0; i < n; i++) {
            ahead = ahead->next;
        }
        
        // If ahead pointer is nullptr, it means we need to remove the head
        if (ahead == nullptr) {
            return head->next;
        }
        
        // Move both pointers until ahead pointer reaches the end
        while (ahead->next != nullptr) {
            ahead = ahead->next;
            behind = behind->next;
        }
        
        // Remove the nth node from the end
        behind->next = behind->next->next;
        
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
- Handle edge cases where n is equal to the length of the linked list.
- Make sure to update the next pointer of the behind pointer correctly to remove the nth node from the end.