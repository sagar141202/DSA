# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node becomes the last node of the first half, the second node becomes the first node of the second half, the third node becomes the second node of the second half, and so on. The problem assumes that the input linked list has at least one node. For example, if the input linked list is 1 -> 2 -> 3 -> 4, the reordered list should be 1 -> 4 -> 2 -> 3.

## Approach
We can solve this problem by first finding the middle of the linked list, then reversing the second half of the list, and finally merging the two halves in an alternating manner. This approach ensures that the nodes are reordered as required.

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
        // Base case: if the list has 0 or 1 node, it's already reordered
        if (!head || !head->next || !head->next->next) return;

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
- To reorder a linked list, we can divide it into two halves and then merge them in an alternating manner.
- Finding the middle of a linked list can be done using the slow and fast pointer technique.
- Reversing a linked list can be done by iterating through the list and updating the next pointers of each node.