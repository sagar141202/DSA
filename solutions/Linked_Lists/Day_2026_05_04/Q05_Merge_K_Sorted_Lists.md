# Merge K Sorted Lists

## Problem Statement
Given an array of 'k' sorted linked lists, merge them into one sorted linked list. Each node in the linked list has a value and a pointer to the next node. The input linked lists are sorted in ascending order, and the output linked list should also be sorted in ascending order. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged linked list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6. The function should take the heads of the 'k' linked lists as input and return the head of the merged linked list.

## Approach
We can use a priority queue to store the current smallest node from each linked list. We remove the smallest node from the queue, add it to the result list, and insert the next node from the same list into the queue. This process continues until all nodes are processed. The priority queue ensures that the smallest node is always removed first, resulting in a sorted merged list. We use a min-heap as our priority queue, where each element is a pair containing the node's value and the list it belongs to.

## Complexity
- Time: O(N log k)
- Space: O(k)

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

struct compare {
    bool operator()(const ListNode* a, const ListNode* b) {
        return a->val > b->val;
    }
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // Create a min-heap to store the current smallest node from each list
        priority_queue<ListNode*, vector<ListNode*>, compare> minHeap;
        
        // Add the head of each list to the min-heap
        for (ListNode* node : lists) {
            if (node) {
                minHeap.push(node);
            }
        }
        
        // Create a dummy node to serve as the head of the result list
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Merge the linked lists
        while (!minHeap.empty()) {
            // Remove the smallest node from the min-heap
            ListNode* smallest = minHeap.top();
            minHeap.pop();
            
            // Add the smallest node to the result list
            current->next = smallest;
            current = current->next;
            
            // Add the next node from the same list to the min-heap
            if (smallest->next) {
                minHeap.push(smallest->next);
            }
        }
        
        // Return the head of the merged linked list
        return dummy->next;
    }
};
```

## Test Cases
```
Input: [
  1 -> 4 -> 5,
  1 -> 3 -> 4,
  2 -> 6
]
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

Input: []
Output: null

Input: [
  1 -> 2 -> 3
]
Output: 1 -> 2 -> 3
```

## Key Takeaways
- Use a priority queue to efficiently merge the linked lists.
- Utilize a min-heap to ensure the smallest node is always removed first.
- Create a dummy node to simplify the process of building the result list.