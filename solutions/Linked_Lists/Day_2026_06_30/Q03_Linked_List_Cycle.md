# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. To solve this problem, we can use a variety of methods, but we must ensure that our solution is efficient in terms of both time and space complexity. For example, given a linked list with the following nodes: 1 -> 2 -> 3 -> 4 -> 2 (cycle), our function should return true. However, given a linked list with the following nodes: 1 -> 2 -> 3 -> 4, our function should return false.

## Approach
We will use the Floyd's Tortoise and Hare algorithm to solve this problem. The algorithm uses two pointers, one moving twice as fast as the other, to traverse the linked list. If there is a cycle, the two pointers will eventually meet.

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
        
        // traverse the linked list
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
Input: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
Output: true
Input: 1 -> 2 -> 3 -> 4
Output: false
```

## Key Takeaways
- The Floyd's Tortoise and Hare algorithm can be used to detect a cycle in a linked list.
- The algorithm uses two pointers, one moving twice as fast as the other, to traverse the linked list.
- If there is a cycle, the two pointers will eventually meet, indicating the presence of a cycle.