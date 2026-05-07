# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list has at least one node, and all the values of the node are unique. The cycle is a connected component of the linked list that has more than one node. For example, given the linked list 3 -> 2 -> 0 -> -4 -> 2, the function should return the node with value 2, which is the node where the cycle begins.

## Approach
The algorithm uses Floyd's Tortoise and Hare algorithm to detect the cycle, then finds the start of the cycle by moving one pointer to the head and keeping the other at the meeting point, moving both one step at a time.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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
            tortoise = tortoise->next;  // move one step
            hare = hare->next->next;  // move two steps
            if (tortoise == hare) {
                break;
            }
        }
        
        // If no cycle is found
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
Input: head = [3,2,0,-4], pos = 1 (node with value 2 has a cycle)
Output: The node with value 2
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can detect a cycle in a linked list.
- To find the start of the cycle, move one pointer to the head and keep the other at the meeting point, then move both one step at a time.
- This solution has a time complexity of O(n) and a space complexity of O(1).