# Rotate List

## Problem Statement
Given the head of a list and an integer `k`, rotate the list to the right by `k` places. The list is considered to be a circular linked list, so if `k` is greater than the length of the list, we can take the modulus of `k` with the length of the list to get the effective number of rotations. For example, if we have the list `1 -> 2 -> 3 -> 4 -> 5` and `k = 2`, the rotated list should be `4 -> 5 -> 1 -> 2 -> 3`. If `k = 7`, the rotated list should still be `4 -> 5 -> 1 -> 2 -> 3` because `7 % 5 = 2`.

## Approach
We can solve this problem by first finding the length of the list and the last node, then connecting the last node to the head to form a circular linked list. We then find the new tail node by moving `length - k % length - 1` steps from the head. The node after the new tail node will be the new head.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
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
        if (!head || !head->next || k == 0) {
            return head;
        }
        
        // find the length and the last node
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
        
        // break the circular linked list
        new_tail->next = NULL;
        
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
- We need to consider the case where `k` is greater than the length of the list.
- We can use the modulus operator to find the effective number of rotations.
- We can solve this problem by first finding the length of the list and the last node, then connecting the last node to the head to form a circular linked list.