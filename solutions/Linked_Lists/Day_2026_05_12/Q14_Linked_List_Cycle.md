# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is present and false otherwise. The linked list may have 0 to 10^5 nodes, and the value of each node is an integer between -10^5 to 10^5.

## Approach
The algorithm uses Floyd's Tortoise and Hare (Cycle Detection) approach. It uses two pointers, one moving twice as fast as the other. If there is a cycle, these two pointers will eventually meet.

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
        
        while (slow != fast) {
            if (fast == NULL || fast->next == NULL) {
                return false;
            }
            // Move slow pointer one step at a time
            slow = slow->next;
            // Move fast pointer two steps at a time
            fast = fast->next->next;
        }
        
        // If the two pointers meet, there is a cycle
        return true;
    }
};
```

## Test Cases
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the second node.
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the first node.
Input: head = [1]
Output: false
Explanation: There is no cycle in the linked list.
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- This approach has a time complexity of O(n) and a space complexity of O(1), making it efficient for large linked lists.
- The algorithm uses two pointers, one moving twice as fast as the other, to detect cycles in the linked list.