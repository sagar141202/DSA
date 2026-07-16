# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the nodes are rearranged in the following way: the first node is followed by the last node, then the second node is followed by the second to last node, and so on. The rearrangement should be done in a way that the original data of the nodes is preserved. For example, given the list 1 -> 2 -> 3 -> 4, the reordered list would be 1 -> 4 -> 2 -> 3. The list is 1-indexed, meaning the first node is considered the first node, not the zeroth node. The length of the linked list is in the range [1, 10000].

## Approach
The solution involves finding the middle of the linked list, reversing the second half of the list, and then rearranging the nodes. We can use a two-pointer approach to find the middle of the list and then reverse the second half. Finally, we can rearrange the nodes by iterating through the first half and the reversed second half.

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

        // rearrange the nodes
        ListNode* first = head;
        while (prev) {
            ListNode* temp1 = first->next;
            ListNode* temp2 = prev->next;
            first->next = prev;
            prev->next = temp1;
            first = temp1;
            prev = temp2;
        }
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4
Output: 1 -> 4 -> 2 -> 3
```

## Key Takeaways
- To solve this problem, we need to find the middle of the linked list and reverse the second half of the list.
- We can use a two-pointer approach to find the middle of the list and then reverse the second half.
- The time complexity of the solution is O(n), where n is the number of nodes in the linked list.