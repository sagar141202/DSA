# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is found and false otherwise. The linked list may have 0 or more nodes, and each node may have a value from 0 to 9. For example, given the head of a linked list with the values [1, 2, 3, 4] and a cycle at node 2, the function should return true.

## Approach
We will use Floyd's Cycle Detection algorithm, also known as the "tortoise and hare" algorithm. This algorithm uses two pointers that move at different speeds through the list. If there is a cycle, the faster pointer will eventually catch up to the slower pointer.

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
        
        // Loop until the fast pointer reaches the end of the list
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
        
        // If the loop ends, it means the fast pointer caught up to the slow pointer, so there is a cycle
        return true;
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 4] with a cycle at node 2
Output: true
Input: [1, 2, 3, 4] with no cycle
Output: false
```

## Key Takeaways
- Floyd's Cycle Detection algorithm can be used to detect cycles in linked lists.
- The algorithm uses two pointers moving at different speeds to detect cycles.
- The time complexity of the algorithm is O(n), where n is the number of nodes in the linked list.