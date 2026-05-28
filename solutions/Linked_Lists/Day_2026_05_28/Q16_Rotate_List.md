# Rotate List

## Problem Statement
Given the head of a linked list, rotate the list to the right by k places. The number of nodes in the list is in the range [0, 100], 0 <= Node.val <= 100, and 0 <= k <= 100. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list should be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
The approach is to first find the length of the linked list, then connect the tail to the head to form a circular linked list. We then find the new tail and new head by moving (length - k % length) steps from the head.

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
        // base case: if the list is empty or only contains one node
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
        
        // connect the tail to the head to form a circular linked list
        old_tail->next = head;
        
        // find the new tail and new head
        ListNode* new_tail = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            new_tail = new_tail->next;
        }
        
        // find the new head
        ListNode* new_head = new_tail->next;
        
        // break the circular linked list
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
- We need to handle the case where k is greater than the length of the list by taking the modulus of k with the length of the list.
- We use a circular linked list to simplify the rotation process.
- We need to break the circular linked list after finding the new head and new tail.