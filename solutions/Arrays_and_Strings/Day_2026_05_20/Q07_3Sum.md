# 3Sum

## Problem Statement
Given an array `nums` of `n` integers, find all unique triplets in the array which gives the sum of zero. The solution should not contain duplicate triplets. For example, given the array `nums = [-1,0,1,2,-1,-4]`, the output should be `[[-1,-1,2],[-1,0,1]]`. The array can contain duplicate elements, and the length of the array can be up to `10^4` elements.

## Approach
The approach is to use a two-pointer technique with a sorted array. First, we sort the array, then for each element, we use two pointers to find the other two elements that sum up to the negation of the current element. This approach ensures that we find all unique triplets with a sum of zero.

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
        
        // Initialize the result vector
        vector<vector<int>> result;
        
        // Iterate over the array
        for (int i = 0; i < nums.size() - 2; i++) {
            // Skip the same result
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
                    
                    // Move the pointers and skip the same result
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
Input: nums = []
Output: []
Input: nums = [0]
Output: []
```

## Key Takeaways
- Sort the array before using the two-pointer technique to ensure that the solution is efficient and scalable.
- Use a two-pointer technique to find the other two elements that sum up to the negation of the current element.
- Skip the same result to avoid duplicates in the solution.