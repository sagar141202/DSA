# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if there is a cycle and false otherwise. The linked list can have any number of nodes and the cycle can be of any length, including a single node pointing to itself. The input will be a pointer to the head of the linked list, and the output will be a boolean indicating whether a cycle exists.

## Approach
The algorithm uses Floyd's Tortoise and Hare approach, also known as the slow and fast pointer technique. This involves moving two pointers through the list at different speeds. If there is a cycle, the fast pointer will eventually catch up to the slow pointer.

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
        // if list is empty, there is no cycle
        if (head == NULL || head->next == NULL) {
            return false;
        }
        
        // initialize slow and fast pointers
        ListNode *slow = head;
        ListNode *fast = head->next;
        
        // move slow and fast pointers through the list
        while (slow != fast) {
            // if fast pointer reaches the end, there is no cycle
            if (fast == NULL || fast->next == NULL) {
                return false;
            }
            // move slow pointer one step at a time
            slow = slow->next;
            // move fast pointer two steps at a time
            fast = fast->next->next;
        }
        
        // if slow and fast pointers meet, there is a cycle
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
- Floyd's Tortoise and Hare approach can be used to detect cycles in linked lists.
- The slow and fast pointer technique has a time complexity of O(n) and a space complexity of O(1).
- This approach can be modified to find the start of the cycle in the linked list.