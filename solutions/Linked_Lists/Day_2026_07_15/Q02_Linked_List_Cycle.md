# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is present and false otherwise. The linked list may have multiple nodes with the same value, but each node's next pointer should be unique. For example, given the head of a linked list with nodes 1 -> 2 -> 3 -> 4 -> 2 (cycle), the function should return true. However, given the head of a linked list with nodes 1 -> 2 -> 3 -> 4, the function should return false.

## Approach
The approach to solve this problem is to use the Floyd's Tortoise and Hare algorithm. This algorithm uses two pointers that move at different speeds through the list. If a cycle is present, these two pointers will eventually meet.

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
        // if the list is empty, it does not have a cycle
        if (head == NULL || head->next == NULL) {
            return false;
        }
        
        // initialize two pointers, one moving twice as fast as the other
        ListNode *slow = head;
        ListNode *fast = head->next;
        
        // loop until the fast pointer reaches the end of the list or the two pointers meet
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
        
        // if the loop ends, it means the two pointers have met, so there is a cycle
        return true;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
Output: true
Input: 1 -> 2 -> 3 -> 4
Output: false
```

## Key Takeaways
- The Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- This algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large linked lists.
- The algorithm uses two pointers moving at different speeds to detect the cycle.