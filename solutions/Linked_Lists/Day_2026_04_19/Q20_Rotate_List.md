# Rotate List

## Problem Statement
Given the head of a list and an integer k, rotate the list to the right by k places. The rotation should be performed in-place, i.e., without using any extra space. The list is considered to be a circular list, i.e., the last node is connected to the first node. If k is greater than the length of the list, the rotation should be performed k mod n times, where n is the length of the list. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list should be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
The algorithm involves first finding the length of the list and the last node, then connecting the last node to the head to form a circular list. We then find the new tail node by moving (length - k % length - 1) steps from the head. The node next to the new tail node becomes the new head.

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
        // base case: if the list is empty or only contains one node
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
        
        // find the new tail node
        ListNode* new_tail = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            new_tail = new_tail->next;
        }
        
        // find the new head node
        ListNode* new_head = new_tail->next;
        
        // break the circular list at the new tail node
        new_tail->next = NULL;
        
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
- The key to this problem is to first connect the last node to the head to form a circular list, which allows us to handle cases where k is greater than the length of the list.
- We then find the new tail node by moving (length - k % length - 1) steps from the head, and the node next to the new tail node becomes the new head.
- The time complexity is O(n) because we need to traverse the list to find the length and the last node, and the space complexity is O(1) because we only use a constant amount of space to store the new tail and head nodes.