# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is at least 1 and at most 10^5. You are given the head of the list and the integer n, where 1 <= n <= sz. For example, if we have a list 1 -> 2 -> 3 -> 4 -> 5 and n = 2, then the output should be 1 -> 2 -> 3 -> 5.

## Approach
We can solve this problem by using two pointers, one of which is nth steps ahead of the other. When the leading pointer reaches the end of the list, the trailing pointer will be at the node right before the one we want to remove. We then remove the nth node from the end by changing the next pointer of the trailing pointer.

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
        // Initialize two pointers, both pointing to the head of the list
        ListNode* leading = head;
        ListNode* trailing = head;

        // Move the leading pointer nth steps ahead
        for (int i = 0; i < n; i++) {
            leading = leading->next;
        }

        // If the leading pointer is nullptr, it means we need to remove the head
        if (leading == nullptr) {
            return head->next;
        }

        // Move both pointers until the leading pointer reaches the end of the list
        while (leading->next != nullptr) {
            leading = leading->next;
            trailing = trailing->next;
        }

        // Remove the nth node from the end
        trailing->next = trailing->next->next;

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
- We use two pointers to solve this problem, one of which is nth steps ahead of the other.
- When the leading pointer reaches the end of the list, the trailing pointer will be at the node right before the one we want to remove.
- We remove the nth node from the end by changing the next pointer of the trailing pointer.