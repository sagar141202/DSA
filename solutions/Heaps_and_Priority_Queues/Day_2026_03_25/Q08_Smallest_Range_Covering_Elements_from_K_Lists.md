# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max] where min and max are the minimum and maximum values in the range. The goal is to minimize the length of the range, i.e., max - min. For example, if we have three lists [1, 3, 5], [2, 4, 6], and [7, 8, 9], the smallest range covering at least one element from each list is [2, 7] with a length of 5.

## Approach
We can use a priority queue to keep track of the smallest elements from each list. The priority queue will store pairs of (value, list_index) where value is the smallest element from the list and list_index is the index of the list. We will keep removing the smallest element from the priority queue and adding the next element from the same list until we find a range that covers at least one element from each list.

## Complexity
- Time: O(N log K) where N is the total number of elements across all lists and K is the number of lists.
- Space: O(K) for storing the priority queue.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        // Create a priority queue to store the smallest elements from each list
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        
        // Initialize the priority queue with the smallest elements from each list
        for (int i = 0; i < nums.size(); i++) {
            pq.push({nums[i][0], i, 0});
        }
        
        // Initialize the range and the maximum value in the range
        int rangeMin = INT_MAX, rangeMax = INT_MIN;
        int maxVal = INT_MIN;
        
        // Iterate over the priority queue to find the smallest range
        while (!pq.empty()) {
            // Get the smallest element from the priority queue
            auto curr = pq.top();
            pq.pop();
            
            // Update the range and the maximum value in the range
            rangeMin = min(rangeMin, curr[0]);
            rangeMax = max(rangeMax, curr[0]);
            maxVal = max(maxVal, curr[0]);
            
            // If the range covers at least one element from each list, return the range
            if (pq.empty() || maxVal - rangeMin > rangeMax - rangeMin) {
                break;
            }
            
            // Add the next element from the same list to the priority queue
            if (curr[2] + 1 < nums[curr[1]].size()) {
                pq.push({nums[curr[1]][curr[2] + 1], curr[1], curr[2] + 1});
            }
        }
        
        // Return the smallest range
        return {rangeMin, rangeMax};
    }
};
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
```

## Key Takeaways
- We use a priority queue to keep track of the smallest elements from each list.
- We iterate over the priority queue to find the smallest range that covers at least one element from each list.
- The time complexity is O(N log K) where N is the total number of elements across all lists and K is the number of lists.