# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is found and false otherwise. The linked list may have 0 or more nodes, and each node may have a value between 0 and 100. The function should not modify the linked list.

## Approach
The algorithm uses Floyd's Tortoise and Hare approach, also known as the slow and fast pointer technique. Two pointers are used, one moving twice as fast as the other. If a cycle exists, these two pointers will eventually meet.

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
        // If the list is empty, there's no cycle
        if (head == NULL || head->next == NULL) {
            return false;
        }
        
        // Initialize slow and fast pointers
        ListNode *slow = head;
        ListNode *fast = head->next;
        
        // Loop until the fast pointer reaches the end of the list
        while (slow != fast) {
            // If the fast pointer reaches the end, there's no cycle
            if (fast == NULL || fast->next == NULL) {
                return false;
            }
            
            // Move the slow pointer one step
            slow = slow->next;
            // Move the fast pointer two steps
            fast = fast->next->next;
        }
        
        // If the loop ends, a cycle is found
        return true;
    }
};
```

## Test Cases
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Input: head = [1,2], pos = 0
Output: true
Input: head = [1], pos = -1
Output: false
```

## Key Takeaways
- The Floyd's Tortoise and Hare algorithm is an efficient way to detect cycles in linked lists.
- The time complexity of this algorithm is O(n), where n is the number of nodes in the linked list.
- The space complexity is O(1), as only a constant amount of space is used to store the slow and fast pointers.