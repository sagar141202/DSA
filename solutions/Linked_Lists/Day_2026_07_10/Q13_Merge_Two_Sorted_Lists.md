# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order. The function should take the heads of the two linked lists as input and return the head of the merged linked list. For example, given two lists `1 -> 3 -> 5` and `2 -> 4 -> 6`, the merged list should be `1 -> 2 -> 3 -> 4 -> 5 -> 6`. The lists can be of different lengths.

## Approach
The algorithm uses a recursive approach to merge the two lists by comparing the values of the nodes and adding the smaller value to the result list. The process continues until one of the lists is exhausted, at which point the remaining nodes from the other list are appended to the result.

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
        
        // Return the head of the merged list
        return dummy->next;
    }
};
```

## Test Cases
```
Input: l1 = [1, 3, 5], l2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
Input: l1 = [], l2 = [0]
Output: [0]
Input: l1 = [], l2 = []
Output: []
```

## Key Takeaways
- The time complexity of the solution is O(n + m), where n and m are the lengths of the two input lists.
- The space complexity of the solution is O(n + m), as in the worst case, the merged list will have n + m nodes.
- The solution uses a dummy node to simplify the code and avoid special handling for the head of the merged list.