# Linked List Cycle II

## Problem Statement
Given a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list is defined by a ListNode struct, where each node has an integer value and a pointer to the next node. The cycle is defined as a node that points back to a previous node. For example, given the linked list 3 -> 2 -> 0 -> -4 -> 2, where the last node (2) points back to the second node (2), the function should return the second node (2). If the input linked list is 1 -> 2 -> 3 -> 4, where there is no cycle, the function should return nullptr.

## Approach
The algorithm uses the Floyd's Tortoise and Hare (Cycle Detection) approach to detect the cycle in the linked list. It uses two pointers, a slow pointer and a fast pointer, to traverse the linked list. If a cycle is detected, it resets the slow pointer to the head of the linked list and moves both pointers one step at a time to find the node where the cycle begins.

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
    ListNode *detectCycle(ListNode *head) {
        // Phase 1: Detecting the cycle using Floyd's Tortoise and Hare algorithm
        ListNode *tortoise = head;
        ListNode *hare = head;
        while (hare != NULL && hare->next != NULL) {
            tortoise = tortoise->next;
            hare = hare->next->next;
            if (tortoise == hare) {
                break;
            }
        }
        
        // If no cycle is detected
        if (hare == NULL || hare->next == NULL) {
            return NULL;
        }
        
        // Phase 2: Finding the starting point of the cycle
        tortoise = head;
        while (tortoise != hare) {
            tortoise = tortoise->next;
            hare = hare->next;
        }
        
        return tortoise;
    }
};
```

## Test Cases
```
Input: 3 -> 2 -> 0 -> -4 -> 2 (where the last node points back to the second node)
Output: The second node (2)
Input: 1 -> 2 -> 3 -> 4 (where there is no cycle)
Output: nullptr
```

## Key Takeaways
- The Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- Once a cycle is detected, resetting one of the pointers to the head of the linked list and moving both pointers one step at a time can help find the starting point of the cycle.
- This solution has a time complexity of O(n) and a space complexity of O(1), where n is the number of nodes in the linked list.