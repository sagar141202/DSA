# Merge Two Sorted Lists

## Problem Statement
Given two sorted linked lists, merge them into a single sorted linked list. The nodes of the linked lists should be merged in a way that the resulting list is also sorted. For example, given two lists 1 -> 2 -> 4 and 1 -> 3 -> 4, the merged list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4. The input lists can be empty, and the resulting list should also handle this case.

## Approach
We can solve this problem by using a simple iterative approach, comparing the values of the nodes of the two lists and adding the smaller value to the merged list. We will use a dummy node to simplify the code and handle edge cases. The algorithm will run in linear time, proportional to the total number of nodes in the input lists.

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
        // Create a dummy node to simplify the code
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
        
        // Add any remaining nodes
        if (l1 != nullptr) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        // Return the merged list
        return dummy->next;
    }
};
```

## Test Cases
```
Input: l1 = [1, 2, 4], l2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
Input: l1 = [], l2 = [0]
Output: [0]
Input: l1 = [], l2 = []
Output: []
```

## Key Takeaways
- We can merge two sorted linked lists in linear time using a simple iterative approach.
- Using a dummy node can simplify the code and handle edge cases.
- The space complexity is O(n + m) because we need to store the merged list, but the time complexity is also O(n + m) because we only visit each node once.