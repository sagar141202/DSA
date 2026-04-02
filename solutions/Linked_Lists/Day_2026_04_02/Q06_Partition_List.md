# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of the nodes should be preserved. For example, given a linked list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
We will create two separate linked lists, one for values less than x and one for values greater than or equal to x. Then we will concatenate these two lists to form the final partitioned list. This approach ensures that the relative order of the nodes is preserved.

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
        // Create two dummy nodes for the two lists
        ListNode* before_head = new ListNode(0);
        ListNode* after_head = new ListNode(0);
        
        // Pointers for the two lists
        ListNode* before = before_head;
        ListNode* after = after_head;
        
        // Traverse the original list
        while (head) {
            // If the current node's value is less than x, add it to the before list
            if (head->val < x) {
                before->next = head;
                before = before->next;
            } 
            // Otherwise, add it to the after list
            else {
                after->next = head;
                after = after->next;
            }
            head = head->next;
        }
        
        // Connect the two lists
        after->next = nullptr;
        before->next = after_head->next;
        
        // Return the head of the partitioned list
        ListNode* result = before_head->next;
        delete before_head;
        delete after_head;
        return result;
    }
};
```

## Test Cases
```
Input: head = [1, 4, 3, 2, 5, 2], x = 3
Output: [1, 2, 2, 4, 3, 5]
```

## Key Takeaways
- We use two dummy nodes to simplify the code and avoid edge cases.
- We traverse the original list only once, making the time complexity O(n).
- The space complexity is O(1) as we only use a constant amount of space to store the dummy nodes and pointers.