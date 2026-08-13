# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is found and false otherwise. The linked list may have any number of nodes, and each node may have a value between 1 and 100. The list may or may not have a cycle.

## Approach
The algorithm uses Floyd's Tortoise and Hare approach, where two pointers move at different speeds through the list. If a cycle exists, these two pointers will eventually meet. If no cycle exists, the faster pointer will reach the end of the list.

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
        if (head == NULL || head->next == NULL) {
            return false;
        }
        
        // Initialize two pointers, one moving twice as fast as the other
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
Input: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
Output: true

Input: 1 -> 2 -> 3 -> 4 -> NULL (no cycle)
Output: false
```

## Key Takeaways
- Floyd's Tortoise and Hare approach can be used to detect cycles in linked lists.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large lists.
- The approach can be applied to other problems involving cycles, such as detecting cycles in graphs.