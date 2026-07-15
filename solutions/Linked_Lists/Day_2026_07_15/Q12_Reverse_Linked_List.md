# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The linked list can have any number of nodes, and each node has a value and a pointer to the next node. The function should take the head of the list as input and return the head of the reversed list. For example, if the input list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 5 -> 4 -> 3 -> 2 -> 1. The list can be empty, and the function should handle this case correctly.

## Approach
The algorithm uses a three-pointer approach to reverse the linked list. It initializes three pointers: previous, current, and next. It iterates through the list, reversing the next pointer of each node. The function returns the new head of the reversed list.

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
        // Initialize three pointers: previous, current, and next
        ListNode* prev = NULL;
        ListNode* curr = head;
        ListNode* next = NULL;

        // Iterate through the list
        while (curr != NULL) {
            // Store the next node
            next = curr->next;

            // Reverse the next pointer
            curr->next = prev;

            // Move the pointers one step forward
            prev = curr;
            curr = next;
        }

        // Return the new head of the reversed list
        return prev;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1

Input: 
Output: 

Input: 1
Output: 1
```

## Key Takeaways
- The three-pointer approach is useful for reversing linked lists.
- The function should handle the case where the input list is empty.
- The time complexity is O(n), where n is the number of nodes in the list, because we only iterate through the list once.