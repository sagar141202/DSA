# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node becomes the last node of the first half, the second node becomes the first node of the second half, and so on. The problem should be solved in-place, and the solution should have a time complexity of O(n) and a space complexity of O(1), where n is the number of nodes in the linked list. For example, if the input list is 1 -> 2 -> 3 -> 4, the output list should be 1 -> 4 -> 2 -> 3.

## Approach
The algorithm involves finding the middle of the linked list, reversing the second half, and then merging the two halves. We can find the middle of the list using the slow and fast pointer technique, reverse the second half using a simple iterative approach, and then merge the two halves by adjusting the next pointers of the nodes.

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
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    void reorderList(ListNode* head) {
        // Base case: if the list has 0 or 1 nodes, it is already reordered
        if (!head || !head->next || !head->next->next) return;

        // Find the middle of the list using the slow and fast pointer technique
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Reverse the second half of the list
        ListNode* second = slow->next;
        slow->next = nullptr;  // Break the list into two halves
        ListNode* prev = nullptr;
        while (second) {
            ListNode* next = second->next;
            second->next = prev;
            prev = second;
            second = next;
        }
        second = prev;  // Update the head of the second half

        // Merge the two halves
        ListNode* first = head;
        while (second) {
            ListNode* next1 = first->next;
            ListNode* next2 = second->next;
            first->next = second;
            second->next = next1;
            first = next1;
            second = next2;
        }
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4
Output: 1 -> 4 -> 2 -> 3
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 5 -> 2 -> 4 -> 3
```

## Key Takeaways
- The slow and fast pointer technique can be used to find the middle of a linked list in O(n) time complexity.
- Reversing a linked list can be done in O(n) time complexity using a simple iterative approach.
- Merging two linked lists can be done by adjusting the next pointers of the nodes in O(n) time complexity.