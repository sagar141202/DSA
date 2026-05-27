# 3Sum

## Problem Statement
Given an integer array `nums`, find all unique triplets in the array which gives the sum of zero. The solution should not contain duplicate triplets. The array can contain duplicate elements, but the triplets should be unique. For example, given the array `[-1,0,1,2,-1,-4]`, the output should be `[[-1,-1,2],[-1,0,1]]`.

## Approach
The approach to solve this problem is to use a two-pointer technique. First, sort the array and then fix one element, and use two pointers to find the other two elements that sum up to the negation of the fixed element. This ensures that the sum of the three elements is zero.

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
            // Skip the same result
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            // Initialize two pointers
            int left = i + 1;
            int right = nums.size() - 1;
            
            // Find the other two elements
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum < 0) left++;
                else if (sum > 0) right--;
                else {
                    result.push_back({nums[i], nums[left], nums[right]});
                    // Skip the same result
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++;
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
Input: [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Input: []
Output: []
Input: [0]
Output: []
```

## Key Takeaways
- Sort the array to apply the two-pointer technique.
- Skip the same result to avoid duplicates in the output.
- Use two pointers to find the other two elements that sum up to the negation of the fixed element.