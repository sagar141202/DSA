# Merge K Sorted Lists

## Problem Statement
Merge k sorted linked lists and return it as one sorted list. The lists are defined as follows: 
- Each list node has an integer value and a pointer to the next node in the list.
- The input is an array of k linked-lists, where each element is the head of a linked list.
- The output is the head of the merged linked list.
- The linked lists can contain duplicate values and are not guaranteed to be non-empty.
- Example: Input: `[[1,4,5],[1,3,4],[2,6]]`, Output: `[1,1,2,3,4,4,5,6]`.

## Approach
We will utilize a min-heap data structure to efficiently merge the k sorted lists. The min-heap will store the current smallest node from each list, allowing us to extract the smallest node and add it to the result list in O(log k) time. We will repeat this process until all nodes have been processed.

## Complexity
- Time: O(N log k)
- Space: O(k)

## C++ Solution
```cpp
#include <queue>
#include <vector>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

struct Compare {
    bool operator()(const ListNode* a, const ListNode* b) {
        return a->val > b->val;
    }
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // Create a min-heap to store the current smallest node from each list
        priority_queue<ListNode*, vector<ListNode*>, Compare> minHeap;
        
        // Add the head of each list to the min-heap
        for (ListNode* head : lists) {
            if (head) {
                minHeap.push(head);
            }
        }
        
        // Create a dummy node to serve as the head of the result list
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Merge the lists
        while (!minHeap.empty()) {
            // Extract the smallest node from the min-heap
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
        
        // Return the head of the result list
        return dummy->next;
    }
};
```

## Test Cases
```
Input: [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Input: []
Output: []
Input: [[1]]
Output: [1]
```

## Key Takeaways
- Utilize a min-heap data structure to efficiently merge k sorted lists.
- The time complexity of the solution is O(N log k), where N is the total number of nodes across all lists.
- The space complexity of the solution is O(k), where k is the number of lists.