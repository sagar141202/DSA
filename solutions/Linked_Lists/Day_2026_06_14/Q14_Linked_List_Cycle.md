# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is present and false otherwise. The linked list may have multiple nodes and the cycle may be at any point in the list. For example, given the head of a linked list with the nodes 1 -> 2 -> 3 -> 4 -> 2, the function should return true because there is a cycle in the list.

## Approach
The approach to solve this problem is to use the Floyd's Tortoise and Hare algorithm, also known as the slow and fast pointer technique. This algorithm uses two pointers that move at different speeds through the linked list. If there is a cycle, the fast pointer will eventually catch up to the slow pointer. If there is no cycle, the fast pointer will reach the end of the linked list.

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
Input: 1 -> 2 -> 3 -> 4 -> 2
Output: true

Input: 1 -> 2 -> 3 -> 4
Output: false
```

## Key Takeaways
- The Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- The algorithm uses two pointers that move at different speeds through the linked list.
- If the fast pointer catches up to the slow pointer, there is a cycle in the list. If the fast pointer reaches the end of the list, there is no cycle.