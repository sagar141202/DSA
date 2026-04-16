# Linked List Cycle II

## Problem Statement
Given a linked list, return the node where the cycle begins. If there is no cycle, return null. To detect a cycle, we can use Floyd's Tortoise and Hare algorithm. However, finding the start of the cycle requires additional steps. The linked list is defined as a sequence of nodes, where each node has an integer value and a pointer to the next node. The cycle is defined as a node that points back to a previous node in the list. For example, the list 3 -> 2 -> 0 -> -4 -> 2 has a cycle starting at node 2, while the list 1 -> 2 has no cycle.

## Approach
The algorithm involves first detecting the cycle using Floyd's Tortoise and Hare algorithm, then finding the start of the cycle by moving one pointer to the head of the list and moving both pointers one step at a time. The node where the two pointers meet is the start of the cycle. This approach works because the distance from the head of the list to the start of the cycle is equal to the distance from the meeting point to the start of the cycle.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
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
            tortoise = tortoise->next;
            hare = hare->next->next;
            if (tortoise == hare) {
                break;
            }
        }
        
        // If there is no cycle
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
Input: head = [3,2,0,-4], pos = 1 (node 2)
Output: The node with value 2
Input: head = [1,2], pos = 0 (node 1)
Output: The node with value 1
Input: head = [1], pos = -1 (no cycle)
Output: NULL
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect a cycle in a linked list.
- To find the start of the cycle, we need to move one pointer to the head of the list and move both pointers one step at a time.
- The node where the two pointers meet is the start of the cycle.