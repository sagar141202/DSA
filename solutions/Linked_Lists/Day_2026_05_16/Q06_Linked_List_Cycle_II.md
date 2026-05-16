# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list is defined by the Node class, where each node has a value and a pointer to the next node. The cycle is defined as a node that has already been visited before. For example, given the linked list 3 -> 2 -> 0 -> -4 -> 2, the function should return the node with value 2, because the cycle begins at this node.

## Approach
The algorithm uses the Floyd's Tortoise and Hare (Cycle Detection) approach to detect the cycle, and then finds the start of the cycle by moving the slow pointer to the head and keeping the fast pointer at the meeting point. The slow and fast pointers will meet at the start of the cycle.

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
        if (head == NULL || head->next == NULL) {
            return NULL;
        }
        
        ListNode *slow = head;
        ListNode *fast = head;
        
        // Detect cycle using Floyd's Tortoise and Hare algorithm
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            
            if (slow == fast) {
                break;
            }
        }
        
        if (fast == NULL || fast->next == NULL) {
            return NULL;
        }
        
        // Find the start of the cycle
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
Input: 3 -> 2 -> 0 -> -4 -> 2
Output: Node with value 2
Input: 1 -> 2
Output: nullptr
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- Once a cycle is detected, the start of the cycle can be found by moving the slow pointer to the head and keeping the fast pointer at the meeting point.
- The time complexity of this solution is O(n), where n is the number of nodes in the linked list.