# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list is defined as a sequence of nodes where each node has a value and a next pointer pointing to the next node in the sequence. A cycle occurs when a node's next pointer points back to a previous node. The cycle can start at any node, and the cycle can be of any length. For example, given the linked list 3 -> 2 -> 0 -> -4 -> 2, the function should return the node with value 2, because the cycle starts at this node.

## Approach
We can use the Floyd's Tortoise and Hare algorithm to detect the cycle in the linked list. Once the cycle is detected, we can find the start of the cycle by moving one of the pointers to the head of the list and moving both pointers one step at a time.

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
        
        // If no cycle is detected, return nullptr
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
Input: head = [3,2,0,-4], pos = 1 (0-indexed)
Output: node with value 2
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- Once a cycle is detected, we can find the start of the cycle by moving one pointer to the head of the list and moving both pointers one step at a time.
- This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large linked lists.