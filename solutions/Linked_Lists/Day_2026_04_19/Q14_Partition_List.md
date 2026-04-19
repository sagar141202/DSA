# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the list such that all nodes with a value less than x come before all nodes with a value greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be preserved. The list should be partitioned in-place.

## Approach
We can solve this problem by maintaining two separate linked lists, one for nodes with values less than x and one for nodes with values greater than or equal to x. Then, we concatenate these two lists to get the final partitioned list.

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
        // Create two dummy nodes to simplify the code
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

        // Connect the two lists
        after->next = NULL;
        before->next = after_head->next;

        // Return the result
        ListNode* result = before_head->next;
        delete before_head;
        delete after_head;
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
- We use two dummy nodes to simplify the code and avoid edge cases.
- We iterate through the list only once to achieve a time complexity of O(n).
- The space complexity is O(1) since we only use a constant amount of space to store the dummy nodes and other variables.