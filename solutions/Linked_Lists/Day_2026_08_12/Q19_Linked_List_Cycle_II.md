# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null. The linked list has at least one node, and all the values in the list are unique. The cycle can start from any node, not just the head. For example, given the list 3 -> 2 -> 0 -> -4 -> 2, the cycle starts at the node with value 2.

## Approach
We can use the Floyd's Tortoise and Hare algorithm to detect the cycle and then find the start of the cycle. The algorithm uses two pointers, one moving twice as fast as the other, to detect the cycle. Once the cycle is detected, we reset one of the pointers to the head and move both pointers one step at a time to find the start of the cycle.

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
            tortoise = tortoise->next;
            hare = hare->next->next;
            if (tortoise == hare) {
                break;
            }
        }
        
        // If no cycle is found, return NULL
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
Input: 3 -> 2 -> 0 -> -4 -> 2
Output: Node with value 2
Input: 1 -> 2
Output: NULL
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- Once a cycle is detected, we can find the start of the cycle by resetting one of the pointers to the head and moving both pointers one step at a time.
- The time complexity of this solution is O(n), where n is the number of nodes in the linked list, and the space complexity is O(1) as we only use a constant amount of space.