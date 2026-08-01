# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list has at least one node, and all the values are unique. The cycle must start at some node in the list, and the node where the cycle starts is called the beginning of the cycle. If the list has a cycle, the cycle does not intersect with itself except at the start of the cycle. The list does not contain more than one cycle.

## Approach
We can use Floyd's Tortoise and Hare algorithm to detect the cycle, then find the start of the cycle by moving one of the pointers to the head and keeping the other at the meeting point. Both pointers move one step at a time, and they will meet at the start of the cycle.

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
    ListNode *detectCycle(ListNode *head) {
        if (head == nullptr || head->next == nullptr) {
            return nullptr;
        }

        // Phase 1: Detecting the cycle using Floyd's Tortoise and Hare algorithm
        ListNode *tortoise = head;
        ListNode *hare = head;
        while (hare != nullptr && hare->next != nullptr) {
            tortoise = tortoise->next;  // Move one step at a time
            hare = hare->next->next;    // Move two steps at a time
            if (tortoise == hare) {
                break;
            }
        }

        // If there is no cycle, return nullptr
        if (hare == nullptr || hare->next == nullptr) {
            return nullptr;
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
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Input: head = [1], pos = -1
Output: no cycle
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect a cycle in a linked list.
- If a cycle is detected, we can find the start of the cycle by moving one pointer to the head and keeping the other at the meeting point, then moving both pointers one step at a time.
- The time complexity of this solution is O(n), where n is the number of nodes in the linked list, and the space complexity is O(1) as we only use a constant amount of space.