# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node is followed by the last node, then the second node is followed by the second to last node, and so on. The problem can be solved by first finding the middle of the linked list, then reversing the second half of the list, and finally merging the two halves. The linked list is 1-indexed, meaning the first node is considered node 1. For example, given the linked list 1 -> 2 -> 3 -> 4, the reordered list would be 1 -> 4 -> 2 -> 3.

## Approach
The algorithm involves three main steps: finding the middle of the linked list, reversing the second half, and merging the two halves. This approach ensures that the list is reordered as required. The time complexity is O(n), where n is the number of nodes in the list.

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
        // Base case: if the list is empty or only contains one node
        if (head == nullptr || head->next == nullptr) {
            return;
        }
        
        // Find the middle of the linked list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next != nullptr && fast->next->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        // Reverse the second half of the linked list
        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* prev = nullptr;
        while (second != nullptr) {
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }
        
        // Merge the two halves
        ListNode* first = head;
        while (prev != nullptr) {
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
- To solve this problem, we need to find the middle of the linked list first.
- Reversing the second half of the linked list is a crucial step.
- Merging the two halves requires careful handling of node pointers to avoid losing any nodes.