# Reorder List

## Problem Statement
Given a singly linked list, reorder it such that the nodes are rearranged in the following way: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ... . For example, if the input list is 1 -> 2 -> 3 -> 4, the output should be 1 -> 4 -> 2 -> 3. The input list is guaranteed to be non-empty and have at least one node. The list should be modified in-place.

## Approach
The approach is to find the middle of the list, reverse the second half, and then merge the two halves. This can be done by using two pointers to find the middle, reversing the second half using a simple reversal algorithm, and then merging the two halves by rearranging the nodes.

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

Input: 1 -> 2 -> 3
Output: 1 -> 3 -> 2
```

## Key Takeaways
- To solve this problem, we need to find the middle of the list, reverse the second half, and then merge the two halves.
- We can use two pointers to find the middle of the list, with one pointer moving twice as fast as the other.
- We can reverse a linked list by keeping track of the previous node and updating the next pointer of each node.