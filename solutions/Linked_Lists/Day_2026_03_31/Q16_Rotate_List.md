# Rotate List

## Problem Statement
Given the head of a linked list, rotate the list to the right by k places. The list is considered to be a circular list, meaning that the last node is connected to the first node. The number of nodes in the list will be in the range [0, 100]. Each node will have a unique value in the range [-500, 500]. The value of k will be in the range [0, 100]. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list will be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
The approach is to first find the length of the linked list and connect the last node to the head to form a circular list. Then, find the new tail node by moving (length - k % length - 1) steps from the head. The node next to the new tail node will be the new head. Update the head and tail pointers accordingly.

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
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        // base case: if the list is empty or only has one node, return the head
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

        // connect the last node to the head to form a circular list
        old_tail->next = head;

        // find the new tail node
        ListNode* new_tail = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            new_tail = new_tail->next;
        }

        // find the new head node
        ListNode* new_head = new_tail->next;

        // break the circular list at the new tail node
        new_tail->next = NULL;

        // return the new head node
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
- The key to solving this problem is to first form a circular list and then find the new tail node.
- The new tail node is found by moving (length - k % length - 1) steps from the head.
- The new head node is the node next to the new tail node.
- The time complexity is O(n) because we need to traverse the list to find the length and the new tail node.