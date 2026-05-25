# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the resulting list should also be sorted in ascending order. The input lists are defined as follows: `l1` and `l2` are the heads of the two sorted linked lists. The task is to merge these lists and return the head of the merged list. For example, given `l1 = [1, 2, 4]` and `l2 = [1, 3, 4]`, the output should be `[1, 1, 2, 3, 4, 4]`.

## Approach
The approach involves creating a new linked list and comparing the current nodes of `l1` and `l2` to determine which node to add to the new list. This process continues until one of the lists is exhausted, at which point the remaining nodes from the other list are appended to the new list. The algorithm uses a recursive or iterative approach to merge the lists.

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
        // Create a dummy node to simplify some corner cases such as lists with only one node, or removing the head of the list.
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Compare the current nodes of l1 and l2 and add the smaller one to the new list.
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
        
        // If one of the lists is exhausted, append the remaining nodes from the other list.
        if (l1 != nullptr) {
            current->next = l1;
        } else if (l2 != nullptr) {
            current->next = l2;
        }
        
        // Return the head of the merged list (which is the next node of the dummy node).
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
Input: l1 = [0], l2 = []
Output: [0]
```

## Key Takeaways
- The key to solving this problem is to compare the current nodes of the two lists and add the smaller one to the new list.
- Using a dummy node simplifies the code and avoids having to deal with special cases such as an empty list or a list with only one node.
- The time complexity is O(n + m), where n and m are the lengths of the two input lists, because each node is visited once. The space complexity is also O(n + m) because in the worst case, the merged list will contain all nodes from both input lists.