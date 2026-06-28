# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max], where min and max are the minimum and maximum values of the range. The goal is to minimize the length of this range, which is calculated as max - min. If there are multiple such ranges, return the one with the smallest minimum value. For example, given the lists [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], the smallest range covering elements from all lists is [20, 24].

## Approach
The algorithm uses a priority queue to keep track of the smallest element from each list. It iterates through the lists, updating the minimum and maximum values of the current range. The priority queue ensures that the smallest element is always considered first.

## Complexity
- Time: O(N log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        // Create a priority queue to store the current smallest element from each list
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        
        // Initialize the priority queue with the first element from each list
        for (int i = 0; i < nums.size(); i++) {
            pq.push({nums[i][0], i, 0});
        }
        
        // Initialize the minimum and maximum values of the range
        int min_val = INT_MAX;
        int max_val = INT_MIN;
        for (auto& num : nums) {
            min_val = min(min_val, num[0]);
            max_val = max(max_val, num[0]);
        }
        
        // Initialize the result
        vector<int> result = {min_val, max_val};
        
        // Iterate through the lists
        while (!pq.empty()) {
            // Get the smallest element from the priority queue
            auto curr = pq.top();
            pq.pop();
            
            // Update the minimum and maximum values of the range
            int curr_min = curr[0];
            int list_idx = curr[1];
            int elem_idx = curr[2];
            
            // Update the result if the current range is smaller
            if (max_val - curr_min < result[1] - result[0]) {
                result = {curr_min, max_val};
            }
            
            // If the current element is not the last element in its list, add the next element to the priority queue
            if (elem_idx + 1 < nums[list_idx].size()) {
                pq.push({nums[list_idx][elem_idx + 1], list_idx, elem_idx + 1});
                // Update the maximum value of the range
                max_val = max(max_val, nums[list_idx][elem_idx + 1]);
            } else {
                // If the current element is the last element in its list, break the loop
                break;
            }
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20, 24]
```

## Key Takeaways
- Use a priority queue to keep track of the smallest element from each list.
- Iterate through the lists, updating the minimum and maximum values of the current range.
- Use the priority queue to ensure that the smallest element is always considered first.