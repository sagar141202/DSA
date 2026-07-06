# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is found and false otherwise. The linked list may have 0 to 10^5 nodes, and each node may have a value from 0 to 10^5.

## Approach
We can use Floyd's cycle-finding algorithm, also known as the "tortoise and the hare" algorithm. This algorithm uses two pointers that move at different speeds through the list, and if a cycle exists, these two pointers will eventually meet.

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
        // if the list is empty, there's no cycle
        if (head == NULL || head->next == NULL) {
            return false;
        }
        
        // initialize two pointers
        ListNode *slow = head;
        ListNode *fast = head->next;
        
        // move the pointers through the list
        while (slow != fast) {
            // if the fast pointer reaches the end, there's no cycle
            if (fast == NULL || fast->next == NULL) {
                return false;
            }
            // move the slow pointer one step at a time
            slow = slow->next;
            // move the fast pointer two steps at a time
            fast = fast->next->next;
        }
        
        // if the pointers meet, there's a cycle
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

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

## Key Takeaways
- Floyd's cycle-finding algorithm can be used to detect cycles in linked lists.
- The algorithm uses two pointers that move at different speeds through the list.
- If a cycle exists, the two pointers will eventually meet, indicating the presence of a cycle.