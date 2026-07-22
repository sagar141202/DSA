# Rotate List

## Problem Statement
Given the head of a list and an integer k, rotate the list to the right by k places. The list is considered to be a circular list, meaning that the last node is connected to the first node. If k is greater than the length of the list, the list is rotated by k % length places. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and k is 2, the rotated list should be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
The algorithm involves finding the length of the list, connecting the last node to the first node, and then finding the new tail node at the (length - k % length - 1)th position. The new head node is the next node of the new tail node.

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
        if (!head || !head->next || k == 0) {
            return head;
        }
        
        // find the length of the list and the last node
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n += 1;
        }
        
        // connect the last node to the first node
        old_tail->next = head;
        
        // find the new tail node
        ListNode* new_tail = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            new_tail = new_tail->next;
        }
        
        // find the new head node
        ListNode* new_head = new_tail->next;
        
        // disconnect the new tail node and the new head node
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
- To rotate a linked list, we need to find the length of the list and connect the last node to the first node.
- We can then find the new tail node and the new head node based on the given rotation value k.
- The time complexity of the algorithm is O(n), where n is the length of the list, and the space complexity is O(1) since we only use a constant amount of space.