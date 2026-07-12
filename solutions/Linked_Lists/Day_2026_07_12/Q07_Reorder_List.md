# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the nodes are rearranged in the following way: the first node is followed by the last node, then the second node is followed by the second-to-last node, and so on. The reordered list should be modified in-place. The length of the list is in the range [1, 20000]. The nodes in the list have values in the range [1, 100000].

## Approach
The approach involves finding the middle of the linked list, reversing the second half, and then merging the two halves. We use the slow and fast pointer technique to find the middle, and a recursive or iterative approach to reverse the second half.

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

        // Find the middle of the linked list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Reverse the second half
        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* prev = nullptr;
        while (second) {
            ListNode* nextTemp = second->next;
            second->next = prev;
            prev = second;
            second = nextTemp;
        }

        // Merge the two halves
        ListNode* first = head;
        while (prev) {
            ListNode* nextTemp1 = first->next;
            ListNode* nextTemp2 = prev->next;
            first->next = prev;
            prev->next = nextTemp1;
            first = nextTemp1;
            prev = nextTemp2;
        }
    }
};
```

## Test Cases
```
Input: [1,2,3,4]
Output: [1,4,2,3]
Input: [1,2,3,4,5]
Output: [1,5,2,4,3]
```

## Key Takeaways
- The slow and fast pointer technique can be used to find the middle of a linked list.
- Reversing a linked list can be done recursively or iteratively.
- Merging two linked lists can be done by adjusting the next pointers of the nodes.