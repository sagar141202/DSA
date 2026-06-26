# Merge Two Sorted Lists

## Problem Statement
You are given two sorted linked lists, `l1` and `l2`, and you need to merge them into one sorted linked list. The lists are sorted in ascending order, and the merge should also be in ascending order. For example, if `l1` is `1 -> 3 -> 5` and `l2` is `2 -> 4 -> 6`, the merged list should be `1 -> 2 -> 3 -> 4 -> 5 -> 6`. The input lists are non-empty, and each node has a unique integer value.

## Approach
The approach to solve this problem is to compare the current nodes of both lists and add the smaller one to the result list. We will use a dummy node to simplify the code and avoid dealing with special cases for the head of the result list. The algorithm will iterate through both lists until one of them is exhausted, and then append the remaining nodes from the other list.

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
        
        // Merge two sorted lists
        while (l1 && l2) {
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        
        // Append the remaining nodes from the other list
        current->next = l1 ? l1 : l2;
        
        // Return the next node of the dummy node as the result
        return dummy->next;
    }
};
```

## Test Cases
```
Input: l1 = [1, 3, 5], l2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
Input: l1 = [1, 2, 3], l2 = []
Output: [1, 2, 3]
Input: l1 = [], l2 = [1, 2, 3]
Output: [1, 2, 3]
```

## Key Takeaways
- We use a dummy node to simplify the code and avoid dealing with special cases for the head of the result list.
- The time complexity is O(n + m), where n and m are the lengths of the input lists, because we iterate through both lists once.
- The space complexity is O(n + m) because we create a new list with n + m nodes.