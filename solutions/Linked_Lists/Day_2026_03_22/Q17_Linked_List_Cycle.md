# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is found and false otherwise. The linked list may have a cycle at any point, and the cycle may have any number of nodes. For example, given a linked list with the following nodes: 1 -> 2 -> 3 -> 4 -> 2, the function should return true because there is a cycle at node 2.

## Approach
The algorithm uses the Floyd's Tortoise and Hare (Cycle Detection) approach, where two pointers move at different speeds through the list. If a cycle exists, the two pointers will eventually meet at some node.

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
        // If the linked list is empty, there is no cycle
        if (head == NULL || head->next == NULL) {
            return false;
        }
        
        // Initialize two pointers
        ListNode *slow = head;
        ListNode *fast = head->next;
        
        // Move the pointers through the list
        while (slow != fast) {
            // If the fast pointer reaches the end, there is no cycle
            if (fast == NULL || fast->next == NULL) {
                return false;
            }
            // Move the slow pointer one step
            slow = slow->next;
            // Move the fast pointer two steps
            fast = fast->next->next;
        }
        
        // If the pointers meet, there is a cycle
        return true;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 2
Output: true
Input: 1 -> 2 -> 3 -> 4
Output: false
```

## Key Takeaways
- Use the Floyd's Tortoise and Hare approach to detect cycles in linked lists.
- Initialize two pointers, one moving one step at a time and the other moving two steps at a time.
- If the two pointers meet at any point, a cycle exists in the linked list.