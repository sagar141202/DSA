# Rotate List

## Problem Statement
Given the head of a list and an integer k, rotate the list to the right by k places. The rotation should be performed in-place, i.e., without creating a new list. If k is greater than the length of the list, the rotation should be equivalent to k modulo the length of the list. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list should be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
We can solve this problem by first finding the length of the list and the new tail node. Then, we can connect the new tail node to nullptr and the old tail node to the head node. This approach ensures that the rotation is performed in-place and handles cases where k is greater than the length of the list.

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
        // Base cases
        if (!head || !head->next || k == 0) {
            return head;
        }
        
        // Find the length of the list and the new tail node
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n++;
        }
        
        // Connect the old tail node to the head node
        old_tail->next = head;
        
        // Find the new tail node
        ListNode* new_tail = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            new_tail = new_tail->next;
        }
        
        // Find the new head node
        ListNode* new_head = new_tail->next;
        
        // Connect the new tail node to nullptr
        new_tail->next = nullptr;
        
        return new_head;
    }
};
```

## Test Cases
```
Input: head = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]
Input: head = [1, 2, 3, 4, 5], k = 5
Output: [1, 2, 3, 4, 5]
```

## Key Takeaways
- We need to handle cases where k is greater than the length of the list by taking k modulo the length of the list.
- The rotation should be performed in-place, i.e., without creating a new list.
- We can use a two-pointer approach to find the new tail node and the new head node.