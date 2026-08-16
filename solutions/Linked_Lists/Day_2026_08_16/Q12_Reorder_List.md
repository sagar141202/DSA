# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node and the last node are swapped, the second node and the second-to-last node are swapped, and so on. The list should be modified in-place. For example, if the input list is 1 -> 2 -> 3 -> 4, the output list should be 1 -> 4 -> 2 -> 3. If the input list has an odd number of nodes, the middle node remains in its original position.

## Approach
The approach is to first find the middle of the linked list, then reverse the second half of the list, and finally merge the two halves. This can be achieved by using three pointers: one for the current node, one for the next node, and one for the node after the next node.

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
        if (!head || !head->next || !head->next->next) return;

        // find the middle of the linked list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // reverse the second half of the list
        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* prev = nullptr;
        while (second) {
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }

        // merge two sorted lists
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
- To reorder a linked list, we need to find the middle of the list, reverse the second half, and then merge the two halves.
- The time complexity of this solution is O(n), where n is the number of nodes in the linked list.
- The space complexity of this solution is O(1), as we only use a constant amount of space to store the pointers.