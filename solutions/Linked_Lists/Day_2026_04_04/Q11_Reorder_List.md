# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node becomes the last node of the first half, the second node becomes the first node of the second half, and so on. The length of the list is in the range [1, 100]. The nodes are numbered from 1 to n, where n is the length of the list. You may not modify the values in the list's nodes, only the nodes themselves may be changed. For example, given the list 1 -> 2 -> 3 -> 4, the reordered list should be 1 -> 4 -> 2 -> 3.

## Approach
We can solve this problem by first finding the middle of the linked list, then reversing the second half of the list, and finally merging the two halves. This approach ensures that the nodes are reordered as required.

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
        // base case: if the list has 0 or 1 node, it is already reordered
        if (!head || !head->next || !head->next->next) {
            return;
        }

        // find the middle of the list
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
- To reorder a linked list, we can use a combination of finding the middle, reversing the second half, and merging the two halves.
- We need to be careful when handling the edges of the list, such as the base case where the list has 0 or 1 node.
- The time complexity of this solution is O(n), where n is the length of the list, because we are traversing the list a constant number of times.