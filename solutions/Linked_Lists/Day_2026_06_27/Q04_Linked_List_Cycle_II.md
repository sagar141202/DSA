# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list has at least one node, and all the values are unique. The cycle can start from any node, and the cycle may be of any length. For example, given a linked list with nodes 3 -> 2 -> 0 -> -4 and a cycle starting at node 1 (i.e., the node with value -4 is connected to node 0), the function should return the node with value -4.

## Approach
The approach to solve this problem is to use the Floyd's Tortoise and Hare algorithm to detect the cycle, then find the start of the cycle by moving one pointer to the head and keeping the other pointer at the meeting point, and finally moving both pointers one step at a time until they meet again.

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
        if (head == nullptr || head->next == nullptr) {
            return nullptr;
        }

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

        // If there is no cycle, return nullptr
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
Input: head = [3,2,0,-4], pos = 1
Output: node with value -4
Input: head = [1,2], pos = 0
Output: node with value 1
Input: head = [1], pos = -1
Output: nullptr
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect a cycle in a linked list.
- Once a cycle is detected, we can find the start of the cycle by moving one pointer to the head and keeping the other pointer at the meeting point.
- The time complexity of this solution is O(n), where n is the number of nodes in the linked list.