# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is between 1 and 30,000. n will always be valid, i.e., 1 ≤ n ≤ sz. The problem can be solved by using a two-pointer approach to track the nth node from the end.

## Approach
We use two pointers, p1 and p2, to traverse the linked list. p1 is moved n steps ahead of p2, and then both pointers are moved one step at a time until p1 reaches the end of the list. At this point, p2 will be at the nth node from the end.

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
        // Initialize two pointers, p1 and p2
        ListNode* p1 = head;
        ListNode* p2 = head;
        
        // Move p1 n steps ahead of p2
        for (int i = 0; i < n; i++) {
            p1 = p1->next;
        }
        
        // If p1 is nullptr, it means we need to remove the head
        if (p1 == nullptr) {
            return head->next;
        }
        
        // Move both pointers one step at a time until p1 reaches the end
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
Input: [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Input: [1], n = 1
Output: []
Input: [1,2], n = 1
Output: [1]
```

## Key Takeaways
- Use two pointers to track the nth node from the end.
- Move the first pointer n steps ahead of the second pointer.
- Move both pointers one step at a time until the first pointer reaches the end.