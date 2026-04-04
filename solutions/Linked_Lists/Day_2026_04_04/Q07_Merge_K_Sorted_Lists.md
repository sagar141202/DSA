# Merge K Sorted Lists

## Problem Statement
Given an array of 'k' sorted linked lists, merge them into one sorted linked list. Each linked list is sorted in ascending order. The merged list should also be sorted in ascending order. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6. The input linked lists are non-empty and the nodes have unique values.

## Approach
We will use a priority queue to store the nodes from the linked lists. The priority queue will be sorted based on the node values. We will then pop the smallest node from the queue, add it to the merged list, and push the next node from the same linked list into the queue.

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
        
        // Push the head of each linked list into the priority queue
        for (auto list : lists) {
            if (list) {
                pq.push(list);
            }
        }
        
        // Create a dummy node for the merged list
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Merge the linked lists
        while (!pq.empty()) {
            ListNode* node = pq.top();
            pq.pop();
            current->next = node;
            current = current->next;
            
            // Push the next node from the same linked list into the queue
            if (node->next) {
                pq.push(node->next);
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
```

## Key Takeaways
- Use a priority queue to efficiently merge the linked lists.
- Create a dummy node to simplify the code and avoid special cases for the head of the merged list.
- The time complexity is O(N log k) where N is the total number of nodes and k is the number of linked lists.