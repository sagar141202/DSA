# Merge K Sorted Lists

## Problem Statement
Given an array of 'k' sorted linked lists, merge them into one sorted linked list. Each linked list is sorted in ascending order, and the result should also be sorted in ascending order. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged linked list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6. The input linked lists are non-empty, and each node has a unique value.

## Approach
We can use a priority queue to store the current smallest node from each linked list. The priority queue will be ordered based on the node's value. We will keep removing the smallest node from the queue and adding the next node from the same linked list until all nodes are processed.

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
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
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

        ListNode* dummy = new ListNode();
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
Input: [[1, 4, 5], [1, 3, 4], [2, 6]]
Output: [1, 1, 2, 3, 4, 4, 5, 6]
Input: []
Output: []
Input: [[1]]
Output: [1]
```

## Key Takeaways
- Use a priority queue to efficiently merge the sorted linked lists.
- The time complexity is O(N log k) where N is the total number of nodes and k is the number of linked lists.
- The space complexity is O(k) due to the priority queue.