# Rotate List

## Problem Statement
Given the head of a list and an integer k, rotate the list to the right by k places. The list is considered to be a circular list, so if k is greater than the length of the list, we can rotate it by k % length places. For example, if we have the list 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list should be 4 -> 5 -> 1 -> 2 -> 3. If k = 7, the rotated list should be the same as when k = 2, because 7 % 5 = 2.

## Approach
We can solve this problem by first finding the length of the list and the new tail of the rotated list. Then, we can rotate the list by changing the next pointer of the new tail to None and the next pointer of the old tail to the old head. We also need to update the head of the list to the new head.

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
        if (!head || !head->next) return head;
        
        // find the length of the list and the new tail
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n++;
        }
        
        // connect the old tail to the old head to form a circular list
        old_tail->next = head;
        
        // find the new tail
        ListNode* new_tail = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            new_tail = new_tail->next;
        }
        
        // find the new head
        ListNode* new_head = new_tail->next;
        
        // break the circular list at the new tail
        new_tail->next = NULL;
        
        // return the new head
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
- To rotate a linked list, we need to find the new tail and the new head of the rotated list.
- We can use a circular list to simplify the rotation process.
- The time complexity of this solution is O(n), where n is the length of the list.