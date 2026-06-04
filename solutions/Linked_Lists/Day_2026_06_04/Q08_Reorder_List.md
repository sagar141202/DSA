# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the nodes are rearranged in the following way: the first node is followed by the last node, then the second node, then the second-to-last node, and so on. The reordering should be done in-place and only use a constant amount of extra space. For example, if the input list is 1 -> 2 -> 3 -> 4, the output should be 1 -> 4 -> 2 -> 3. If the input list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 1 -> 5 -> 2 -> 4 -> 3.

## Approach
The approach is to first find the middle of the list, then reverse the second half of the list, and finally merge the two halves. This can be done by using two pointers to find the middle, then reversing the second half, and finally iterating over the two halves to merge them.

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
- To solve this problem, we need to find the middle of the list and reverse the second half.
- We can use two pointers to find the middle of the list.
- We can reverse the second half of the list by iterating over it and changing the next pointers of each node.
- Finally, we can merge the two halves by iterating over them and changing the next pointers of each node.