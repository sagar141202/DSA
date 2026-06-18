# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list has at least one node and may have a cycle. The length of the linked list is not known in advance. For example, given the linked list 3 -> 2 -> 0 -> -4 -> 2, the cycle begins at the node with value 2.

## Approach
The algorithm uses Floyd's Tortoise and Hare (Cycle Detection) approach to detect the cycle, then moves one pointer back to the start and keeps the other pointer at the meeting point, moving both one step at a time to find the cycle start.

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
        bool cycleDetected = false;
        while (hare != nullptr && hare->next != nullptr) {
            tortoise = tortoise->next;  // Move one step at a time
            hare = hare->next->next;     // Move two steps at a time
            if (tortoise == hare) {
                cycleDetected = true;
                break;
            }
        }
        
        if (!cycleDetected) {
            return nullptr;  // No cycle detected
        }
        
        // Phase 2: Finding the start of the cycle
        tortoise = head;  // Move one pointer back to the start
        while (tortoise != hare) {
            tortoise = tortoise->next;  // Move both pointers one step at a time
            hare = hare->next;
        }
        
        return tortoise;  // Return the node where the cycle begins
    }
};
```

## Test Cases
```
Input: head = [3,2,0,-4], pos = 1
Output: The node where the cycle begins is the node with value 2.
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- Once a cycle is detected, moving one pointer back to the start and keeping the other pointer at the meeting point, then moving both one step at a time will lead to the start of the cycle.
- This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large linked lists.