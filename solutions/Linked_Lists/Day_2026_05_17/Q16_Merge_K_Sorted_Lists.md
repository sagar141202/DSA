# Merge K Sorted Lists

## Problem Statement
Merge k sorted linked lists and return it as one sorted list. The lists are defined as a node with an integer value and a pointer to the next node. The input is an array of k linked lists, and the output is a single sorted linked list. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the output will be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6.

## Approach
We can use a priority queue to store the current smallest node from each list. The priority queue will store pairs of the node's value and the list it belongs to. We will keep removing the smallest node from the queue and add it to the result list, then add the next node from the same list to the queue if it exists.

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
        bool operator()(const pair<int, ListNode*>& a, const pair<int, ListNode*>& b) {
            return a.first > b.first;
        }
    };

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<pair<int, ListNode*>, vector<pair<int, ListNode*>>, compare> pq;
        
        // Add the head of each list to the priority queue
        for (auto list : lists) {
            if (list) {
                pq.push({list->val, list});
            }
        }

        // Create a dummy node to serve as the start of the result list
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;

        // Merge the lists
        while (!pq.empty()) {
            // Get the node with the smallest value from the priority queue
            auto [val, node] = pq.top();
            pq.pop();

            // Add the node to the result list
            current->next = node;
            current = current->next;

            // Add the next node from the same list to the priority queue
            if (node->next) {
                pq.push({node->next->val, node->next});
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
- Use a priority queue to efficiently select the smallest node from the k lists.
- Create a dummy node to simplify the code and avoid special cases for the head of the result list.
- The time complexity is O(N log k) where N is the total number of nodes across all k lists.