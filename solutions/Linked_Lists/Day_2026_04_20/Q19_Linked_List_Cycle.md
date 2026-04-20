# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is present and false otherwise. The linked list may have any number of nodes, and each node may have a value from 0 to 9. For example, given a linked list with nodes 3 -> 2 -> 0 -> -4 and the node with value 0 points back to the node with value 2, the function should return true.

## Approach
The algorithm used to solve this problem is Floyd's Tortoise and Hare algorithm, which uses two pointers that move at different speeds through the linked list. If a cycle is present, the fast pointer will eventually catch up to the slow pointer. If no cycle is present, the fast pointer will reach the end of the linked list.

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
        // if the linked list is empty, there is no cycle
        if (head == NULL || head->next == NULL) {
            return false;
        }

        // initialize the slow and fast pointers
        ListNode *slow = head;
        ListNode *fast = head->next;

        // move the slow and fast pointers through the linked list
        while (slow != fast) {
            // if the fast pointer reaches the end of the linked list, there is no cycle
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
Input: 3 -> 2 -> 0 -> -4 (with 0 pointing back to 2)
Output: true
Input: 1 -> 2 (with no cycle)
Output: false
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- The algorithm uses two pointers that move at different speeds through the linked list.
- If a cycle is present, the fast pointer will eventually catch up to the slow pointer.