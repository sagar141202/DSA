# Linked List Cycle II

## Problem Statement
Given a linked list, return the node where the cycle begins. If there is no cycle, return null. The linked list is defined by a ListNode class, where each node has an integer value and a pointer to the next node. The cycle is defined as a node that points back to a previous node. For example, given the linked list 4 -> 1 -> 8 -> 4 -> 5, the function should return the node with value 8, because 5 points back to the node with value 8, creating a cycle. If the linked list is 1 -> 2 -> 3 -> 4, the function should return null, because there is no cycle.

## Approach
We will use the Floyd's Tortoise and Hare algorithm to detect the cycle and then find the start of the cycle. The algorithm uses two pointers, one moving twice as fast as the other, to detect the cycle. Once the cycle is detected, we move one of the pointers to the start of the linked list and move both pointers at the same speed to find the start of the cycle.

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
        
        // If no cycle is found, return NULL
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
Input: 4 -> 1 -> 8 -> 4 -> 5 (where 5 points back to the node with value 8)
Output: The node with value 8
Input: 1 -> 2 -> 3 -> 4
Output: NULL
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- The algorithm uses two pointers moving at different speeds to detect the cycle.
- Once the cycle is detected, moving one of the pointers to the start of the linked list and moving both pointers at the same speed can help find the start of the cycle.