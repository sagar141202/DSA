# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list has at least one node, and all the values in the linked list are unique. The cycle is defined as a node that is visited more than once during a traversal of the linked list.

## Approach
The approach to solve this problem involves using the Floyd's Tortoise and Hare algorithm to detect the cycle, and then finding the start of the cycle. We use two pointers, slow and fast, to traverse the linked list. If a cycle exists, the fast pointer will eventually catch up to the slow pointer.

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
            tortoise = tortoise->next;  // move one step at a time
            hare = hare->next->next;    // move two steps at a time
            if (tortoise == hare) {
                break;
            }
        }
        
        // If no cycle is found, return nullptr
        if (hare == NULL || hare->next == NULL) {
            return NULL;
        }
        
        // Phase 2: Finding the start of the cycle
        tortoise = head;  // reset the tortoise to the head
        while (tortoise != hare) {
            tortoise = tortoise->next;  // move one step at a time
            hare = hare->next;           // move one step at a time
        }
        
        return tortoise;  // return the node where the cycle begins
    }
};
```

## Test Cases
```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
```

## Key Takeaways
- Use Floyd's Tortoise and Hare algorithm to detect the cycle in the linked list.
- Once the cycle is detected, find the start of the cycle by moving the tortoise and hare one step at a time from the head and the meeting point respectively.
- The time complexity of this solution is O(n), where n is the number of nodes in the linked list.