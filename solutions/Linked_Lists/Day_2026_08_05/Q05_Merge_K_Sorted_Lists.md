# Merge K Sorted Lists

## Problem Statement
Given an array of `k` sorted linked lists, merge them into one sorted linked list. Each linked list is defined by a `ListNode` struct, where each node has a `val` (value) and a `next` pointer to the next node in the list. The input is an array of `k` pointers to the head nodes of the linked lists. The output should be the head node of the merged linked list. For example, if we have three linked lists: `1 -> 4 -> 5`, `1 -> 3 -> 4`, and `2 -> 6`, the merged linked list should be `1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6`. The constraint is that the total number of nodes in all linked lists is `n`, and the number of linked lists is `k`.

## Approach
We will use a priority queue to store the current smallest node from each linked list. The priority queue will be ordered based on the value of the nodes. We will repeatedly extract the smallest node from the priority queue and add it to the merged linked list, then insert the next node from the same linked list into the priority queue.

## Complexity
- Time: O(n log k)
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
            if (list) {
                pq.push(list);
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
Input: [[1, 4, 5], [1, 3, 4], [2, 6]]
Output: [1, 1, 2, 3, 4, 4, 5, 6]
```

## Key Takeaways
- Use a priority queue to efficiently select the smallest node from the linked lists.
- Keep track of the current node in the merged linked list to avoid losing the head of the merged list.
- The time complexity is O(n log k) due to the priority queue operations, where n is the total number of nodes and k is the number of linked lists.