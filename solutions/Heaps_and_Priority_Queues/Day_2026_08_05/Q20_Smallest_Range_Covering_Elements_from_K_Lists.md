# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max], where min and max are the minimum and maximum values in the range, respectively. The lists are non-empty and contain distinct integers. For example, given the lists [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], the smallest range covering elements from all lists is [20, 24].

## Approach
We can solve this problem using a priority queue to keep track of the smallest element from each list. The priority queue will store pairs of (value, list_index, element_index). We will keep removing the smallest element from the queue and add the next element from the same list until we find a range that covers all lists.

## Complexity
- Time: O(N log K)
- Space: O(K)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        // Create a priority queue to store the smallest element from each list
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
        
        // Initialize the priority queue with the smallest element from each list
        for (int i = 0; i < nums.size(); i++) {
            pq.push({nums[i][0], i, 0});
        }
        
        // Initialize the range
        int min_range = INT_MAX;
        int max_range = INT_MIN;
        int min_val = INT_MAX;
        int max_val = INT_MIN;
        
        // Initialize a set to keep track of the lists that are covered
        unordered_set<int> covered;
        
        // Loop until we find a range that covers all lists
        while (!pq.empty()) {
            // Get the smallest element from the priority queue
            auto [val, list_index, element_index] = pq.top();
            pq.pop();
            
            // Update the range
            min_val = min(min_val, val);
            max_val = max(max_val, val);
            
            // Add the list to the covered set
            covered.insert(list_index);
            
            // If all lists are covered, update the range
            if (covered.size() == nums.size()) {
                if (max_val - min_val < max_range - min_range) {
                    min_range = min_val;
                    max_range = max_val;
                }
            }
            
            // Add the next element from the same list to the priority queue
            if (element_index + 1 < nums[list_index].size()) {
                pq.push({nums[list_index][element_index + 1], list_index, element_index + 1});
            } else {
                // If we have reached the end of a list, remove it from the covered set
                covered.erase(list_index);
            }
        }
        
        // Return the smallest range
        return {min_range, max_range};
    }
};
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20, 24]
```

## Key Takeaways
- We use a priority queue to keep track of the smallest element from each list.
- We use a set to keep track of the lists that are covered by the current range.
- We update the range whenever we find a smaller range that covers all lists.