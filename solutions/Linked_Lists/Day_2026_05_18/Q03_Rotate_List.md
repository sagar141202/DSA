# Rotate List

## Problem Statement
Given the head of a linked list, rotate the list to the right by k places. The number of nodes in the list is in the range [0, 100]. 0 <= Node.val <= 100. 0 <= k <= 105. It is guaranteed that the number of nodes in the list is in the range [0, 100] and 0 <= k <= 10^5. For example, if we have the list 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list will be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
We can solve this problem by first connecting the last node to the head of the list, forming a circular linked list. Then, we find the new tail of the list, which is the (length - k % length - 1)th node. We break the cycle at this node, and the next node becomes the new head of the rotated list.

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
        
        // Find the length of the list and the last node
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n++;
        }
        
        // Connect the last node to the head
        old_tail->next = head;
        
        // Find the new tail
        ListNode* new_tail = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            new_tail = new_tail->next;
        }
        
        // Find the new head
        ListNode* new_head = new_tail->next;
        
        // Break the cycle
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
- We can use a two-pointer approach to find the new tail and head of the rotated list.
- We need to break the cycle at the new tail to form the rotated list.