# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list has at least one node, and all the values of the node are unique. 

## Approach
We can use Floyd's Tortoise and Hare algorithm to detect the cycle, then move one pointer back to the head and keep the other pointer at the meeting point, and move both pointers one step at a time to find the start of the cycle.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (!head || !head->next) return nullptr;

        ListNode *slow = head;
        ListNode *fast = head;

        // detect cycle using Floyd's Tortoise and Hare algorithm
        do {
            slow = slow->next;
            if (!fast->next || !fast->next->next) return nullptr;
            fast = fast->next->next;
        } while (slow != fast);

        // reset slow to head, keep fast at meeting point
        slow = head;

        // move both pointers one step at a time to find the start of the cycle
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
Output: node with value 2
Input: head = [1,2], pos = 0
Output: node with value 1
Input: head = [1], pos = -1
Output: nullptr
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- Once a cycle is detected, we can reset one pointer to the head and keep the other pointer at the meeting point, and move both pointers one step at a time to find the start of the cycle.
- This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large linked lists.