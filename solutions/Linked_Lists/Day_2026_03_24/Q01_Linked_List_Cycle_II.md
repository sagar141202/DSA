# Linked List Cycle II

## Problem Statement
Given a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list is defined by a ListNode class, where each node has an integer value and a pointer to the next node. The cycle is defined as a node that points back to a previous node. For example, given the linked list 3 -> 2 -> 0 -> -4 -> 2, the function should return the node with value 2, because the cycle begins at this node.

## Approach
The algorithm uses the Floyd's Tortoise and Hare (Cycle Detection) approach to detect the cycle in the linked list, then finds the start of the cycle by moving one pointer to the head and keeping the other at the meeting point, then moving both one step at a time.

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
        
        // If no cycle is found
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
Input: head = [3,2,0,-4], pos = 1 (0-indexed)
Output: The node with value 2
```

## Key Takeaways
- Use Floyd's Tortoise and Hare algorithm to detect the cycle in the linked list.
- After detecting the cycle, move one pointer to the head of the list and keep the other at the meeting point, then move both one step at a time to find the start of the cycle.
- This solution has a time complexity of O(n) and a space complexity of O(1), where n is the number of nodes in the linked list.