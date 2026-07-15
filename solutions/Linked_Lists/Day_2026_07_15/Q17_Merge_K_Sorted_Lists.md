# Merge K Sorted Lists

## Problem Statement
Given an array of 'k' linked lists, merge them into one sorted linked list. Each linked list is sorted in ascending order. The merged linked list should also be sorted in ascending order. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged linked list will be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6.

## Approach
We will use a priority queue to store the current smallest node from each linked list. The node with the smallest value will be extracted from the queue and added to the merged list. We will then add the next node from the same linked list to the queue. This process will continue until all nodes are merged.

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
        
        // Add the head of each linked list to the priority queue
        for (auto list : lists) {
            if (list) {
                pq.push(list);
            }
        }

        // Create a dummy node to simplify the code
        ListNode* dummy = new ListNode();
        ListNode* current = dummy;

        // Merge the linked lists
        while (!pq.empty()) {
            ListNode* smallest = pq.top();
            pq.pop();
            current->next = smallest;
            current = current->next;
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
Input: [[1, 4, 5], [1, 3, 4], [2, 6]]
Output: [1, 1, 2, 3, 4, 4, 5, 6]
```

## Key Takeaways
- Use a priority queue to efficiently select the smallest node from the linked lists.
- Create a dummy node to simplify the code and avoid special cases for the head of the merged linked list.
- The time complexity is O(N log k) because we perform a heap operation for each node, and each heap operation takes O(log k) time.