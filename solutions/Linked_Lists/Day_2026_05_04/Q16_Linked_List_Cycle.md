# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is present and false otherwise. The linked list may have up to 10^5 nodes, and each node may have a value between -10^5 and 10^5. For example, given the head of a linked list with the values [3, 2, 0, -4] and a cycle at the node with value 0, the function should return true.

## Approach
We can solve this problem using Floyd's Tortoise and Hare algorithm, which uses two pointers that move at different speeds. If a cycle is present, the two pointers will eventually meet at some node within the cycle. The intuition is that the faster pointer will eventually catch up to the slower pointer if a cycle is present.

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
    bool hasCycle(ListNode *head) {
        // if the list is empty, there's no cycle
        if (head == NULL || head->next == NULL) {
            return false;
        }
        
        // initialize two pointers, one moving twice as fast as the other
        ListNode *slow = head;
        ListNode *fast = head->next;
        
        // move the pointers through the list
        while (slow != fast) {
            // if the fast pointer reaches the end, there's no cycle
            if (fast == NULL || fast->next == NULL) {
                return false;
            }
            
            // move the slow pointer one step
            slow = slow->next;
            
            // move the fast pointer two steps
            fast = fast->next->next;
        }
        
        // if the pointers meet, there's a cycle
        return true;
    }
};
```

## Test Cases
```
Input: head = [3, 2, 0, -4], pos = 1 (cycle at node with value 0)
Output: true

Input: head = [1, 2], pos = 0 (cycle at node with value 1)
Output: true

Input: head = [1], pos = -1 (no cycle)
Output: false
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect cycles in linked lists.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large linked lists.
- The algorithm uses two pointers moving at different speeds to detect cycles, making it a simple yet effective solution.