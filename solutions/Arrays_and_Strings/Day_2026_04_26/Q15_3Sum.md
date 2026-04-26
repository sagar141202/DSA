# 3Sum

## Problem Statement
Given an array of integers `nums`, find all unique triplets in the array which gives the sum of zero. The solution should not contain duplicate triplets. For example, given `nums = [-1,0,1,2,-1,-4]`, the output should be `[[-1,-1,2],[-1,0,1]]`. The array can contain duplicate elements and the length of the array is not fixed.

## Approach
The algorithm uses a two-pointer technique with sorting to find the triplets. First, sort the array and then fix one element, and use two pointers to find the other two elements that sum up to the negation of the fixed element.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // sort the array
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        
        // iterate over the array
        for (int i = 0; i < nums.size() - 2; i++) {
            // skip duplicates
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            // two pointers
            int left = i + 1;
            int right = nums.size() - 1;
            
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                // if sum is zero, add to result
                if (sum == 0) {
                    result.push_back({nums[i], nums[left], nums[right]});
                    // skip duplicates
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++;
                    right--;
                } 
                // if sum is less than zero, move left pointer
                else if (sum < 0) {
                    left++;
                } 
                // if sum is greater than zero, move right pointer
                else {
                    right--;
                }
            }
        }
        return result;
    }
};
```

## Test Cases
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

## Key Takeaways
- Sorting the array first helps to avoid duplicates and apply the two-pointer technique efficiently.
- Skipping duplicates is crucial to avoid duplicate triplets in the result.
- The two-pointer technique is used to find the other two elements that sum up to the negation of the fixed element.