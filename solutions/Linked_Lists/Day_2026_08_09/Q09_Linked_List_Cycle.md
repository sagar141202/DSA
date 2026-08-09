# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is found, and false otherwise. The linked list may have multiple nodes, and each node may have a value and a next pointer. For example, given the head of a linked list with the values [3, 2, 0, -4] and a cycle at the node with value 0, the function should return true. If there is no cycle, the function should return false.

## Approach
The algorithm uses the Floyd's Tortoise and Hare cycle detection approach. Two pointers, a slow pointer and a fast pointer, are initialized to the head of the linked list. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a cycle in the linked list, the fast pointer will eventually catch up to the slow pointer.

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
        // If the list is empty, there is no cycle
        if (head == NULL || head->next == NULL) {
            return false;
        }

        // Initialize the slow and fast pointers
        ListNode *slow = head;
        ListNode *fast = head->next;

        // Loop until the fast pointer reaches the end of the list
        while (slow != fast) {
            // If the fast pointer reaches the end of the list, there is no cycle
            if (fast == NULL || fast->next == NULL) {
                return false;
            }

            // Move the slow pointer one step at a time
            slow = slow->next;

            // Move the fast pointer two steps at a time
            fast = fast->next->next;
        }

        // If the loop ends, there is a cycle in the list
        return true;
    }
};
```

## Test Cases
```
Input: [3, 2, 0, -4] with a cycle at the node with value 0
Output: true

Input: [1, 2] with no cycle
Output: false
```

## Key Takeaways
- Use Floyd's Tortoise and Hare cycle detection approach to detect cycles in linked lists.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large linked lists.
- The algorithm can be applied to other data structures with similar properties, such as graphs.