# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the merged list should also be sorted in ascending order. The function should take the heads of the two linked lists as input and return the head of the merged linked list. For example, given two linked lists `1 -> 3 -> 5` and `2 -> 4 -> 6`, the merged linked list should be `1 -> 2 -> 3 -> 4 -> 5 -> 6`. The input linked lists can be of different lengths, and the function should handle cases where one or both of the input linked lists are empty.

## Approach
The algorithm uses a recursive approach to compare nodes from both lists and merge them in sorted order. It creates a new linked list with the smaller node from the two lists and recursively merges the remaining nodes. The function handles edge cases where one or both lists are empty.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // Create a dummy node to simplify the merging process
        ListNode* dummy = new ListNode();
        ListNode* current = dummy;
        
        // Merge the two lists
        while (l1 != nullptr && l2 != nullptr) {
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        
        // Append the remaining nodes from either list
        if (l1 != nullptr) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        // Return the head of the merged list
        ListNode* head = dummy->next;
        delete dummy;
        return head;
    }
};
```

## Test Cases
```
Input: l1 = [1, 3, 5], l2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
Input: l1 = [], l2 = [2, 4, 6]
Output: [2, 4, 6]
Input: l1 = [1, 3, 5], l2 = []
Output: [1, 3, 5]
```

## Key Takeaways
- The function uses a recursive approach to merge the two sorted linked lists.
- It creates a dummy node to simplify the merging process and avoid special handling for the head of the merged list.
- The function has a time complexity of O(n + m), where n and m are the lengths of the input linked lists, and a space complexity of O(n + m) due to the creation of a new linked list.