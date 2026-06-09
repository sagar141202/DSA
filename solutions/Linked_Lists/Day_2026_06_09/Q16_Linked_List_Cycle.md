# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is present and false otherwise. The linked list may have 0 to 10^5 nodes, and each node may have a value from 0 to 10^5. For example, if the input is [1,2,3,4,5] with a cycle between the last node and the second node, the function should return true.

## Approach
The algorithm uses Floyd's Tortoise and Hare approach, where two pointers move at different speeds through the linked list. If a cycle is present, the two pointers will eventually meet. The intuition is that the faster pointer will eventually catch up to the slower pointer if a cycle exists.

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
        
        // move the pointers through the list
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
        
        // if the pointers meet, there is a cycle
        return true;
    }
};
```

## Test Cases
```
Input: [1,2,3,4,5] with a cycle between the last node and the second node
Output: true
Input: [1,2,3,4,5] with no cycle
Output: false
```

## Key Takeaways
- Floyd's Tortoise and Hare approach can be used to detect cycles in linked lists.
- The approach has a time complexity of O(n) and a space complexity of O(1), making it efficient for large linked lists.
- The algorithm can be applied to other problems that involve detecting cycles, such as in graphs.