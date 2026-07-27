# Rotate List

## Problem Statement
Given the head of a list and an integer k, rotate the list to the right by k places. The rotation should be performed in-place, i.e., without using any extra space. The list is considered to be a circular linked list, meaning the last node's next pointer points to the head of the list. If k is greater than the length of the list, the rotation is equivalent to rotating the list by k % length places. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list should be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
The approach is to first find the length of the list and connect the last node to the head to form a circular linked list. Then, find the new tail node which is (length - k % length - 1) nodes from the head. Finally, break the circular linked list at the new tail node and return the new head.

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
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n += 1;
        }
        
        // connect the last node to the head to form a circular linked list
        old_tail->next = head;
        
        // find the new tail node
        ListNode* new_tail = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            new_tail = new_tail->next;
        }
        
        // find the new head node
        ListNode* new_head = new_tail->next;
        
        // break the circular linked list at the new tail node
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
- To rotate a linked list, we need to find the length of the list and connect the last node to the head to form a circular linked list.
- We can find the new tail node by moving (length - k % length - 1) nodes from the head.
- We can break the circular linked list at the new tail node to get the rotated list.