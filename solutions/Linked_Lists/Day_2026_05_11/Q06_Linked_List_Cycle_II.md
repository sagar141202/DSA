# Linked List Cycle II

## Problem Statement
Given a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list is defined by a ListNode struct, where each node has an integer value and a next pointer. The cycle is defined as a node that points back to a previous node. For example, given the linked list 3 -> 2 -> 0 -> -4 -> 2, where the last node (2) points back to the second node (2), the function should return the node with value 2. The function has the following constraints: 1. The number of nodes in the list is in the range [0, 10^4]. 2. -10^5 <= Node.val <= 10^5. 3. pos is -1 or a valid index in the linked list.

## Approach
The algorithm uses the Floyd's Tortoise and Hare (Cycle Detection) approach to detect the cycle in the linked list, then uses the meeting point to find the start of the cycle. The approach involves two pointers, a slow pointer and a fast pointer, that move at different speeds through the list. When the fast pointer meets the slow pointer, we know there is a cycle.

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
            tortoise = tortoise->next; // Move one step at a time
            hare = hare->next->next; // Move two steps at a time
            if (tortoise == hare) {
                break;
            }
        }
        
        // If no cycle is found
        if (hare == NULL || hare->next == NULL) {
            return NULL;
        }
        
        // Phase 2: Finding the start of the cycle
        tortoise = head; // Reset the tortoise to the head
        while (tortoise != hare) {
            tortoise = tortoise->next; // Move one step at a time
            hare = hare->next; // Move one step at a time
        }
        
        return tortoise; // Return the node where the cycle begins
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
- The Floyd's Tortoise and Hare algorithm is used to detect the cycle in the linked list.
- Once the cycle is detected, the meeting point is used to find the start of the cycle.
- The time complexity of the solution is O(n), where n is the number of nodes in the linked list.