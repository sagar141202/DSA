# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes' values are in the range [-5000, 5000]. The list is guaranteed to be non-null. For example, if the input is [1, 2, 3, 4, 5], the output should be [5, 4, 3, 2, 1].

## Approach
Reverse a linked list by initializing three pointers: previous, current, and next. Initialize previous as NULL and current as the head of the list. Then, traverse the list and reverse the next pointer of each node. The algorithm iterates through the list, updating the next pointer of each node to point to the previous node.

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
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* curr = head;
        while (curr != NULL) {
            ListNode* nextTemp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
Input: []
Output: []
Input: [1]
Output: [1]
```

## Key Takeaways
- To reverse a linked list, we need to update the next pointer of each node to point to the previous node.
- We can use three pointers (previous, current, and next) to achieve this in a single pass through the list.
- The time complexity of this solution is O(n), where n is the number of nodes in the list, and the space complexity is O(1) since we only use a constant amount of space.