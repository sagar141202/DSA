# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove duplicates from the list and return the head of the modified list. The list is sorted in ascending order, and each node has a unique value. For example, if the input list is 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the output list should be 1 -> 2 -> 3 -> 4 -> 5. The function should have a time complexity of O(n), where n is the number of nodes in the list.

## Approach
The approach is to traverse the linked list and compare each node's value with the next node's value. If they are the same, remove the next node. This process continues until the end of the list is reached. The function uses a pointer to keep track of the current node and another pointer to keep track of the next node.

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
    ListNode* deleteDuplicates(ListNode* head) {
        // If the list is empty, return NULL
        if (head == NULL) return NULL;
        
        // Initialize two pointers
        ListNode* current = head;
        ListNode* nextNode = head->next;
        
        // Traverse the list
        while (nextNode != NULL) {
            // If the current node's value is the same as the next node's value
            if (current->val == nextNode->val) {
                // Remove the next node
                current->next = nextNode->next;
                nextNode = current->next;
            } else {
                // Move to the next node
                current = nextNode;
                nextNode = nextNode->next;
            }
        }
        
        // Return the head of the modified list
        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5
```

## Key Takeaways
- Use two pointers to traverse the linked list and compare node values.
- Remove nodes with duplicate values by updating the next pointer of the current node.
- The function has a time complexity of O(n), where n is the number of nodes in the list.