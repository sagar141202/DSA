# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is present and false otherwise. The linked list may have multiple nodes with the same value, but the next pointers should be considered to determine the presence of a cycle. For example, given the head of a linked list with the values [3, 2, 0, -4] and the next pointers as follows: 3 -> 2 -> 0 -> -4 -> 2, the function should return true because there is a cycle in the list.

## Approach
We will use the Floyd's Tortoise and Hare algorithm to detect the cycle. This algorithm uses two pointers, one moving twice as fast as the other, to traverse the linked list. If a cycle is present, the fast pointer will eventually meet the slow pointer. If no cycle is present, the fast pointer will reach the end of the linked list.

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
        // if the list is empty or only has one node, there is no cycle
        if (head == NULL || head->next == NULL) {
            return false;
        }

        // initialize two pointers, one moving twice as fast as the other
        ListNode *slow = head;
        ListNode *fast = head->next;

        // traverse the linked list
        while (slow != fast) {
            // if the fast pointer reaches the end of the list, there is no cycle
            if (fast == NULL || fast->next == NULL) {
                return false;
            }

            // move the slow pointer one step
            slow = slow->next;

            // move the fast pointer two steps
            fast = fast->next->next;
        }

        // if the fast pointer meets the slow pointer, there is a cycle
        return true;
    }
};
```

## Test Cases
```
Input: [3, 2, 0, -4] with next pointers: 3 -> 2 -> 0 -> -4 -> 2
Output: true

Input: [1, 2] with next pointers: 1 -> 2 -> 1
Output: true

Input: [1] with next pointers: 1 -> NULL
Output: false
```

## Key Takeaways
- The Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- The algorithm uses two pointers, one moving twice as fast as the other, to traverse the linked list.
- If a cycle is present, the fast pointer will eventually meet the slow pointer.