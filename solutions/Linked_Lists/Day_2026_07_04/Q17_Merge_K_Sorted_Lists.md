# Merge K Sorted Lists

## Problem Statement
Given an array of 'k' sorted linked lists, merge them into one sorted linked list. Each linked list is sorted in ascending order. The merged linked list should also be sorted in ascending order. For example, if we have three sorted linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged linked list will be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6.

## Approach
We can use a priority queue to store the current smallest node from each linked list. We then pop the smallest node from the priority queue, add it to the result, and push the next node from the same linked list into the priority queue. This process continues until all nodes are processed.

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
        for (auto node : lists) {
            if (node) pq.push(node);
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
Input: [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Input: []
Output: []
Input: [[]]
Output: []
```

## Key Takeaways
- Use of priority queue to efficiently merge 'k' sorted linked lists.
- The time complexity is O(N log k) due to the priority queue operations, where 'N' is the total number of nodes and 'k' is the number of linked lists.
- The space complexity is O(k) for storing the current smallest node from each linked list in the priority queue.