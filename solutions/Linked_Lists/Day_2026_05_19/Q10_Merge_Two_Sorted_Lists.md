# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order. The function should take the heads of the two lists as input and return the head of the merged list. For example, given two lists 1 -> 2 -> 4 and 1 -> 3 -> 4, the merged list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4. The lists can be of different lengths.

## Approach
We will create a new dummy node and compare the values of the nodes in the two lists. The smaller value will be appended to the new list. This process will continue until all nodes from both lists have been merged.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define the structure for a linked list node
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // Create a new dummy node
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Merge the two lists
        while (l1 != NULL && l2 != NULL) {
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        
        // Append the remaining nodes, if any
        if (l1 != NULL) {
            current->next = l1;
        } else if (l2 != NULL) {
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
Input: l1 = [1, 2, 4], l2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
Input: l1 = [], l2 = [0]
Output: [0]
Input: l1 = [1], l2 = []
Output: [1]
```

## Key Takeaways
- We use a dummy node to simplify the merging process.
- The time complexity is O(n + m), where n and m are the lengths of the two input lists.
- The space complexity is O(n + m) for the merged list.