# Rotate List

## Problem Statement
Given the head of a linked list, rotate the list to the right by k places. The number of nodes in the list is in the range [0, 5000]. The value of each node is in the range [-5000, 5000]. k is a non-negative integer that represents the number of places to rotate the list to the right. If the list is empty or only contains one node, or k is 0, the list remains unchanged. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list should be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
The approach is to first find the length of the linked list and the last node. Then, connect the last node to the head to form a circular list. Finally, find the new tail node and the new head node, and break the circular list at the new tail node. The new head node will be the head of the rotated list.

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
        // if the list is empty or only contains one node, or k is 0, return the head
        if (!head || !head->next || k == 0) {
            return head;
        }
        
        // find the length of the linked list and the last node
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n++;
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
        new_tail->next = nullptr;
        
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
- The key to solving this problem is to first find the length of the linked list and the last node.
- Then, connect the last node to the head to form a circular list.
- Finally, find the new tail node and the new head node, and break the circular list at the new tail node.