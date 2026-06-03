# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is present and false otherwise. The linked list may have multiple nodes with the same value, and the cycle may start and end at any node.

## Approach
We will use Floyd's Tortoise and Hare algorithm to detect the cycle. This algorithm uses two pointers that move at different speeds through the list. If there is a cycle, these two pointers will eventually meet.

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
        if (head == NULL) {
            return false;
        }
        
        // initialize two pointers, one moving twice as fast as the other
        ListNode *slow = head;
        ListNode *fast = head->next;
        
        // if the fast pointer reaches the end, there is no cycle
        while (slow != fast) {
            // if the fast pointer reaches the end, there is no cycle
            if (fast == NULL || fast->next == NULL) {
                return false;
            }
            
            // move the slow pointer one step
            slow = slow->next;
            
            // move the fast pointer two steps
            fast = fast->next->next;
        }
        
        // if the two pointers meet, there is a cycle
        return true;
    }
};
```

## Test Cases
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the second node.
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- The algorithm uses two pointers moving at different speeds to detect the cycle.
- If the two pointers meet, there is a cycle in the linked list.