# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is found and false otherwise. The linked list is represented as a sequence of nodes where each node has a value and a next pointer. For example, the linked list 1 -> 2 -> 3 -> 4 -> 2 has a cycle because the node with value 4 points back to the node with value 2.

## Approach
The algorithm uses Floyd's cycle-finding algorithm, also known as the "tortoise and the hare" algorithm. It uses two pointers, one moving twice as fast as the other. If a cycle exists, these two pointers will eventually meet at some node within the cycle.

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
        
        // initialize two pointers, one moving twice as fast as the other
        ListNode *slow = head;
        ListNode *fast = head->next;
        
        // move the pointers through the list
        while (slow != fast) {
            // if the fast pointer reaches the end, there's no cycle
            if (fast == NULL || fast->next == NULL) {
                return false;
            }
            
            // move the slow pointer one step
            slow = slow->next;
            // move the fast pointer two steps
            fast = fast->next->next;
        }
        
        // if the pointers meet, there's a cycle
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
- Floyd's cycle-finding algorithm can be used to detect cycles in linked lists.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large linked lists.
- The algorithm uses two pointers, one moving twice as fast as the other, to detect the cycle.