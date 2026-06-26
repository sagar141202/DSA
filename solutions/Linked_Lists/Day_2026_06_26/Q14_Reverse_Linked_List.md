# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes are numbered from 0 to n - 1. The list is defined as: 
0 -> 1 -> 2 -> ... -> n - 1. 
For example, if we have a linked list 1 -> 2 -> 3 -> 4 -> 5, the reversed linked list should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
We can solve this problem by iterating over the linked list and reversing the next pointer of each node. We will keep track of the previous node and update the next pointer of the current node to the previous node.

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
    ListNode* reverseList(ListNode* head) {
        // Initialize previous and current pointers
        ListNode* prev = nullptr;
        ListNode* curr = head;
        
        // Traverse the linked list
        while (curr != nullptr) {
            // Store the next node
            ListNode* nextTemp = curr->next;
            
            // Reverse the link
            curr->next = prev;
            
            // Move the pointers one step forward
            prev = curr;
            curr = nextTemp;
        }
        
        // Return the new head
        return prev;
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
Input: [1, 2]
Output: [2, 1]
Input: []
Output: []
```

## Key Takeaways
- Initialize three pointers: previous, current, and next to keep track of the nodes.
- Traverse the linked list, reversing the next pointer of each node.
- Update the head of the list to the new first node after reversing.