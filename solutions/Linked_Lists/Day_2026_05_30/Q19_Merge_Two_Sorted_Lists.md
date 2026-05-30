# Merge Two Sorted Lists

## Problem Statement
Given two sorted linked lists, merge them into one sorted linked list. The nodes in the lists should be merged in a way that the resulting list is also sorted. For example, if the first list is 1 -> 3 -> 5 and the second list is 2 -> 4 -> 6, the merged list should be 1 -> 2 -> 3 -> 4 -> 5 -> 6. The input lists are non-empty and the nodes have a value and a pointer to the next node.

## Approach
We will use a simple iterative approach to merge the two lists, comparing the values of the current nodes in both lists and appending the smaller value to the result list. We will keep track of the current nodes in both lists and move them forward accordingly.

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
        // Create a new dummy node to serve as the start of the result list
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // While there are still nodes in both lists
        while (l1 != nullptr && l2 != nullptr) {
            // If the value of the current node in l1 is smaller, append it to the result list
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            } 
            // Otherwise, append the current node in l2 to the result list
            else {
                current->next = l2;
                l2 = l2->next;
            }
            // Move the current pointer forward
            current = current->next;
        }
        
        // If there are remaining nodes in l1, append them to the result list
        if (l1 != nullptr) {
            current->next = l1;
        } 
        // If there are remaining nodes in l2, append them to the result list
        else if (l2 != nullptr) {
            current->next = l2;
        }
        
        // Return the next node of the dummy node, which is the start of the result list
        return dummy->next;
    }
};
```

## Test Cases
```
Input: l1 = [1, 2, 4], l2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
Input: l1 = [], l2 = []
Output: []
Input: l1 = [], l2 = [0]
Output: [0]
```

## Key Takeaways
- The time complexity of the solution is O(n + m), where n and m are the lengths of the input lists.
- The space complexity of the solution is O(n + m), as we need to store the result list.
- We use a dummy node to simplify the code and avoid special cases for the head of the result list.