# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is present and false otherwise. The linked list is defined as a sequence of nodes, where each node has an integer value and a next pointer pointing to the next node in the sequence. The cycle can be present at any point in the linked list.

## Approach
The algorithm uses the two-pointer technique, also known as the Floyd's cycle-finding algorithm. It uses two pointers, one moving twice as fast as the other, to traverse the linked list. If there is a cycle, these two pointers will eventually meet at some node.

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
        // If the list is empty, there is no cycle
        if (head == NULL) {
            return false;
        }

        // Initialize two pointers, one moving twice as fast as the other
        ListNode *slow = head;
        ListNode *fast = head->next;

        // Traverse the linked list
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

        // If the two pointers meet, there is a cycle
        return true;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 2 (cycle at node 2)
Output: true

Input: 1 -> 2 -> 3 -> 4 -> NULL (no cycle)
Output: false
```

## Key Takeaways
- The Floyd's cycle-finding algorithm is an efficient way to detect cycles in linked lists.
- The algorithm uses two pointers, one moving twice as fast as the other, to traverse the linked list.
- If the two pointers meet at some node, it indicates the presence of a cycle in the linked list.