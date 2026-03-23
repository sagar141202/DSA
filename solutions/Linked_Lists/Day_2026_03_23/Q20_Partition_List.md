# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of nodes with values less than x and nodes with values greater than or equal to x should remain the same. The list should be partitioned in-place.

## Approach
The algorithm involves creating two separate linked lists, one for nodes with values less than x and one for nodes with values greater than or equal to x. We then concatenate these two lists to obtain the final partitioned list. This approach ensures that the relative order of nodes is preserved.

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
    ListNode* partition(ListNode* head, int x) {
        // Create two dummy nodes to serve as the heads of the two separate lists
        ListNode* beforeHead = new ListNode(0);
        ListNode* afterHead = new ListNode(0);
        
        // Initialize pointers to the current nodes in the two separate lists
        ListNode* before = beforeHead;
        ListNode* after = afterHead;
        
        // Traverse the original list
        while (head != nullptr) {
            // If the current node's value is less than x, add it to the "before" list
            if (head->val < x) {
                before->next = head;
                before = before->next;
            } 
            // Otherwise, add it to the "after" list
            else {
                after->next = head;
                after = after->next;
            }
            // Move to the next node in the original list
            head = head->next;
        }
        
        // Connect the "before" list to the "after" list
        after->next = nullptr;
        before->next = afterHead->next;
        
        // Return the head of the partitioned list
        ListNode* result = beforeHead->next;
        delete beforeHead;
        delete afterHead;
        return result;
    }
};
```

## Test Cases
```
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
```

## Key Takeaways
- We use two separate linked lists to partition the original list based on the given value x.
- The relative order of nodes is preserved by maintaining the original order within each separate list.
- The solution has a time complexity of O(n) and a space complexity of O(1), where n is the number of nodes in the linked list.