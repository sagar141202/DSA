# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is found and false otherwise. The linked list may have multiple nodes and may or may not have a cycle. For example, given the head of a linked list with the nodes 1 -> 2 -> 3 -> 4 -> 2 (cycle at node 2), the function should return true. However, given the head of a linked list with the nodes 1 -> 2 -> 3 -> 4 (no cycle), the function should return false.

## Approach
The algorithm uses Floyd's Tortoise and Hare (Cycle Detection) approach, which involves two pointers moving at different speeds through the linked list. If a cycle exists, these two pointers will eventually meet at some node within the cycle. The intuition is that the faster pointer will eventually catch up to the slower pointer if a cycle is present.

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
        // If the list is empty, it does not have a cycle
        if (head == NULL) {
            return false;
        }

        // Initialize two pointers, one moving twice as fast as the other
        ListNode *slow = head;
        ListNode *fast = head->next;

        // Loop until the fast pointer reaches the end of the list
        while (slow != fast) {
            // If the fast pointer reaches the end, there is no cycle
            if (fast == NULL || fast->next == NULL) {
                return false;
            }

            // Move the slow pointer one step at a time
            slow = slow->next;
            // Move the fast pointer two steps at a time
            fast = fast->next->next;
        }

        // If the loop ends, it means the fast pointer caught up to the slow pointer, so there is a cycle
        return true;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 2 (cycle at node 2)
Output: true
Input: 1 -> 2 -> 3 -> 4 (no cycle)
Output: false
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large lists.
- The algorithm works by moving two pointers at different speeds through the list and checking if they ever meet, indicating a cycle.