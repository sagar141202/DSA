# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list is guaranteed to have at most one cycle. The cycle can start at any node, and the nodes in the cycle can have any values. For example, given the linked list 3 -> 2 -> 0 -> -4 -> 2, the cycle begins at node 2.

## Approach
The algorithm uses Floyd's Tortoise and Hare (Cycle Detection) to detect the cycle and then finds the start of the cycle. It uses two pointers, a slow pointer and a fast pointer, to traverse the linked list. If a cycle exists, the fast pointer will eventually meet the slow pointer. Then, we reset the slow pointer to the head and move both pointers one step at a time to find the start of the cycle.

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
        if (head == NULL || head->next == NULL) {
            return NULL;
        }

        // Phase 1: Detecting the cycle using Floyd's Tortoise and Hare algorithm
        ListNode *tortoise = head;
        ListNode *hare = head;
        while (hare != NULL && hare->next != NULL) {
            tortoise = tortoise->next;  // Move one step at a time
            hare = hare->next->next;  // Move two steps at a time
            if (tortoise == hare) {
                break;
            }
        }

        if (hare == NULL || hare->next == NULL) {
            return NULL;  // No cycle
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
- Use Floyd's Tortoise and Hare algorithm to detect the cycle in the linked list.
- After detecting the cycle, reset one of the pointers to the head and move both pointers one step at a time to find the start of the cycle.
- If there is no cycle, the algorithm returns nullptr.