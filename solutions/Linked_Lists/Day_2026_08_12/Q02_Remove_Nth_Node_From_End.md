# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is between 1 and 30,000. For example, with n = 1, the last node is removed, and with n = sz, the first node is removed. You are guaranteed that n is a valid node to remove.

## Approach
We use two pointers, p1 and p2, to traverse the linked list. p1 is moved n steps ahead of p2. Then, both pointers are moved one step at a time until p1 reaches the end of the list. At this point, p2 is at the node before the one to be removed.

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
        // Create two pointers, p1 and p2, and move p1 n steps ahead
        ListNode* p1 = head;
        ListNode* p2 = head;
        
        // Move p1 n steps ahead
        for (int i = 0; i < n; i++) {
            p1 = p1->next;
        }
        
        // If p1 is nullptr, it means we need to remove the head
        if (p1 == nullptr) {
            return head->next;
        }
        
        // Move both pointers until p1 reaches the end
        while (p1->next != nullptr) {
            p1 = p1->next;
            p2 = p2->next;
        }
        
        // Remove the nth node from the end
        p2->next = p2->next->next;
        
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
- Use two pointers to solve linked list problems that involve removing nodes based on their position from the end.
- Be careful when handling edge cases, such as when the node to be removed is the head of the list.
- Always test your solution with different inputs to ensure it works correctly.