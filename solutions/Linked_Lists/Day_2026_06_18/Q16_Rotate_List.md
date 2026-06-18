# Rotate List

## Problem Statement
Given the head of a linked list, rotate the list to the right by k places. The number of nodes in the list is in the range [0, 100]. 0 <= Node.val <= 100. 0 <= k <= 105. It is guaranteed that the number k is non-negative. Example: if the list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list should be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
The solution involves first calculating the length of the linked list, then connecting the tail to the head to form a circular linked list. We then find the new tail node by moving (length - k % length - 1) steps from the head. The next node of the new tail is the new head.

## Complexity
- Time: O(n)
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
    ListNode* rotateRight(ListNode* head, int k) {
        // Base cases
        if (!head || !head->next || k == 0) {
            return head;
        }

        // Calculate length and connect tail to head
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n += 1;
        }
        old_tail->next = head;

        // Find new tail
        ListNode* new_tail = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            new_tail = new_tail->next;
        }

        // Find new head
        ListNode* new_head = new_tail->next;

        // Break the circle
        new_tail->next = nullptr;

        return new_head;
    }
};
```

## Test Cases
```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Input: head = [1,2,3,4,5], k = 5
Output: [1,2,3,4,5]
```

## Key Takeaways
- The key to solving this problem is to first connect the tail to the head to form a circular linked list.
- We then find the new tail node by moving (length - k % length - 1) steps from the head.
- The next node of the new tail is the new head, and we break the circle by setting the next of the new tail to nullptr.