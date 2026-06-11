# Rotate List

## Problem Statement
Given the head of a linked list, rotate the list to the right by k places. The number of nodes in the list is in the range [0, 100], 0 <= k <= 2 * 10^5, and -100 <= Node.val <= 100. For example, if we have a list 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list will be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
The approach involves first finding the length of the linked list, then connecting the last node to the head to form a circular linked list. We then find the new tail node by moving (length - k % length - 1) steps from the head. The node next to the new tail will be the new head.

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
        // base cases
        if (!head || !head->next || k == 0) {
            return head;
        }

        // find the length of the list and the last node
        ListNode* current = head;
        int length = 1;
        while (current->next) {
            current = current->next;
            length++;
        }

        // connect the last node to the head
        current->next = head;

        // find the new tail node
        int newTailIndex = length - k % length - 1;
        ListNode* newTail = head;
        for (int i = 0; i < newTailIndex; i++) {
            newTail = newTail->next;
        }

        // find the new head node
        ListNode* newHead = newTail->next;

        // break the circular linked list
        newTail->next = nullptr;

        return newHead;
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
- To rotate a linked list, we can first find the length of the list and then connect the last node to the head to form a circular linked list.
- The new tail node can be found by moving (length - k % length - 1) steps from the head.
- The node next to the new tail will be the new head.