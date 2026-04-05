# Rotate List

## Problem Statement
Given the head of a list and an integer k, rotate the list to the right by k places. The list is considered to be a circular list, so if k is greater than the length of the list, the rotation will be equivalent to k modulo the length of the list. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list will be 4 -> 5 -> 1 -> 2 -> 3. If the list is empty or only contains one node, the function should return the original list.

## Approach
To solve this problem, we can first find the length of the list and connect the last node to the head to form a circular list. Then, we can calculate the new tail node's position and break the circular list at that point. The new head will be the next node of the new tail.

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
        // base case
        if (!head || !head->next || k == 0) return head;
        
        // find the length of the list and the last node
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n++;
        }
        
        // connect the last node to the head
        old_tail->next = head;
        
        // find the new tail
        ListNode* new_tail = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            new_tail = new_tail->next;
        }
        
        // find the new head
        ListNode* new_head = new_tail->next;
        
        // break the circular list
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
- Connect the last node to the head to form a circular list to simplify the rotation process.
- Calculate the new tail node's position using the length of the list and k modulo the length of the list.
- Break the circular list at the new tail node to get the rotated list.