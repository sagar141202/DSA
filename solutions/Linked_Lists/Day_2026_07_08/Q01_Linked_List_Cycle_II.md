# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null. The linked list has at least one node and may have a cycle. If a cycle exists, the cycle must start from one of the nodes in the list. The nodes in the list are numbered from 1 to n, where n is the number of nodes in the list. We define the node number as the position of the node in the list, starting from 1 (i.e., head is node 1). We assume that the node numbers are consecutive and increasing. For example, given the linked list 3 -> 2 -> 0 -> -4 -> 3, the function should return the node with value 3, because the cycle begins at this node.

## Approach
The approach is to use Floyd's Tortoise and Hare algorithm to detect the cycle and then find the start of the cycle. We use two pointers that move at different speeds to detect the cycle. Once the cycle is detected, we reset one of the pointers to the start of the list and move both pointers at the same speed to find the start of the cycle.

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
        if (head == NULL || head->next == NULL) return NULL;
        
        // Detect cycle using Floyd's Tortoise and Hare algorithm
        ListNode *tortoise = head;
        ListNode *hare = head;
        while (hare != NULL && hare->next != NULL) {
            tortoise = tortoise->next;
            hare = hare->next->next;
            if (tortoise == hare) break;
        }
        
        if (hare == NULL || hare->next == NULL) return NULL;
        
        // Find start of cycle
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
- Use Floyd's Tortoise and Hare algorithm to detect the cycle in a linked list.
- Once the cycle is detected, reset one of the pointers to the start of the list and move both pointers at the same speed to find the start of the cycle.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), where n is the number of nodes in the linked list.