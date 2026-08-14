# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max] where min and max are the minimum and maximum values in the range. If there are multiple ranges with the same size, return the one with the smallest min value. For example, given the lists [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], the smallest range covering elements from all lists is [20,24].

## Approach
We can use a priority queue to store the current smallest element from each list along with its list index and element index. We keep track of the minimum and maximum values in the queue and update the result if we find a smaller range. We then pop the smallest element from the queue and push the next element from the same list into the queue.

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
        // Create a min heap to store the current smallest element from each list
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        
        // Initialize the min and max values
        int minX = INT_MAX, maxX = INT_MIN;
        
        // Push the first element from each list into the queue
        for (int i = 0; i < nums.size(); i++) {
            int val = nums[i][0];
            pq.push({val, i, 0});
            minX = min(minX, val);
            maxX = max(maxX, val);
        }
        
        // Initialize the result
        vector<int> res = {minX, maxX};
        int range = maxX - minX;
        
        // Loop until we have processed all elements
        while (true) {
            // Get the smallest element from the queue
            vector<int> curr = pq.top();
            pq.pop();
            
            // Update the result if we find a smaller range
            if (maxX - curr[0] < range) {
                res = {curr[0], maxX};
                range = maxX - curr[0];
            }
            
            // If we have processed all elements from the current list, break
            if (curr[2] + 1 == nums[curr[1]].size()) {
                break;
            }
            
            // Push the next element from the same list into the queue
            int nextVal = nums[curr[1]][curr[2] + 1];
            pq.push({nextVal, curr[1], curr[2] + 1});
            minX = min(minX, nextVal);
            maxX = max(maxX, nextVal);
        }
        
        return res;
    }
};
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
```

## Key Takeaways
- We use a priority queue to efficiently find the smallest element from each list.
- We keep track of the minimum and maximum values in the queue to update the result.
- We use a while loop to process all elements from each list.