# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null. The linked list has at least one node, and all the values are unique. The cycle can only start from one of the nodes in the linked list, and the cycle does not have to start from the head of the linked list. For example, given the head of a linked list with a cycle, 3 -> 2 -> 0 -> -4 -> 2, the function should return the node with value -4, which is the node where the cycle begins.

## Approach
We can use Floyd's Tortoise and Hare algorithm to detect the cycle and then find the start of the cycle. The algorithm uses two pointers that move at different speeds through the list. If a cycle exists, the two pointers will eventually meet at some node within the cycle.

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
    ListNode *detectCycle(ListNode *head) {
        // if the list is empty, return null
        if (head == NULL) {
            return NULL;
        }
        
        // initialize two pointers, tortoise and hare
        ListNode *tortoise = head;
        ListNode *hare = head;
        
        // move tortoise one step at a time, and hare two steps at a time
        while (hare != NULL && hare->next != NULL) {
            tortoise = tortoise->next;
            hare = hare->next->next;
            
            // if the tortoise and hare meet, there is a cycle
            if (tortoise == hare) {
                break;
            }
        }
        
        // if the hare reaches the end of the list, there is no cycle
        if (hare == NULL || hare->next == NULL) {
            return NULL;
        }
        
        // reset the tortoise to the head of the list
        tortoise = head;
        
        // move the tortoise and hare one step at a time
        while (tortoise != hare) {
            tortoise = tortoise->next;
            hare = hare->next;
        }
        
        // the tortoise and hare will meet at the start of the cycle
        return tortoise;
    }
};
```

## Test Cases
```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect a cycle in a linked list.
- After detecting the cycle, we can reset one of the pointers to the head of the list and move both pointers one step at a time to find the start of the cycle.
- The time complexity of the algorithm is O(n), where n is the number of nodes in the linked list, and the space complexity is O(1), as we only use a constant amount of space.