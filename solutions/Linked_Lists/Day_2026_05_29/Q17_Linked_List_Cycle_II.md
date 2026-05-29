# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list is guaranteed to have at most one cycle. The cycle can start at any node, and the cycle can be of any length. For example, given the linked list 3 -> 2 -> 0 -> -4 -> 2, the cycle begins at the node with value 2.

## Approach
We will use the Floyd's Tortoise and Hare algorithm to detect the cycle and then find the start of the cycle by moving the slow pointer to the head and keeping the fast pointer at the meeting point.

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
        // phase 1: detect cycle using Floyd's Tortoise and Hare algorithm
        ListNode *tortoise = head;
        ListNode *hare = head;
        while (hare != nullptr && hare->next != nullptr) {
            tortoise = tortoise->next;
            hare = hare->next->next;
            if (tortoise == hare) {
                break;
            }
        }
        
        // if no cycle, return nullptr
        if (hare == nullptr || hare->next == nullptr) {
            return nullptr;
        }
        
        // phase 2: find start of cycle
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
- Use Floyd's Tortoise and Hare algorithm to detect cycle in linked list.
- Move slow pointer to head and keep fast pointer at meeting point to find start of cycle.
- Be careful with edge cases where there is no cycle or the cycle starts at the head.