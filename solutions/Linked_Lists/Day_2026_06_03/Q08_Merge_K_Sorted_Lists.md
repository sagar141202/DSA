# Merge K Sorted Lists

## Problem Statement
Given an array of 'k' linked lists, merge them into one sorted linked list. Each linked list is sorted in ascending order. The function should take the array of linked lists as input and return the head of the merged linked list. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged linked list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6. The input linked lists are non-empty and do not contain duplicate values.

## Approach
We can use a priority queue to store the current smallest node from each linked list. The priority queue will be ordered based on the node's value. We repeatedly pop the smallest node from the queue, add it to the result list, and push the next node from the same list into the queue.

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

class Solution {
public:
    struct compare {
        bool operator()(const ListNode* a, const ListNode* b) {
            return a->val > b->val;
        }
    };

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, compare> pq;
        
        // Add the head of each linked list to the priority queue
        for (auto list : lists) {
            if (list) {
                pq.push(list);
            }
        }

        // Create a dummy node to serve as the head of the result list
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;

        while (!pq.empty()) {
            // Pop the smallest node from the queue and add it to the result list
            ListNode* smallest = pq.top();
            pq.pop();
            current->next = smallest;
            current = current->next;

            // Push the next node from the same list into the queue
            if (smallest->next) {
                pq.push(smallest->next);
            }
        }

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
Output: NULL

Input: [
  1 -> 2 -> 3
]
Output: 1 -> 2 -> 3
```

## Key Takeaways
- Use a priority queue to efficiently select the smallest node from the current nodes of the linked lists.
- Create a dummy node to simplify the code and avoid special cases for the head of the result list.
- Iterate through the priority queue until it is empty to ensure all nodes are merged into the result list.