# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node and the last node are swapped, the second node and the second to last node are swapped, and so on. The list is 1-indexed. For example, if the input list is 1 -> 2 -> 3 -> 4, the output should be 1 -> 4 -> 2 -> 3. If the input list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 1 -> 5 -> 2 -> 4 -> 3.

## Approach
The approach is to first find the middle of the linked list, then reverse the second half of the list, and finally merge the two halves. The merging process involves alternating between nodes from the first half and the reversed second half.

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
- The key to solving this problem is to find the middle of the linked list and reverse the second half.
- Merging the two halves requires alternating between nodes from the first half and the reversed second half.
- The time complexity is O(n) because we are traversing the linked list three times: once to find the middle, once to reverse the second half, and once to merge the two halves.