# Merge K Sorted Lists

## Problem Statement
Given an array of 'k' linked lists, merge them into one sorted linked list. Each linked list is sorted in ascending order. The arrays of linked lists are given as [list1, list2, ..., listk]. The task is to return a new sorted linked list containing all the elements from the given linked lists. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the output should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6.

## Approach
We can use a min-heap data structure to efficiently merge the linked lists. The min-heap will store the current smallest node from each linked list. We will keep removing the smallest node from the heap and adding it to the result list, and then add the next node from the same list to the heap.

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
    struct comparator {
        bool operator()(const ListNode* a, const ListNode* b) {
            return a->val > b->val;
        }
    };

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // Create a min-heap to store the current smallest node from each linked list
        priority_queue<ListNode*, vector<ListNode*>, comparator> minHeap;
        
        // Add the head of each linked list to the min-heap
        for (auto list : lists) {
            if (list) {
                minHeap.push(list);
            }
        }
        
        // Create a dummy node to serve as the head of the result list
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Merge the linked lists
        while (!minHeap.empty()) {
            // Remove the smallest node from the min-heap
            ListNode* smallest = minHeap.top();
            minHeap.pop();
            
            // Add the smallest node to the result list
            current->next = smallest;
            current = current->next;
            
            // Add the next node from the same list to the min-heap
            if (smallest->next) {
                minHeap.push(smallest->next);
            }
        }
        
        // Return the result list
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
- Use a min-heap data structure to efficiently merge the linked lists.
- The min-heap stores the current smallest node from each linked list.
- The time complexity is O(N log k), where N is the total number of nodes and k is the number of linked lists.