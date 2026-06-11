# Reverse Linked List

## Problem Statement
Reverse a singly linked list. The linked list is defined as a sequence of nodes, where each node contains an integer value and a pointer to the next node in the list. The task is to reverse the order of the nodes in the list, such that the last node becomes the first node, the second-to-last node becomes the second node, and so on. For example, given the linked list 1 -> 2 -> 3 -> 4 -> 5, the reversed linked list should be 5 -> 4 -> 3 -> 2 -> 1. The input linked list is defined by a pointer to the head node, and the output should also be a pointer to the head node of the reversed linked list. The linked list can contain up to 100 nodes, and each node's value is an integer between 1 and 100.

## Approach
The approach to solve this problem is to use a three-pointer technique, where we initialize three pointers: previous, current, and next. We traverse the linked list, and for each node, we update the next pointer of the current node to point to the previous node, effectively reversing the link. We then move the previous and current pointers one step forward.

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
        // Initialize previous pointer to NULL
        ListNode* prev = NULL;
        // Initialize current pointer to head
        ListNode* curr = head;
        // Traverse the linked list
        while (curr != NULL) {
            // Store the next node in a temporary pointer
            ListNode* nextTemp = curr->next;
            // Reverse the link
            curr->next = prev;
            // Move previous and current pointers one step forward
            prev = curr;
            curr = nextTemp;
        }
        // After traversal, previous pointer points to the new head
        return prev;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1
Input: 1 -> 2
Output: 2 -> 1
Input: 1
Output: 1
```

## Key Takeaways
- We use a three-pointer technique to reverse the linked list.
- The time complexity is O(n), where n is the number of nodes in the linked list.
- The space complexity is O(1), as we only use a constant amount of space to store the pointers.