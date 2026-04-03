# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle exists and false otherwise. The linked list may have 0 to n nodes, where n is a positive integer.

## Approach
We will use Floyd's Tortoise and Hare algorithm, which involves two pointers moving at different speeds through the list. If a cycle exists, the faster pointer will eventually catch up to the slower pointer.

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
        // if the list is empty, there's no cycle
        if (head == NULL || head->next == NULL) {
            return false;
        }

        // initialize two pointers, one moving twice as fast as the other
        ListNode *slow = head;
        ListNode *fast = head->next;

        // loop through the list
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

        // if the loop ends, it means the fast pointer caught up to the slow pointer, so there's a cycle
        return true;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 2 (cycle at node 2)
Output: true
Input: 1 -> 2 -> 3 -> 4 -> NULL (no cycle)
Output: false
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm is an efficient way to detect cycles in linked lists.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it suitable for large linked lists.
- It's essential to handle edge cases, such as an empty list or a list with only one node, when implementing the algorithm.