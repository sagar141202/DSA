# Rotate List

## Problem Statement
Given the head of a linked list, rotate the list to the right by k places. The number of nodes in the list is in the range [0, 100]. 0 <= k <= 105. It is guaranteed that the number of nodes in the list is in the range [0, 100], so there's no need to worry about integer overflow when calculating the actual number of places to rotate. For example, if we have a list 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list should be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
We will first calculate the length of the linked list. Then, we'll connect the last node to the head to form a circular linked list. After that, we'll calculate the new tail node's position and break the circular linked list at that point to get the rotated list.

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
        
        // calculate the length of the linked list
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n += 1;
        }
        
        // connect the last node to the head
        old_tail->next = head;
        
        // calculate the new tail node's position
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
- The key to solving this problem is to first calculate the length of the linked list and then connect the last node to the head to form a circular linked list.
- We use the modulo operator to handle cases where k is greater than the length of the linked list.
- The time complexity is O(n) because we only need to traverse the linked list once to calculate its length and once to find the new tail node.