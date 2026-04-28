# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes will have unique values in the range [-5000, 5000]. The list is guaranteed to be non-empty, except for the case where the list is empty. For example, if the input list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
We will use a iterative approach to reverse the linked list. We initialize three pointers: previous, current, and next. We traverse the list and reverse the next pointer of each node. This approach ensures that we do not lose track of the nodes as we reverse the list.

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
    ListNode* reverseList(ListNode* head) {
        // Initialize previous and current pointers
        ListNode* prev = NULL;
        ListNode* curr = head;
        
        // Traverse the list and reverse the next pointer of each node
        while (curr != NULL) {
            // Store the next node
            ListNode* nextTemp = curr->next;
            
            // Reverse the next pointer
            curr->next = prev;
            
            // Move the previous and current pointers one step forward
            prev = curr;
            curr = nextTemp;
        }
        
        // At the end, the previous pointer will be pointing to the new head
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
- We use three pointers (previous, current, and next) to reverse the linked list.
- We traverse the list only once, making the time complexity O(n).
- The space complexity is O(1) as we only use a constant amount of space to store the pointers.