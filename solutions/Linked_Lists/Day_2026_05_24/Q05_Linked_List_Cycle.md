# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is present and false otherwise. The linked list may have multiple nodes with the same value, so we cannot rely solely on node values to detect a cycle. For example, given the head of a linked list with the values [3, 2, 0, -4] and a cycle at node with value -4, the function should return true.

## Approach
We can solve this problem by using Floyd's cycle-finding algorithm, also known as the "tortoise and the hare" algorithm. This algorithm uses two pointers, one moving twice as fast as the other, to detect a cycle in the linked list. If there is a cycle, these two pointers will eventually meet.

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
        
        // loop until the fast pointer reaches the end of the list or the two pointers meet
        while (slow != fast) {
            // if the fast pointer reaches the end of the list, there is no cycle
            if (fast == NULL || fast->next == NULL) {
                return false;
            }
            
            // move the slow pointer one step at a time
            slow = slow->next;
            // move the fast pointer two steps at a time
            fast = fast->next->next;
        }
        
        // if the two pointers meet, there is a cycle in the list
        return true;
    }
};
```

## Test Cases
```
Input: [3, 2, 0, -4] with a cycle at node with value -4
Output: true
Input: [1, 2] with no cycle
Output: false
```

## Key Takeaways
- Floyd's cycle-finding algorithm can be used to detect a cycle in a linked list.
- The algorithm uses two pointers, one moving twice as fast as the other, to detect a cycle.
- If there is a cycle, the two pointers will eventually meet, indicating the presence of a cycle.