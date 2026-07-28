# Merge K Sorted Lists

## Problem Statement
Merge k sorted linked lists into one sorted linked list. Given an array of `ListNode*` of size `k`, where each `ListNode*` represents the head of a sorted linked list, return a single sorted linked list. The lists are non-empty, and each node has a unique value. For example, if the input is `[[1,4,5],[1,3,4],[2,6]]`, the output should be `[1,1,2,3,4,4,5,6]`.

## Approach
The algorithm uses a priority queue to store the current smallest node from each linked list. It repeatedly pops the smallest node from the queue and adds it to the result list, then pushes the next node from the same linked list into the queue. This process continues until all nodes have been processed.

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
Input: [[1,2,3],[4,5,6]]
Output: [1,2,3,4,5,6]
```

## Key Takeaways
- Using a priority queue to efficiently select the smallest node from the linked lists.
- Iterating through the linked lists and adding nodes to the priority queue ensures that the smallest node is always processed first.
- The time complexity is O(N log k) due to the priority queue operations, where N is the total number of nodes and k is the number of linked lists.