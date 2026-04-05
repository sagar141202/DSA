# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null. The linked list has at least one node, and all the nodes are non-negative. The nodes are numbered from 1 to n, and each node has a unique value. A cycle is defined as a node that points back to a previous node. For example, given the head of a linked list with a cycle: 3 -> 2 -> 0 -> -4 -> 2 (where the last node points back to the second node), the function should return the node with value 2. If no cycle exists, the function should return null.

## Approach
We can solve this problem by using the Floyd's Tortoise and Hare algorithm to detect the cycle, then finding the start of the cycle by moving the slow pointer to the head and keeping the fast pointer at the meeting point. We move both pointers one step at a time, and the point where they meet again is the start of the cycle.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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
            tortoise = tortoise->next;  // Move one step at a time
            hare = hare->next->next;     // Move two steps at a time
            if (tortoise == hare) {
                break;
            }
        }
        
        // If no cycle is found
        if (hare == NULL || hare->next == NULL) {
            return NULL;
        }
        
        // Phase 2: Finding the start of the cycle
        tortoise = head;  // Move the slow pointer to the head
        while (tortoise != hare) {
            tortoise = tortoise->next;  // Move one step at a time
            hare = hare->next;          // Move one step at a time
        }
        
        return tortoise;  // Return the node where the cycle begins
    }
};
```

## Test Cases
```
Input: head = [3,2,0,-4], and the last node points to the node with value 2
Output: The node with value 2
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- To find the start of the cycle, we need to move the slow pointer to the head and keep the fast pointer at the meeting point, then move both pointers one step at a time.
- The time complexity of this solution is O(n), where n is the number of nodes in the linked list, and the space complexity is O(1) since we only use a constant amount of space.