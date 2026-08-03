# Merge K Sorted Lists

## Problem Statement
Given an array of 'k' sorted linked lists, merge them into one sorted linked list. Each linked list is sorted in ascending order. The merged linked list should also be sorted in ascending order. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged linked list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6.

## Approach
We can solve this problem by using a priority queue to store the current smallest node from each linked list. The priority queue will automatically keep track of the smallest node, allowing us to efficiently merge the linked lists. We will keep removing the smallest node from the queue and adding it to the merged list until all nodes have been processed.

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
            if (node) {
                pq.push(node);
            }
        }

        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;

        while (!pq.empty()) {
            ListNode* node = pq.top();
            pq.pop();
            curr->next = node;
            curr = curr->next;
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
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

## Key Takeaways
- We use a priority queue to efficiently keep track of the smallest node from each linked list.
- The time complexity is O(N log k) because we perform a heap operation for each node, and each heap operation takes O(log k) time.
- The space complexity is O(k) because we store at most k nodes in the priority queue at any given time.