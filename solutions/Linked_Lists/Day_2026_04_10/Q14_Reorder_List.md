# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node becomes the last node of the first half, the second node becomes the last node of the second half, and so on. The problem can be visualized as follows: given a list 1 -> 2 -> 3 -> 4, the reordered list would be 1 -> 4 -> 2 -> 3. The list should be reordered in-place.

## Approach
We will use a two-pointer approach to find the middle of the list, then reverse the second half of the list. Finally, we will merge the two halves by alternating nodes from each half.

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
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 5 -> 2 -> 4 -> 3
```

## Key Takeaways
- To find the middle of a linked list, we can use a two-pointer approach with one pointer moving twice as fast as the other.
- Reversing a linked list can be done in-place by keeping track of the previous node and reversing the next pointer of each node.
- Merging two linked lists can be done by alternating nodes from each list.