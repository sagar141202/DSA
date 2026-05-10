# Merge K Sorted Lists

## Problem Statement
Merge k sorted linked lists into one sorted linked list. Given an array of `ListNode*` of size k, where each `ListNode*` represents the head of a sorted linked list, return a single sorted linked list. Each linked list node has a value and a pointer to the next node. The input linked lists are non-empty, and each node has a unique value. For example, given `[[1,4,5],[1,3,4],[2,6]]`, the output should be `[1,1,2,3,4,4,5,6]`.

## Approach
We can use a priority queue to store the current smallest node from each linked list. The priority queue will automatically keep track of the smallest node, and we can repeatedly remove the smallest node and add the next node from the same linked list. This process continues until all nodes have been processed.

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
Input: [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Input: [[1,2,3],[4,5,6]]
Output: [1,2,3,4,5,6]
```

## Key Takeaways
- Using a priority queue to efficiently select the smallest node from each linked list.
- Iteratively removing the smallest node and adding the next node from the same linked list until all nodes have been processed.
- The time complexity is O(N log k), where N is the total number of nodes and k is the number of linked lists.