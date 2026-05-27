# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list has at least one node, and all the values in the linked list are unique. The cycle is defined as a node that is visited more than once.

## Approach
The algorithm uses the Floyd's Tortoise and Hare (Cycle Detection) approach to detect the cycle, then uses the meeting point to find the start of the cycle. The tortoise moves one step at a time, while the hare moves two steps at a time.

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
        if (head == nullptr || head->next == nullptr) {
            return nullptr;
        }
        
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
        
        // If no cycle is found
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
- Once the cycle is detected, we can find the start of the cycle by moving the tortoise to the head and keeping the hare at the meeting point, then moving both one step at a time.
- This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large linked lists.