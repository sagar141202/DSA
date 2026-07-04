# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list has at least one node, and all the values are unique. The cycle begins at some node, which means that the next pointer of that node points to a previous node.

## Approach
We can use the Floyd's Tortoise and Hare algorithm to detect the cycle, then move one of the pointers back to the head of the list and keep the other pointer at the meeting point. Finally, we move both pointers one step at a time and return the node where they meet again, which is the start of the cycle.

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
        while (hare != nullptr && hare->next != nullptr) {
            tortoise = tortoise->next;
            hare = hare->next->next;
            if (tortoise == hare) {
                break;
            }
        }
        
        // If no cycle is found, return nullptr
        if (hare == nullptr || hare->next == nullptr) {
            return nullptr;
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
- After detecting the cycle, we can find the start of the cycle by moving one of the pointers back to the head of the list and keeping the other pointer at the meeting point.
- We can then move both pointers one step at a time and return the node where they meet again, which is the start of the cycle.