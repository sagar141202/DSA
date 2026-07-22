# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is found and false otherwise. The linked list may have multiple nodes and may be empty. For example, given the head of a linked list with nodes 1 -> 2 -> 3 -> 4 -> 2 (cycle at node 2), the function should return true.

## Approach
The algorithm uses Floyd's Tortoise and Hare (Cycle Detection) approach. Two pointers are used, one moving twice as fast as the other. If there is a cycle, these two pointers will eventually meet.

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
        
        // initialize two pointers
        ListNode *slow = head;
        ListNode *fast = head->next;
        
        // loop until the fast pointer reaches the end or the two pointers meet
        while (slow != fast) {
            // if the fast pointer reaches the end, there is no cycle
            if (fast == NULL || fast->next == NULL) {
                return false;
            }
            
            // move the slow pointer one step at a time
            slow = slow->next;
            // move the fast pointer two steps at a time
            fast = fast->next->next;
        }
        
        // if the loop ends, the two pointers have met, so there is a cycle
        return true;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 2 (cycle at node 2)
Output: true

Input: 1 -> 2 -> 3 -> 4 -> 5 (no cycle)
Output: false

Input: (empty list)
Output: false
```

## Key Takeaways
- Use Floyd's Tortoise and Hare approach to detect cycles in linked lists.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large linked lists.
- The algorithm can be used to detect cycles in other data structures, such as graphs.