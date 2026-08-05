# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list has at least one node, and all the values are unique. The cycle begins at the node with the value that is equal to the value of the node where the fast pointer and slow pointer meet.

## Approach
We can solve this problem by using the Floyd's Tortoise and Hare algorithm to detect the cycle, then move one of the pointers back to the head and keep the other pointer at the meeting point, and move both pointers one step at a time to find the cycle beginning node.

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
        
        // Detect cycle using Floyd's Tortoise and Hare algorithm
        ListNode *tortoise = head;
        ListNode *hare = head;
        while (hare != nullptr && hare->next != nullptr) {
            tortoise = tortoise->next;
            hare = hare->next->next;
            if (tortoise == hare) {
                break;
            }
        }
        
        // If no cycle is found
        if (hare == nullptr || hare->next == nullptr) {
            return nullptr;
        }
        
        // Move tortoise back to head and keep hare at meeting point
        tortoise = head;
        
        // Move both pointers one step at a time to find cycle beginning node
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
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- The meeting point of the two pointers can be used to find the cycle beginning node.
- The time complexity of this solution is O(n), where n is the number of nodes in the linked list.