# Rotate List

## Problem Statement
Given the head of a linked list, rotate the list to the right by k places. The number of nodes in the list is in the range [0, 100]. 0 <= k <= 105. It is guaranteed that the number of nodes in the list is in the range [0, 100] and 0 <= k <= 105. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list should be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
The approach involves finding the length of the linked list, connecting the last node to the head to form a circular linked list, and then finding the new tail node which is at (length - k % length - 1)th position. The node next to the new tail node will be the new head of the rotated list.

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
        // base case
        if (!head || !head->next || k == 0) {
            return head;
        }

        // find the length of the list and the last node
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n += 1;
        }

        // connect the last node to the head
        old_tail->next = head;

        // find the new tail node
        ListNode* new_tail = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            new_tail = new_tail->next;
        }

        // find the new head node
        ListNode* new_head = new_tail->next;

        // break the cycle
        new_tail->next = nullptr;

        return new_head;
    }
};
```

## Test Cases
```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```

## Key Takeaways
- The key to solving this problem is to first find the length of the linked list and then connect the last node to the head to form a circular linked list.
- We then find the new tail node which is at (length - k % length - 1)th position, and the node next to it will be the new head of the rotated list.
- The use of modulo operation (k % n) ensures that we handle cases where k is greater than the length of the list.