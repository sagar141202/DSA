# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The linked list can have any number of nodes, and each node has a value and a pointer to the next node. The function should return the head of the reversed linked list. For example, if the input linked list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 5 -> 4 -> 3 -> 2 -> 1. The function should handle cases where the input linked list is empty or has only one node.

## Approach
We can solve this problem by iterating through the linked list and reversing the next pointer of each node. We will use three pointers to keep track of the current node, the previous node, and the next node. The algorithm will iterate through the list until it reaches the end, at which point the previous pointer will be the head of the reversed list.

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
        // Initialize three pointers
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* next = nullptr;

        // Iterate through the list
        while (curr != nullptr) {
            // Store the next node
            next = curr->next;
            // Reverse the next pointer
            curr->next = prev;
            // Move the pointers
            prev = curr;
            curr = next;
        }

        // Return the head of the reversed list
        return prev;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1
Input: 1
Output: 1
Input: 
Output: 
```

## Key Takeaways
- We use three pointers to keep track of the current node, the previous node, and the next node.
- We iterate through the list until we reach the end, at which point the previous pointer will be the head of the reversed list.
- The time complexity is O(n), where n is the number of nodes in the list, and the space complexity is O(1) since we only use a constant amount of space.