# Rotate List

## Problem Statement
Given the head of a list and an integer `k`, rotate the list to the right by `k` places. The list is considered to be a circular list, so if `k` is greater than the length of the list, the rotation will be equivalent to `k % n`, where `n` is the length of the list. For example, if the list is `1 -> 2 -> 3 -> 4 -> 5` and `k = 2`, the rotated list will be `4 -> 5 -> 1 -> 2 -> 3`. The list node is defined as `struct ListNode { int val; ListNode *next; ListNode() : val(0), next(nullptr) {} }`.

## Approach
To solve this problem, we can use a two-pointer approach, where one pointer reaches the end of the list and the other pointer is `k` steps behind. We can then reconnect the nodes to form the rotated list. The key idea is to find the new tail of the rotated list and the new head.

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
        if (!head || !head->next || k == 0) return head;
        
        // find the length of the list
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n++;
        }
        
        // connect the list to form a ring
        old_tail->next = head;
        
        // find the new tail
        ListNode* new_tail = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            new_tail = new_tail->next;
        }
        
        // find the new head
        ListNode* new_head = new_tail->next;
        
        // break the ring
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
- The rotation can be done in O(n) time complexity by finding the length of the list and reconnecting the nodes.
- We need to handle the case where `k` is greater than the length of the list by taking `k % n`.
- The list is considered to be a circular list, so we need to connect the last node to the first node to form a ring before rotating.