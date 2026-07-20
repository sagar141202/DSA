# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node becomes the last node of the first half, the second node becomes the last node of the second half, and so on. The problem can be visualized as follows: given a list 1 -> 2 -> 3 -> 4, the reordered list would be 1 -> 4 -> 2 -> 3. The list is 1-indexed. The length of the list is in the range [1, 1000]. The nodes have values in the range [1, 1000].

## Approach
To solve this problem, we can use a two-step approach: first, find the middle of the linked list, then reverse the second half of the list. After reversing the second half, we can merge the two halves by alternating nodes from the first and second halves.

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
- The key to solving this problem is to find the middle of the linked list and reverse the second half.
- We can use the slow and fast pointer approach to find the middle of the list.
- The time complexity of the solution is O(n), where n is the number of nodes in the list, because we are traversing the list twice: once to find the middle and once to reverse the second half.