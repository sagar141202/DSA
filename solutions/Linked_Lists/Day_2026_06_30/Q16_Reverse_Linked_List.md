# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes' values are in the range [-5000, 5000]. The list can be empty, and the function should handle this case. For example, if the input list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
The approach is to initialize three pointers: previous, current, and next. We initialize previous as NULL and current as the head of the list. Then, we traverse the list, and for each node, we do the following: store the next node in next, reverse the link of the current node, and move the previous and current pointers one step forward. This way, we reverse the links of all nodes in the list.

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
        // Initialize previous as NULL and current as the head of the list
        ListNode* previous = NULL;
        ListNode* current = head;
        
        // Traverse the list
        while (current != NULL) {
            // Store the next node in next
            ListNode* next = current->next;
            
            // Reverse the link of the current node
            current->next = previous;
            
            // Move the previous and current pointers one step forward
            previous = current;
            current = next;
        }
        
        // Return the new head of the reversed list
        return previous;
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
- We use three pointers to reverse the linked list: previous, current, and next.
- The time complexity is O(n), where n is the number of nodes in the list, because we traverse the list once.
- The space complexity is O(1) because we only use a constant amount of space to store the pointers.