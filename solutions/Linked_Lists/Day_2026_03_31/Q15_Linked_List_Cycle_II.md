# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null. The linked list has at least one node, and all the values in the linked list are unique. The cycle is guaranteed to have at least one node, and the node with the beginning of the cycle must be in the list. For example, given the linked list 3 -> 2 -> 0 -> -4 -> 2, the function should return the node with value 2, because it is where the cycle begins.

## Approach
The algorithm uses the Floyd's Tortoise and Hare (Cycle Detection) approach to detect the cycle, then moves one of the pointers to the head and keeps the other pointer at the meeting point, moving both one step at a time to find the start of the cycle. This approach works because the distance from the head to the start of the cycle is equal to the distance from the meeting point to the start of the cycle.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
Output: returned node with value 2
```

## Key Takeaways
- We use Floyd's Tortoise and Hare algorithm to detect the cycle in the linked list.
- Once the cycle is detected, we move one of the pointers to the head and keep the other pointer at the meeting point, then move both one step at a time to find the start of the cycle.
- The algorithm has a time complexity of O(n) and a space complexity of O(1).