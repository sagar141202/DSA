# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the nodes are rearranged in the following way: the first node is followed by the last node, then the second node is followed by the second to last node, and so on. The reordered list should be connected in the same way as the original list, and the last node should be connected to `null`. For example, given the list `1 -> 2 -> 3 -> 4`, the reordered list would be `1 -> 4 -> 2 -> 3`. If the list has an odd number of nodes, the middle node should remain in its original position.

## Approach
The algorithm involves finding the middle of the linked list, reversing the second half, and then rearranging the nodes. We find the middle using the slow and fast pointer technique, reverse the second half, and then merge the two halves.

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
        if (!head || !head->next) return;

        // find the middle of the list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // reverse the second half
        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* prev = nullptr;
        while (second) {
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }

        // merge the two halves
        ListNode* first = head;
        second = prev;
        while (second) {
            ListNode* temp1 = first->next;
            ListNode* temp2 = second->next;
            first->next = second;
            second->next = temp1;
            first = temp1;
            second = temp2;
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
- The slow and fast pointer technique can be used to find the middle of a linked list.
- Reversing a linked list can be done iteratively by keeping track of the previous node.
- Merging two linked lists can be done by adjusting the `next` pointers of the nodes.