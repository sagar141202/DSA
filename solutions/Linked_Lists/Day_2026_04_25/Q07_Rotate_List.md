# Rotate List

## Problem Statement
Given the head of a list and an integer k, rotate the list to the right by k places. The list is considered to be a circular list, so if k is greater than the length of the list, we can take the modulus of k with the length of the list to get the effective number of rotations. For example, if we have a list [1,2,3,4,5] and k = 2, the rotated list would be [4,5,1,2,3]. If k = 7, the effective number of rotations would be 7 % 5 = 2, so the rotated list would still be [4,5,1,2,3].

## Approach
The algorithm involves first finding the length of the list and the last node of the list. Then, we connect the last node to the head of the list to form a circular list. Next, we find the new last node by moving (length - k % length - 1) steps from the head. Finally, we find the new head by moving one step from the new last node and break the circular list at the new last node.

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
        // base case: if the list is empty or only contains one node, return the head
        if (!head || !head->next) return head;

        // find the length of the list and the last node
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n += 1;
        }

        // connect the last node to the head to form a circular list
        old_tail->next = head;

        // find the new last node
        ListNode* new_tail = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            new_tail = new_tail->next;
        }

        // find the new head and break the circular list
        ListNode* new_head = new_tail->next;
        new_tail->next = nullptr;

        return new_head;
    }
};
```

## Test Cases
```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Input: head = [1,2,3,4,5], k = 7
Output: [4,5,1,2,3]
```

## Key Takeaways
- The key to solving this problem is to first find the length of the list and the last node, and then connect the last node to the head to form a circular list.
- We can take the modulus of k with the length of the list to get the effective number of rotations.
- The new last node can be found by moving (length - k % length - 1) steps from the head.