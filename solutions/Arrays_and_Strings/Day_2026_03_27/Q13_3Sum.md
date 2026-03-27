# 3Sum

## Problem Statement
Given an array of integers `nums`, find all unique triplets in the array that sum to zero. The solution should not contain duplicate triplets. The input array can contain duplicate elements, and the triplets should be returned in a sorted order. For example, given the input `nums = [-1,0,1,2,-1,-4]`, the output should be `[[-1,-1,2],[-1,0,1]]`.

## Approach
The algorithm uses a two-pointer technique to find the triplets. It first sorts the input array and then iterates over each element, using two pointers to find a pair of elements that sum to the negation of the current element. The algorithm skips duplicate elements to avoid duplicate triplets.

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
        // Sort the input array
        sort(nums.begin(), nums.end());
        
        // Initialize the result vector
        vector<vector<int>> result;
        
        // Iterate over each element in the array
        for (int i = 0; i < nums.size() - 2; i++) {
            // Skip duplicate elements
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            // Initialize two pointers
            int left = i + 1;
            int right = nums.size() - 1;
            
            // Find a pair of elements that sum to the negation of the current element
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                // If the sum is zero, add the triplet to the result vector
                if (sum == 0) {
                    result.push_back({nums[i], nums[left], nums[right]});
                    
                    // Skip duplicate elements
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    
                    // Move the pointers
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
- The two-pointer technique is useful for finding pairs of elements that sum to a target value.
- Sorting the input array can help to simplify the problem and avoid duplicate triplets.
- Skipping duplicate elements is essential to avoid duplicate triplets in the result vector.