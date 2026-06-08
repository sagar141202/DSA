# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list has at least one node, and all the values of the node are unique. For example, given a linked list of 3 -> 2 -> 0 -> -4 -> 2, where the last node (2) is connected to the second node (2), the function should return the node with value 2.

## Approach
The algorithm uses the Floyd's Tortoise and Hare (Cycle Detection) approach to detect the cycle and then finds the start of the cycle. It uses two pointers, slow and fast, to traverse the linked list. If a cycle is detected, it resets one of the pointers to the head and moves both pointers one step at a time to find the start of the cycle.

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
        
        // Phase 2: Finding the start of the cycle
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
Input: head = [3,2,0,-4], pos = 1
Output: node with value 2
```

## Key Takeaways
- The Floyd's Tortoise and Hare algorithm can be used to detect a cycle in a linked list.
- Once a cycle is detected, we can find the start of the cycle by resetting one of the pointers to the head and moving both pointers one step at a time.
- The time complexity of the solution is O(n), where n is the number of nodes in the linked list, and the space complexity is O(1) as we only use a constant amount of space.