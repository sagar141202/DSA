# Linked List Cycle II

## Problem Statement
Given a linked list, return the node where the cycle begins. If there is no cycle, return null. The linked list is defined by a ListNode class, where each node has a value and a next pointer to the next node in the list. The cycle is defined as a node that points back to a previous node in the list. For example, given the list 3 -> 2 -> 0 -> -4 -> 2, the function should return the node with value 2, because the cycle begins at this node.

## Approach
The algorithm uses Floyd's Tortoise and Hare algorithm to detect the cycle, then finds the start of the cycle by moving one pointer to the head of the list and keeping the other pointer at the meeting point. The two pointers then move one step at a time, meeting at the start of the cycle.

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
        if (head == NULL || head->next == NULL) {
            return NULL;
        }

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
        tortoise = head;  // Move one pointer to the head of the list
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
Input: 3 -> 2 -> 0 -> -4 -> 2
Output: Node with value 2
Input: 1 -> 2
Output: NULL
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- The start of the cycle can be found by moving one pointer to the head of the list and keeping the other pointer at the meeting point, then moving both pointers one step at a time.
- This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large linked lists.