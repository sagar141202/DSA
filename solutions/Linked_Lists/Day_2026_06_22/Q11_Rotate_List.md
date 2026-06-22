# Rotate List

## Problem Statement
Given the head of a list and an integer k, rotate the list to the right by k places. The list is considered to be a circular list, so if k is greater than the length of the list, the rotation will be performed for k % length places. For example, given the list 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list will be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
We will first calculate the length of the list, then connect the last node to the head to form a circular list. We will then find the new tail node which is (length - k % length - 1) nodes from the head, and the new head node which is (length - k % length) nodes from the head. We will then break the circular list at the new tail node to get the rotated list.

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

        // calculate the length of the list
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n += 1;
        }

        // connect the last node to the head
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
- The key to solving this problem is to first calculate the length of the list and then connect the last node to the head to form a circular list.
- We can then find the new tail node and the new head node based on the length of the list and the value of k.
- Finally, we can break the circular list at the new tail node to get the rotated list.