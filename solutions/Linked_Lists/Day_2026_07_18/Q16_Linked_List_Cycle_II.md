# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list is defined as a sequence of nodes where each node has a value and a next pointer pointing to the next node in the sequence. A cycle occurs when a node's next pointer points to a previous node in the sequence. The solution should handle cases where the cycle may or may not be present and should be efficient in terms of time and space complexity. For example, given the linked list 3 -> 2 -> 0 -> -4 -> 2, the function should return the node with value 2.

## Approach
We will use the two-pointer technique, also known as the Floyd's Tortoise and Hare algorithm, to detect the cycle and then find the start of the cycle. This approach involves moving two pointers at different speeds through the linked list to detect the cycle and then adjusting the pointers to find the start of the cycle. The key intuition is that if there is a cycle, the fast pointer will eventually meet the slow pointer within the cycle.

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
        if (head == nullptr || head->next == nullptr) {
            return nullptr;
        }

        // Phase 1: Detecting the cycle using Floyd's Tortoise and Hare algorithm
        ListNode *tortoise = head;
        ListNode *hare = head;
        while (hare != nullptr && hare->next != nullptr) {
            tortoise = tortoise->next; // Move one step at a time
            hare = hare->next->next; // Move two steps at a time
            if (tortoise == hare) {
                break;
            }
        }

        if (hare == nullptr || hare->next == nullptr) {
            return nullptr; // No cycle
        }

        // Phase 2: Finding the start of the cycle
        tortoise = head;
        while (tortoise != hare) {
            tortoise = tortoise->next;
            hare = hare->next;
        }

        return tortoise;
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
- The two-pointer technique is effective for detecting cycles in linked lists.
- The algorithm consists of two phases: detecting the cycle and finding the start of the cycle.
- The time complexity is O(n), where n is the number of nodes in the linked list, and the space complexity is O(1) as it only uses a constant amount of space.