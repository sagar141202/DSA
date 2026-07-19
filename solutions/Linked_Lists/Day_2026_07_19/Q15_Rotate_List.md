# Rotate List

## Problem Statement
Given the head of a linked list, rotate the list to the right by k places. The number of nodes in the list is in the range [0, 100]. 0 <= k <= 105. It is guaranteed that the number of nodes in the list is in the range [0, 100], so you don't need to worry about the case where k is greater than the length of the list. For example, if we have the list 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list should be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
To solve this problem, we can use a two-pointer approach. First, we connect the last node to the head to form a circular linked list. Then, we calculate the new tail node's position and break the circular linked list at that point. The new head will be the next node of the new tail.

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
        // base case
        if (!head || !head->next || k == 0) {
            return head;
        }
        
        // find the length of the linked list
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n += 1;
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
- We need to handle the case where k is greater than the length of the list by taking k modulo the length of the list.
- Connecting the last node to the head to form a circular linked list simplifies the problem and allows us to find the new tail and head in a single pass.
- The time complexity is O(n) because we need to traverse the linked list to find its length and the new tail.