# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null. The linked list has at least one node, and all the values of the node are unique. The cycle is defined as a node that has a next pointer pointing to a previous node in the list. For example, given the head of a linked list with a cycle as [3,2,0,-4], where the cycle starts at node with value -4, the function should return the node with value -4.

## Approach
The algorithm uses Floyd's Tortoise and Hare (Cycle Detection) to detect the presence of a cycle, then finds the start of the cycle by moving one pointer to the head and keeping the other at the meeting point, then moving both pointers one step at a time.

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
            hare = hare->next->next;   // Move two steps at a time
            if (tortoise == hare) {
                break;
            }
        }
        
        // If no cycle is found
        if (hare == NULL || hare->next == NULL) {
            return NULL;
        }
        
        // Phase 2: Finding the start of the cycle
        tortoise = head;  // Move one pointer to the head
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
Input: head = [3,2,0,-4], where the cycle starts at node with value -4
Output: The node with value -4
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- After detecting the cycle, we can find the start of the cycle by moving one pointer to the head and keeping the other at the meeting point, then moving both pointers one step at a time.
- The time complexity of this solution is O(n), where n is the number of nodes in the linked list, and the space complexity is O(1), as we only use a constant amount of space.