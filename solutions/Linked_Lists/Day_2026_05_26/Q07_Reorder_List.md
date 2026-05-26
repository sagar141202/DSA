# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the nodes are rearranged in the following way: the first node is followed by the last node, then the second node is followed by the second last node, and so on. For example, if the input linked list is 1 -> 2 -> 3 -> 4, the output should be 1 -> 4 -> 2 -> 3. If the input linked list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 1 -> 5 -> 2 -> 4 -> 3. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the number of nodes in the linked list.

## Approach
The solution involves finding the middle of the linked list, reversing the second half of the list, and then merging the two halves. This approach ensures that the nodes are rearranged in the required order. The algorithm uses a two-pointer technique to find the middle of the list and a recursive approach to reverse the second half.

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
        // Base case: if the list is empty or has only one node
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
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }

        // Merge the two halves
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
- To solve this problem, we need to find the middle of the linked list and reverse the second half.
- We use a two-pointer technique to find the middle of the list.
- We use a recursive approach to reverse the second half of the list.
- We merge the two halves by rearranging the nodes in the required order.