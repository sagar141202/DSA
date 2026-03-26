# Rotate List

## Problem Statement
Given the head of a linked list, rotate the list to the right by k places. The list is considered to be circular, meaning the last node's next pointer points to the first node. If k is greater than the length of the list, the rotation is done by k mod n, where n is the length of the list. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list should be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
We can solve this problem by first finding the length of the linked list, then connecting the last node to the head to form a circular linked list. We then find the new tail node by moving (length - k % length - 1) steps from the head. The node next to the new tail node will be the new head.

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
- The key to solving this problem is to first form a circular linked list by connecting the last node to the head.
- We then find the new tail node by moving (length - k % length - 1) steps from the head.
- The node next to the new tail node will be the new head of the rotated list.