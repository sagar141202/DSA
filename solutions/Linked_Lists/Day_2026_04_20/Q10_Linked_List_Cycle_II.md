# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list is defined by a ListNode class, where each node has an integer val and a pointer next to the next node. The cycle is defined as a node that points back to a previous node. For example, given the linked list 3 -> 2 -> 0 -> -4 -> 2, where the last node (2) points back to the second node (2), the function should return the node with value 2. If the linked list is 1 -> 2, where there is no cycle, the function should return nullptr.

## Approach
The algorithm uses the Floyd's Tortoise and Hare (Cycle Detection) approach to detect the cycle in the linked list. Once the cycle is detected, it uses the meeting point to find the start of the cycle. This approach ensures that the solution has a linear time complexity.

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
            tortoise = tortoise->next;  // Move one step at a time
            hare = hare->next->next;    // Move two steps at a time
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
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Input: head = [1], pos = -1
Output: no cycle
```

## Key Takeaways
- The Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- Once a cycle is detected, the meeting point can be used to find the start of the cycle.
- This approach has a linear time complexity and constant space complexity.