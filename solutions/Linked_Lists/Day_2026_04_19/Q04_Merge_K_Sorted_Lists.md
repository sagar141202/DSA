# Merge K Sorted Lists

## Problem Statement
Given an array of 'k' linked lists, merge them into one sorted linked list. Each linked list is sorted in ascending order. The input linked lists are non-empty and each node has a unique value. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6.

## Approach
We can solve this problem using a priority queue to keep track of the smallest node from each linked list. We will keep removing the smallest node from the priority queue and add it to our result list, then add the next node from the same list to the priority queue. This process will continue until all nodes are processed.

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
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

## Key Takeaways
- Using a priority queue allows us to efficiently keep track of the smallest node from each linked list.
- The time complexity of this solution is O(N log k), where N is the total number of nodes across all linked lists and k is the number of linked lists.