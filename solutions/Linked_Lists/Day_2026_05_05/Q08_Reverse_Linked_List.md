# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The linked list has a minimum of 1 node and a maximum of 5000 nodes. The list is defined as a sequence of nodes, where each node has a value and a pointer to the next node in the list. The task is to reverse the direction of the pointers to reverse the list.

## Approach
The approach involves initializing three pointers: previous, current, and next. We traverse the list, and for each node, we reverse the next pointer. This process continues until we reach the end of the list, at which point the previous pointer will be pointing to the new head of the reversed list.

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
    ListNode* reverseList(ListNode* head) {
        // Initialize previous, current, and next pointers
        ListNode* prev = NULL;
        ListNode* curr = head;
        ListNode* next = NULL;

        // Traverse the list
        while (curr != NULL) {
            // Store next node
            next = curr->next;
            
            // Reverse the next pointer
            curr->next = prev;
            
            // Move pointers one position ahead
            prev = curr;
            curr = next;
        }
        
        // At the end, 'prev' will be pointing to the new head
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
Input: [1]
Output: [1]
```

## Key Takeaways
- The key to solving this problem is to initialize three pointers: previous, current, and next.
- Traverse the list, and for each node, reverse the next pointer.
- At the end of the traversal, the previous pointer will be pointing to the new head of the reversed list.