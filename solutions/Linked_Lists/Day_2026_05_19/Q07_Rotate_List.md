# Rotate List

## Problem Statement
Given the head of a linked list, rotate the list to the right by k places. The number of nodes in the list is in the range [0, 100]. 0 <= Node.val <= 100. 0 <= k <= 105. It is guaranteed that the number k is non-negative. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list should be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
To solve this problem, we can use a two-pointer approach to find the new tail of the list after rotation. Then, we can connect the new tail to NULL and the old tail to the old head to complete the rotation. We also need to handle the case where k is greater than the length of the list.

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
        // base case: if the list is empty or only has one node
        if (!head || !head->next) return head;

        // find the length of the list
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n += 1;
        }

        // connect the old tail to the old head
        old_tail->next = head;

        // find the new tail
        ListNode* new_tail = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            new_tail = new_tail->next;
        }

        // find the new head
        ListNode* new_head = new_tail->next;

        // disconnect the new tail and the new head
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
- We can use a two-pointer approach to find the new tail of the list after rotation.
- We need to disconnect the new tail and the new head to complete the rotation.