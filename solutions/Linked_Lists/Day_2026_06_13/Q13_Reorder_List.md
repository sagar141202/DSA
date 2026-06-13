# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the nodes are rearranged in the following way: the first node is followed by the last node, then the second node, then the second-to-last node, and so on. The reordered list should be modified in-place. For example, if the input list is 1 -> 2 -> 3 -> 4, the output should be 1 -> 4 -> 2 -> 3. If the input list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 1 -> 5 -> 2 -> 4 -> 3.

## Approach
The approach to solve this problem is to first find the middle of the linked list, then reverse the second half of the list, and finally merge the two halves in an alternating manner. This can be achieved by using a two-pointer technique to find the middle, a recursive or iterative approach to reverse the second half, and a simple merge step.

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

        // Find the middle of the list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Reverse the second half of the list
        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* prev = nullptr;
        while (second) {
            ListNode* nextTemp = second->next;
            second->next = prev;
            prev = second;
            second = nextTemp;
        }

        // Merge the two halves in an alternating manner
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
- To solve this problem, we need to find the middle of the linked list, reverse the second half, and then merge the two halves.
- We use a two-pointer technique to find the middle of the list, where the fast pointer moves twice as fast as the slow pointer.
- We use a recursive or iterative approach to reverse the second half of the list.
- Finally, we merge the two halves in an alternating manner by updating the next pointers of the nodes.