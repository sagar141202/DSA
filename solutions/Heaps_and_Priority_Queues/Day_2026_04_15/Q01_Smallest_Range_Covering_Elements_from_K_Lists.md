# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max] where min and max are the minimum and maximum values in the range. If there are multiple such ranges, return the one with the smallest length. For example, if we have three lists [1, 5, 10], [2, 4, 6], and [3, 7, 8], the smallest range covering elements from all lists is [2, 3] or [3, 4] or [4, 5] with a length of 1 or [3, 6] or [2, 5] or [2, 7] with a length of 3 or 4 or 5 respectively, but the smallest one is [2, 3] or [3, 4] or [4, 5]. 

## Approach
We can use a priority queue to store the current smallest element from each list along with its list index and element index. We keep track of the maximum element in the current range and update the range if a smaller range is found. The priority queue ensures that we always consider the smallest element from each list.

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
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> minHeap;
        
        // Initialize the heap with the first element from each list
        for (int i = 0; i < nums.size(); i++) {
            minHeap.push({nums[i][0], i, 0});
        }
        
        // Initialize the range with the maximum and minimum values
        int rangeMin = *min_element(nums[0].begin(), nums[0].end());
        int rangeMax = *max_element(nums[0].begin(), nums[0].end());
        for (int i = 1; i < nums.size(); i++) {
            rangeMin = min(rangeMin, *min_element(nums[i].begin(), nums[i].end()));
            rangeMax = max(rangeMax, *max_element(nums[i].begin(), nums[i].end()));
        }
        
        // Initialize the result range
        vector<int> result = {rangeMin, rangeMax};
        int minRange = rangeMax - rangeMin;
        
        // Keep track of the maximum element in the current range
        int currentMax = rangeMax;
        
        // Loop until the heap is empty
        while (!minHeap.empty()) {
            // Get the smallest element from the heap
            auto [val, listIndex, elementIndex] = minHeap.top();
            minHeap.pop();
            
            // Update the result range if a smaller range is found
            if (currentMax - val < minRange) {
                minRange = currentMax - val;
                result = {val, currentMax};
            }
            
            // If the current element is the last element in its list, break the loop
            if (elementIndex == nums[listIndex].size() - 1) {
                break;
            }
            
            // Push the next element from the current list into the heap
            minHeap.push({nums[listIndex][elementIndex + 1], listIndex, elementIndex + 1});
            
            // Update the maximum element in the current range
            currentMax = max(currentMax, nums[listIndex][elementIndex + 1]);
        }
        
        return result;
    }
};

int main() {
    Solution solution;
    vector<vector<int>> nums = {{1, 5, 10}, {2, 4, 6}, {3, 7, 8}};
    vector<int> result = solution.smallestRange(nums);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    return 0;
}
```

## Test Cases
```
Input: [[1, 5, 10], [2, 4, 6], [3, 7, 8]]
Output: [2, 3] or [3, 4] or [4, 5]
```

## Key Takeaways
- We use a priority queue to efficiently find the smallest element from each list.
- We keep track of the maximum element in the current range to update the result range.
- The time complexity is O(N log K) where N is the total number of elements and K is the number of lists.