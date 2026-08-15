# Rotate List

## Problem Statement
Given the head of a list and an integer k, rotate the list to the right by k places. The list is considered to be a circular list, so if k is greater than the length of the list, the rotation will be equivalent to k modulo the length of the list. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list will be 4 -> 5 -> 1 -> 2 -> 3. If the list is empty or only contains one node, the function should return the original list.

## Approach
The algorithm involves first finding the length of the list and connecting the last node to the head to form a circular list. Then, we find the new tail node by moving (length - k % length - 1) steps from the head. Finally, we break the circular list at the new tail node and return the new head.

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
        // base cases
        if (!head || !head->next || k == 0) return head;

        // find the length of the list and the last node
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
- The key to solving this problem is to first connect the last node to the head to form a circular list.
- We then find the new tail node by moving (length - k % length - 1) steps from the head.
- Finally, we break the circular list at the new tail node and return the new head.
- This solution has a time complexity of O(n) and a space complexity of O(1), where n is the length of the list.