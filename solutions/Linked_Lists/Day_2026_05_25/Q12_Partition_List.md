# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of the nodes should be preserved. For example, given the list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
We can solve this problem by maintaining two separate lists: one for nodes with values less than x and another for nodes with values greater than or equal to x. We then concatenate these two lists to get the final partitioned list.

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
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        // Create two dummy nodes to simplify some corner cases
        ListNode* before_head = new ListNode(0);
        ListNode* before = before_head;
        ListNode* after_head = new ListNode(0);
        ListNode* after = after_head;

        // Partition the list
        while (head) {
            if (head->val < x) {
                before->next = head;
                before = before->next;
            } else {
                after->next = head;
                after = after->next;
            }
            head = head->next;
        }

        // Concatenate the two lists
        after->next = NULL;
        before->next = after_head->next;

        // Return the head of the partitioned list
        ListNode* new_head = before_head->next;
        delete before_head;
        delete after_head;
        return new_head;
    }
};
```

## Test Cases
```
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Input: head = [2,1], x = 2
Output: [1,2]
```

## Key Takeaways
- We use two dummy nodes to simplify the code and avoid special cases for the head of the lists.
- We iterate through the original list only once, making the time complexity O(n).
- We only use a constant amount of extra space, making the space complexity O(1).