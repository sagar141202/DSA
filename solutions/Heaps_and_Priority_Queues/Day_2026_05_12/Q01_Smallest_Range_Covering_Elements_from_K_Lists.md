# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max] where min and max are the minimum and maximum values in the range. If there are multiple such ranges, return the one with the smallest length. The input lists are not empty and contain only unique integers. The number of lists K is between 1 and 100, and the total number of elements across all lists is at most 1000.

## Approach
We can use a min-heap to store the current smallest element from each list along with its list index and element index. We then repeatedly extract the smallest element from the heap, update the range if necessary, and insert the next element from the same list into the heap. This process continues until we have exhausted all elements from all lists.

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
        // Create a min-heap to store the current smallest element from each list
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> minHeap;
        
        // Initialize the min-heap with the first element from each list
        for (int i = 0; i < nums.size(); i++) {
            minHeap.push({nums[i][0], i, 0});
        }
        
        // Initialize the range
        int minVal = INT_MAX;
        int maxVal = INT_MIN;
        for (auto& num : nums) {
            minVal = min(minVal, num[0]);
            maxVal = max(maxVal, num[0]);
        }
        
        // Initialize the result range
        vector<int> result = {minVal, maxVal};
        
        // Repeat the process until we have exhausted all elements from all lists
        while (true) {
            // Extract the smallest element from the heap
            auto [val, listIdx, elemIdx] = minHeap.top();
            minHeap.pop();
            
            // Update the range if necessary
            if (maxVal - val < result[1] - result[0]) {
                result = {val, maxVal};
            }
            
            // If we have exhausted all elements from the current list, break
            if (elemIdx + 1 == nums[listIdx].size()) {
                break;
            }
            
            // Insert the next element from the same list into the heap
            minHeap.push({nums[listIdx][elemIdx + 1], listIdx, elemIdx + 1});
            
            // Update the maxVal
            maxVal = max(maxVal, nums[listIdx][elemIdx + 1]);
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
```

## Key Takeaways
- We can use a min-heap to efficiently find the smallest range covering elements from K lists.
- The time complexity of this solution is O(N log K) where N is the total number of elements across all lists and K is the number of lists.
- The space complexity is O(K) as we need to store K elements in the min-heap.