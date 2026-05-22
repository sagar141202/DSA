# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node in the list. The function should return true if a cycle is found and false otherwise. The linked list is defined as a sequence of nodes, where each node has a value and a next pointer to the next node in the list. The input linked list is represented as a sequence of nodes, where each node is an instance of the ListNode class, which has an integer value and a next pointer to the next node in the list. For example, given a linked list with the following nodes: 1 -> 2 -> 3 -> 4 -> 2, the function should return true because there is a cycle in the list.

## Approach
The algorithm uses Floyd's Tortoise and Hare (Cycle Detection) algorithm, which uses two pointers that move at different speeds through the list. If there is a cycle, these two pointers will eventually meet. The intuition behind this approach is that if there is a cycle, the fast pointer will eventually catch up to the slow pointer.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
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

        // loop until the fast pointer reaches the end of the list
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

        // if the loop exits, it means the fast pointer caught up to the slow pointer, so there is a cycle
        return true;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 2
Output: true

Input: 1 -> 2 -> 3 -> 4 -> 5
Output: false
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large linked lists.
- The algorithm uses two pointers that move at different speeds through the list to detect cycles.