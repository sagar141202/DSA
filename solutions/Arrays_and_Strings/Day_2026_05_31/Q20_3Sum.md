# 3Sum

## Problem Statement
Given an integer array `nums`, find all unique triplets in the array which gives the sum of zero. The solution should not contain duplicate triplets. For example, given the array `nums = [-1,0,1,2,-1,-4]`, the output should be `[[-1,-1,2],[-1,0,1]]`. The array can contain duplicate elements, and the length of the array is not fixed.

## Approach
The approach is to use a two-pointer technique with sorting. First, sort the array, then fix one element and use two pointers to find the other two elements that sum up to the negation of the fixed element. This approach ensures that all possible triplets are considered and that duplicates are avoided.

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
        // Sort the array
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        
        // Iterate over the array
        for (int i = 0; i < nums.size() - 2; i++) {
            // Skip duplicates for the first element
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            // Initialize two pointers
            int left = i + 1;
            int right = nums.size() - 1;
            
            // Find the other two elements
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                // If the sum is zero, add the triplet to the result
                if (sum == 0) {
                    result.push_back({nums[i], nums[left], nums[right]});
                    
                    // Move the pointers and skip duplicates
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++;
                    right--;
                }
                // If the sum is less than zero, move the left pointer
                else if (sum < 0) {
                    left++;
                }
                // If the sum is greater than zero, move the right pointer
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
Input: nums = [0,1,1]
Output: []
Input: nums = [0,0,0]
Output: [[0,0,0]]
```

## Key Takeaways
- Sorting the array helps to avoid duplicates and to apply the two-pointer technique.
- The two-pointer technique is useful for finding pairs or triplets in a sorted array that sum up to a target value.
- Skipping duplicates is crucial to avoid duplicate triplets in the result.