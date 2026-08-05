# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The input lists are sorted in ascending order, and the output list should also be sorted in ascending order. The function should take the heads of the two input lists as input and return the head of the merged list. For example, given two lists `1 -> 3 -> 5` and `2 -> 4 -> 6`, the function should return `1 -> 2 -> 3 -> 4 -> 5 -> 6`. The lists can be of different lengths, and the function should handle cases where one or both lists are empty.

## Approach
The algorithm uses a recursive approach to merge the two lists by comparing the values of the current nodes and appending the smaller value to the result list. The process is repeated until one of the lists is exhausted, at which point the remaining nodes from the other list are appended to the result.

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
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // Create a dummy node to simplify the code
        ListNode* dummy = new ListNode(0);
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
        if (l1) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        // Return the head of the merged list
        return dummy->next;
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
- The algorithm has a time complexity of O(n + m), where n and m are the lengths of the two input lists.
- The algorithm has a space complexity of O(n + m), as it creates a new list with n + m nodes.
- The use of a dummy node simplifies the code and avoids special cases for the head of the list.