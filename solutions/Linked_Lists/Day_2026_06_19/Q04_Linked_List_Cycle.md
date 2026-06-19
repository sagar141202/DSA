# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is found and false otherwise. The linked list may have multiple nodes with the same value, so it is not sufficient to check for repeated values. For example, given the head of a linked list with the values 3 -> 2 -> 0 -> -4 and a cycle at the node with value 0, the function should return true.

## Approach
The algorithm uses Floyd's Tortoise and Hare (Cycle Detection) approach, which involves two pointers moving at different speeds through the list. If there is a cycle, these two pointers will eventually meet at some point within the cycle. The intuition is that if there is no cycle, the faster pointer will reach the end of the list, while if there is a cycle, the faster pointer will lap the slower pointer.

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
        
        // initialize two pointers, one moving twice as fast as the other
        ListNode *slow = head;
        ListNode *fast = head->next;
        
        // loop until the fast pointer reaches the end of the list or meets the slow pointer
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
        
        // if the loop ends, the slow and fast pointers have met, so there is a cycle
        return true;
    }
};
```

## Test Cases
```
Input: head = [3,2,0,-4], pos = 1 (0-indexed)
Output: true
Explanation: There is a cycle in the linked list, where the node 0's next pointer points to the node 2.
```

## Key Takeaways
- Use Floyd's Tortoise and Hare approach to detect cycles in linked lists.
- If the fast pointer reaches the end of the list, there is no cycle.
- If the slow and fast pointers meet, there is a cycle in the linked list.