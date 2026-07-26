# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max], where min and max are the minimum and maximum values in the range, respectively. The goal is to minimize the difference between max and min. For example, if we have three lists: [1, 5, 10], [2, 4, 6], and [3, 7, 8], the smallest range covering elements from all three lists is [2, 4] or [3, 3] or [4, 4] with a range difference of 2 or 0 or 0, respectively. However, since we are looking for the smallest range, the answer would be [3, 3] with a range difference of 0.

## Approach
We use a priority queue to keep track of the smallest element from each list. The priority queue stores pairs of the form (value, list_index, element_index). We initialize the priority queue with the first element from each list and then keep removing the smallest element from the priority queue and adding the next element from the same list until we find a range that covers at least one element from each list. The range is updated whenever we find a smaller range.

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
        // Create a priority queue to store elements from the lists
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        
        // Initialize the priority queue with the first element from each list
        for (int i = 0; i < nums.size(); i++) {
            pq.push({nums[i][0], i, 0});
        }
        
        // Initialize the range
        int rangeMin = INT_MIN;
        int rangeMax = INT_MAX;
        
        // Initialize the current maximum value in the range
        int currMax = *max_element(nums.begin(), nums.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        while (true) {
            // Get the smallest element from the priority queue
            vector<int> smallest = pq.top();
            pq.pop();
            
            // Update the range if the current range is smaller
            if (currMax - smallest[0] < rangeMax - rangeMin) {
                rangeMin = smallest[0];
                rangeMax = currMax;
            }
            
            // If we have reached the end of any list, break the loop
            if (smallest[2] == nums[smallest[1]].size() - 1) {
                break;
            }
            
            // Add the next element from the same list to the priority queue
            pq.push({nums[smallest[1]][smallest[2] + 1], smallest[1], smallest[2] + 1});
            
            // Update the current maximum value in the range
            currMax = max(currMax, nums[smallest[1]][smallest[2] + 1]);
        }
        
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
- We use a priority queue to efficiently find the smallest element from each list.
- We update the range whenever we find a smaller range.
- The time complexity is O(N log K), where N is the total number of elements and K is the number of lists.