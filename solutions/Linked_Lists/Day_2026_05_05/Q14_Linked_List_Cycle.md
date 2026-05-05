# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is present and false otherwise. The linked list may have 0 to n nodes and n will be in the range [0, 10000]. The value of each node will be in the range [-1000000, 1000000]. Example: if the linked list is 1 -> 2 -> 3 -> 4 -> 2, then the function should return true because there is a cycle.

## Approach
The algorithm uses Floyd's Tortoise and Hare approach, which involves two pointers moving at different speeds through the list. If there is a cycle, these two pointers will eventually meet. The intuition is that the faster pointer will catch up to the slower pointer within the cycle.

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
        // if list is empty
        if (head == NULL) {
            return false;
        }
        
        // initialize two pointers
        ListNode *slow = head;
        ListNode *fast = head->next;
        
        // traverse the list
        while (slow != fast) {
            // if fast reaches the end, there is no cycle
            if (fast == NULL || fast->next == NULL) {
                return false;
            }
            
            // move slow one step
            slow = slow->next;
            // move fast two steps
            fast = fast->next->next;
        }
        
        // if slow and fast meet, there is a cycle
        return true;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 2
Output: true
Input: 1 -> 2 -> 3 -> 4
Output: false
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- This algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large lists.
- The algorithm relies on the fact that if there is a cycle, the faster pointer will eventually catch up to the slower pointer within the cycle.