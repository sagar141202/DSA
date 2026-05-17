# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is present and false otherwise. The linked list is defined as follows: 0 -> 1 -> 2 -> 3 -> 4 -> 2 (cycle at node 2), or 0 -> 1 -> 2 -> 3 -> 4 (no cycle).

## Approach
The algorithm uses the Floyd's Tortoise and Hare (Cycle Detection) approach, where two pointers move at different speeds through the list. If a cycle exists, the faster pointer will eventually catch up to the slower pointer. If no cycle exists, the faster pointer will reach the end of the list.

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
        // handle edge case where list is empty
        if (head == NULL || head->next == NULL) {
            return false;
        }
        
        // initialize two pointers, one moving twice as fast as the other
        ListNode *slow = head;
        ListNode *fast = head->next;
        
        // move pointers through the list
        while (slow != fast) {
            // if fast pointer reaches the end, no cycle exists
            if (fast == NULL || fast->next == NULL) {
                return false;
            }
            
            // move slow pointer one step
            slow = slow->next;
            // move fast pointer two steps
            fast = fast->next->next;
        }
        
        // if we reach this point, a cycle exists
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
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- The algorithm has a time complexity of O(n), where n is the number of nodes in the list.
- The algorithm has a space complexity of O(1), as it only uses a constant amount of space to store the two pointers.