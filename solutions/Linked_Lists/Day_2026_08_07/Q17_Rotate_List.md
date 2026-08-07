# Rotate List

## Problem Statement
Given the head of a list and an integer k, rotate the list to the right by k places. The list is considered to be a circular list, so if k is greater than the length of the list, the rotation should be performed k mod n times, where n is the length of the list. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list should be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
The algorithm involves first calculating the length of the list, then connecting the last node to the head to form a circular list. We then find the new tail node by moving (n - k % n - 1) steps from the head, where n is the length of the list. The node next to the new tail node becomes the new head, and we break the circular list at the new tail node.

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
        // Handle edge cases
        if (!head || !head->next || k == 0) {
            return head;
        }

        // Calculate the length of the list
        ListNode* current = head;
        int n = 1;
        while (current->next) {
            current = current->next;
            n++;
        }

        // Connect the last node to the head to form a circular list
        current->next = head;

        // Find the new tail node
        ListNode* newTail = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            newTail = newTail->next;
        }

        // Find the new head node
        ListNode* newHead = newTail->next;

        // Break the circular list at the new tail node
        newTail->next = nullptr;

        return newHead;
    }
};
```

## Test Cases
```
Input: head = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]
Input: head = [1, 2, 3, 4, 5], k = 5
Output: [1, 2, 3, 4, 5]
```

## Key Takeaways
- To rotate a linked list, we can first calculate its length and then connect the last node to the head to form a circular list.
- We can then find the new tail node by moving (n - k % n - 1) steps from the head, where n is the length of the list.
- The node next to the new tail node becomes the new head, and we break the circular list at the new tail node to get the rotated list.