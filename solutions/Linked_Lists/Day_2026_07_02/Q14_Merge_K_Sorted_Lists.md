# Merge K Sorted Lists

## Problem Statement
Merge k sorted linked lists into one sorted linked list. Given an array of linked-lists, where each linked-list is sorted in ascending order, merge all the linked-lists into one sorted linked-list. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6. The linked lists are defined as follows: each node has a value and a pointer to the next node.

## Approach
We can solve this problem by using a priority queue to store the current smallest node from each linked list. We then pop the smallest node from the queue, add it to the result list, and push the next node from the same list into the queue. This process continues until all nodes are processed.

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
        for (auto list : lists) {
            if (list) pq.push(list);
        }
        
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        
        while (!pq.empty()) {
            ListNode* node = pq.top();
            pq.pop();
            curr->next = node;
            curr = curr->next;
            if (node->next) pq.push(node->next);
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
- We use a priority queue to store the current smallest node from each linked list.
- We pop the smallest node from the queue, add it to the result list, and push the next node from the same list into the queue.
- The time complexity is O(N log k) where N is the total number of nodes and k is the number of linked lists.