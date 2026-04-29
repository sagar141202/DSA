# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node becomes the last node of the first half, the second node becomes the second last node of the first half, and so on. The second half of the list remains in the original order. For example, if the input list is 1 -> 2 -> 3 -> 4, the output list should be 1 -> 4 -> 2 -> 3. The length of the linked list is in the range [1, 100].

## Approach
The algorithm involves finding the middle of the linked list, reversing the second half, and then merging the two halves. This approach ensures that the first node becomes the last node of the first half and the second node becomes the second last node of the first half.

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
        
        // find the middle of the linked list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        // reverse the second half of the linked list
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
- To solve this problem, we need to find the middle of the linked list.
- We need to reverse the second half of the linked list.
- We need to merge the two halves in a way that the first node becomes the last node of the first half and the second node becomes the second last node of the first half.