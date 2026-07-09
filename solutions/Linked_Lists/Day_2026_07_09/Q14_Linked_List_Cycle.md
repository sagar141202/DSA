# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if there is a cycle and false otherwise. The linked list may have 0 to n nodes, and each node may have a value from 0 to 100. 

## Approach
We can solve this problem using Floyd's Tortoise and Hare algorithm, which uses two pointers that move at different speeds to detect a cycle in the linked list. If the two pointers meet, there is a cycle.

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
    bool hasCycle(ListNode *head) {
        // if the list is empty, there is no cycle
        if (head == NULL || head->next == NULL) {
            return false;
        }

        // initialize two pointers, one moves twice as fast as the other
        ListNode *slow = head;
        ListNode *fast = head->next;

        // if the two pointers meet, there is a cycle
        while (slow != fast) {
            // if the fast pointer reaches the end of the list, there is no cycle
            if (fast == NULL || fast->next == NULL) {
                return false;
            }

            // move the slow pointer one step at a time
            slow = slow->next;
            // move the fast pointer two steps at a time
            fast = fast->next->next;
        }

        // if the two pointers meet, there is a cycle
        return true;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
Output: true

Input: 1 -> 2 -> 3 -> 4 (no cycle)
Output: false
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect a cycle in a linked list.
- The algorithm uses two pointers that move at different speeds to detect a cycle.
- If the two pointers meet, there is a cycle in the linked list.