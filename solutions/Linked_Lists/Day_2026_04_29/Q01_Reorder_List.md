# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node is followed by the last node, then the second node, and so on. For example, given the list 1 -> 2 -> 3 -> 4, the reordered list should be 1 -> 4 -> 2 -> 3. If the list has an odd number of nodes, the middle node should remain in its original position.

## Approach
The approach involves finding the middle of the linked list, reversing the second half, and then merging the two halves. We use the slow and fast pointer technique to find the middle of the list, and then reverse the second half. Finally, we merge the two halves by rearranging the nodes.

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
            ListNode* nextTemp = second->next;
            second->next = prev;
            prev = second;
            second = nextTemp;
        }

        // merge the two halves
        ListNode* first = head;
        second = prev;
        while (second) {
            ListNode* nextTemp1 = first->next;
            ListNode* nextTemp2 = second->next;
            first->next = second;
            second->next = nextTemp1;
            first = nextTemp1;
            second = nextTemp2;
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
- Use the slow and fast pointer technique to find the middle of the linked list.
- Reverse the second half of the list using a simple iterative approach.
- Merge the two halves by rearranging the nodes in a way that satisfies the problem constraints.