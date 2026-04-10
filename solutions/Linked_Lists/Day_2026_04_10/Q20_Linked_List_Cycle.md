# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is present and false otherwise. The linked list may have 0 or more nodes, and each node may have a value between 0 and 100. The linked list is represented as a singly linked list where each node is an instance of a ListNode class.

## Approach
We will use Floyd's Tortoise and Hare algorithm to solve this problem, which uses two pointers that move at different speeds to detect a cycle. If a cycle is present, the fast pointer will eventually meet the slow pointer.

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
    bool hasCycle(ListNode *head) {
        // if the list is empty, there is no cycle
        if (head == NULL || head->next == NULL) {
            return false;
        }

        // initialize two pointers
        ListNode *slow = head;
        ListNode *fast = head->next;

        // loop through the list
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

        // if the loop ends, it means the fast pointer met the slow pointer, so there is a cycle
        return true;
    }
};
```

## Test Cases
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the node 0 points to the node 2.

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the node 2 points to the node 1.

Input: head = [1]
Output: false
Explanation: There is no cycle in the linked list.
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect a cycle in a linked list.
- The algorithm uses two pointers that move at different speeds to detect a cycle.
- If a cycle is present, the fast pointer will eventually meet the slow pointer.