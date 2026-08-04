# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is found and false otherwise. The linked list may have multiple nodes with the same value, so we cannot rely on the node's value to identify a cycle. We can only use the node's next pointer to determine if a cycle exists.

## Approach
We can solve this problem by using Floyd's Tortoise and Hare algorithm, also known as the slow and fast pointer approach. This algorithm uses two pointers that move at different speeds through the linked list. If a cycle exists, the fast pointer will eventually catch up to the slow pointer.

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

        // initialize the slow and fast pointers
        ListNode *slow = head;
        ListNode *fast = head->next;

        // move the slow and fast pointers through the list
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

        // if the slow and fast pointers meet, there is a cycle
        return true;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
Output: true

Input: 1 -> 2 -> 3 -> 4 -> 5 (no cycle)
Output: false
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- The algorithm uses two pointers that move at different speeds through the list.
- If a cycle exists, the fast pointer will eventually catch up to the slow pointer.