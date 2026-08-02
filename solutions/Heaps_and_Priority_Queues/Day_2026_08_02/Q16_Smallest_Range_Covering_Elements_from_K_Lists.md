# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max] where min and max are integers. If multiple ranges have the same minimum length, return the range with the smallest minimum value. For example, given the lists [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], the smallest range covering elements from all lists is [20, 24].

## Approach
We can use a priority queue to keep track of the smallest element from each list. The algorithm starts by pushing the first element from each list into the priority queue. Then, it repeatedly removes the smallest element from the queue, updates the range if necessary, and pushes the next element from the same list into the queue.

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
        // Create a priority queue to store the elements
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        
        // Push the first element from each list into the queue
        for (int i = 0; i < nums.size(); i++) {
            pq.push({nums[i][0], i, 0});
        }
        
        // Initialize the range
        int min_range = INT_MAX;
        int max_range = INT_MIN;
        int min_val = INT_MAX;
        int max_val = INT_MIN;
        
        // Iterate over the queue
        while (!pq.empty()) {
            // Get the smallest element from the queue
            vector<int> curr = pq.top();
            pq.pop();
            
            // Update the range
            min_val = min(min_val, curr[0]);
            max_val = max(max_val, curr[0]);
            
            // If the current range is smaller than the min range, update the min range
            if (max_val - min_val < min_range) {
                min_range = max_val - min_val;
                max_range = max_val;
            } else if (max_val - min_val == min_range && min_val < min_range) {
                min_range = max_val - min_val;
                max_range = max_val;
            }
            
            // Push the next element from the same list into the queue
            if (curr[2] + 1 < nums[curr[1]].size()) {
                pq.push({nums[curr[1]][curr[2] + 1], curr[1], curr[2] + 1});
            }
        }
        
        // Return the smallest range
        return {min_val, max_val};
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
- The time complexity is O(N log K) where N is the total number of elements and K is the number of lists.
- The space complexity is O(K) where K is the number of lists.