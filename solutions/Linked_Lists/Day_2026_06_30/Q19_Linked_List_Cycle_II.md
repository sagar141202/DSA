# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list has at least one node, and all the values of the node are unique. The cycle is a connected sequence of nodes where every node references the next node, and the last node references the first node in the sequence.

## Approach
We can use Floyd's Tortoise and Hare algorithm to detect the cycle, then find the start of the cycle by moving one pointer back to the head and keeping the other pointer at the meeting point, and moving both pointers one step at a time.

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
    ListNode *detectCycle(ListNode *head) {
        if (head == NULL || head->next == NULL) return NULL;
        
        // detect cycle using Floyd's Tortoise and Hare algorithm
        ListNode *slow = head;
        ListNode *fast = head;
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) break;
        }
        
        // if no cycle
        if (fast == NULL || fast->next == NULL) return NULL;
        
        // find start of cycle
        slow = head;
        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }
        
        return slow;
    }
};
```

## Test Cases
```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Input: head = [1], pos = -1
Output: no cycle
```

## Key Takeaways
- Use Floyd's Tortoise and Hare algorithm to detect the cycle in the linked list.
- After detecting the cycle, move one pointer back to the head and keep the other pointer at the meeting point, and move both pointers one step at a time to find the start of the cycle.
- If there is no cycle, return nullptr.