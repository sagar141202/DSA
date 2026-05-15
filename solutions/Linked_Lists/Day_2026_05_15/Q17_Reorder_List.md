# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node becomes the first node of the reordered list, the last node becomes the second node, the second node becomes the third node, and so on. The reordered list should be in the form: `1 -> n -> 2 -> (n - 1) -> 3 -> (n - 2) -> ...`. The input linked list will have at least one node and at most 10^4 nodes. Each node's value will be between 1 and 10^4.

## Approach
The algorithm involves finding the middle of the linked list, reversing the second half, and then merging the two halves. This approach ensures the list is reordered as required. We use two pointers to find the middle and then reverse the second half. Finally, we merge the two halves by alternating between the nodes of the two lists.

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
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    void reorderList(ListNode* head) {
        if (head == NULL || head->next == NULL) {
            return;
        }
        
        // Find the middle of the linked list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next != NULL && fast->next->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        // Reverse the second half of the linked list
        ListNode* second = slow->next;
        slow->next = NULL;
        ListNode* prev = NULL;
        while (second != NULL) {
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }
        
        // Merge the two halves
        ListNode* first = head;
        while (prev != NULL) {
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
- To solve this problem, we first need to find the middle of the linked list.
- Then we reverse the second half of the linked list.
- Finally, we merge the two halves by alternating between the nodes of the two lists.