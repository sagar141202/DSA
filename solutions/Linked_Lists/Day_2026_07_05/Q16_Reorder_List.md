# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node becomes the last node of the first half, the second node becomes the last node of the second half, and so on. The problem can be visualized as follows: given a list 1 -> 2 -> 3 -> 4, the reordered list would be 1 -> 4 -> 2 -> 3. If the list has an odd number of nodes, the middle node should remain in its original position. The list should be reordered in-place.

## Approach
The approach to solving this problem involves finding the middle of the linked list, reversing the second half, and then merging the two halves. This can be achieved by using two pointers to find the middle, reversing the second half using a simple iterative approach, and then reordering the nodes.

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
        // base case
        if (!head || !head->next || !head->next->next) return;

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
- To find the middle of a linked list, use the slow and fast pointer approach.
- To reverse a linked list, use a simple iterative approach with three pointers: previous, current, and next.
- To merge two linked lists, iterate through both lists and adjust the next pointers accordingly.