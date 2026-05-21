# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null. The linked list has at least one node, and all the values of the node are unique. The cycle is defined as a node that has a next pointer to a node that is already in the list.

## Approach
We will use Floyd's Tortoise and Hare algorithm to detect the cycle and then find the start of the cycle. The algorithm uses two pointers, one moving twice as fast as the other, to detect the cycle. Once the cycle is detected, we reset one pointer to the head and move both pointers one step at a time to find the start of the cycle.

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
        // phase 1: detect the cycle using Floyd's Tortoise and Hare algorithm
        ListNode *tortoise = head;
        ListNode *hare = head;
        do {
            if (hare == NULL || hare->next == NULL) {
                return NULL; // no cycle
            }
            tortoise = tortoise->next;
            hare = hare->next->next;
        } while (tortoise != hare);

        // phase 2: find the start of the cycle
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
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- The algorithm has two phases: detecting the cycle and finding the start of the cycle.
- The time complexity is O(n), where n is the number of nodes in the linked list, and the space complexity is O(1) as only a constant amount of space is used.