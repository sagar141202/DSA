# Sort List

## Problem Statement
Given the head of a linked list, sort it in ascending order and return the sorted list. The linked list will have at least one node, but it may have up to 5000 nodes. Each node's value will be between -5000 and 5000. For example, if the input is [4,2,1,3], the output will be [1,2,3,4]. If the input is [-1,5,3,4,0], the output will be [-1,0,3,4,5].

## Approach
We can solve this problem by first converting the linked list to a vector, then sorting the vector using the built-in sort function, and finally converting the sorted vector back to a linked list. This approach ensures that the time complexity remains reasonable despite the large number of nodes. The key insight here is to leverage existing sorting algorithms.

## Complexity
- Time: O(n log n)
- Space: O(n)

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
    ListNode* sortList(ListNode* head) {
        // Convert linked list to vector
        vector<int> values;
        while (head) {
            values.push_back(head->val);
            head = head->next;
        }
        
        // Sort the vector
        sort(values.begin(), values.end());
        
        // Convert sorted vector back to linked list
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        for (int val : values) {
            current->next = new ListNode(val);
            current = current->next;
        }
        
        return dummy->next;
    }
};
```

## Test Cases
```
Input: [4,2,1,3]
Output: [1,2,3,4]
Input: [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

## Key Takeaways
- Convert a linked list to a vector to utilize built-in sorting functions.
- Leverage the existing sort function in C++ to achieve efficient sorting.
- Convert the sorted vector back to a linked list to meet the problem's requirements.