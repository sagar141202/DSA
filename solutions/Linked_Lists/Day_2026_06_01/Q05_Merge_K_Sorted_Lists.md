# Merge K Sorted Lists

## Problem Statement
You are given an array of 'k' linked lists, each of which is sorted in ascending order. Merge these linked lists into a single sorted linked list. The head of each linked list is given as an array of ListNode pointers. The definition of a ListNode is: struct ListNode { int val; ListNode *next; ListNode() : val(0), next(nullptr) {}; ListNode(int x) : val(x), next(nullptr) {}; ListNode(int x, ListNode *next) : val(x), next(next) {} };. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, then the merged list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6.

## Approach
We can solve this problem using a priority queue to store the current smallest node from each linked list. The priority queue will automatically sort the nodes based on their values, so we can simply extract the smallest node and add it to our result list. We will repeat this process until all nodes are processed.

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
            if (list) {
                pq.push(list);
            }
        }

        ListNode* head = new ListNode();
        ListNode* curr = head;

        while (!pq.empty()) {
            ListNode* node = pq.top();
            pq.pop();
            curr->next = node;
            curr = curr->next;
            if (node->next) {
                pq.push(node->next);
            }
        }

        return head->next;
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
- We use a priority queue to efficiently find the smallest node from the linked lists.
- We use a compare function to define the order of the nodes in the priority queue.
- The time complexity is O(N log k) where N is the total number of nodes and k is the number of linked lists.